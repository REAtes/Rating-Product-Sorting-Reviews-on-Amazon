# ###  Calculate Weighted Average Rating
# 1. Read the Dataset and Calculate the Initial Average Rating
# 2. Weighted averages are computed for four different time periods.
# 3. The results are compared to the initial average product rating.

import matplotlib.pyplot as plt
import pandas as pd
import math
import scipy.stats as st

df = pd.read_csv("amazon_review.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 1500)


def time_based_weighted_average(dataframe, w1=20, w2=10, w3=10, w4=10, w5=50):
    return dataframe.loc[dataframe["day_diff"] <= dataframe["day_diff"].quantile(0.20), "overall"].mean() * w1 /100 + \
           dataframe.loc[(dataframe["day_diff"] > dataframe["day_diff"].quantile(0.20)) &
                         (dataframe["day_diff"] <= dataframe["day_diff"].quantile(0.40)), "overall"].mean() * w2 / 100 + \
           dataframe.loc[(dataframe["day_diff"] > dataframe["day_diff"].quantile(0.40)) &
                         (dataframe["day_diff"] <= dataframe["day_diff"].quantile(0.60)), "overall"].mean() * w3 / 100 + \
           dataframe.loc[(dataframe["day_diff"] > dataframe["day_diff"].quantile(0.60)) &
                         (dataframe["day_diff"] <= dataframe["day_diff"].quantile(0.80)), "overall"].mean() * w4 / 100 + \
           dataframe.loc[dataframe["day_diff"] > dataframe["day_diff"].quantile(0.80), "overall"].mean() * w5 / 100


initial_avg_rating = df["overall"].mean()  # 4.6
time_based_weighted_average(df)  # 4.5


# ### Determine the Top 20 Reviews for Display
# 1. The helpful_no variable, representing the number of unhelpful votes, is generated.
# 2. It is derived from existing variables since there is no direct helpful_no column.
# 3. Three sorting scores are calculated for each review:
#    1. score_pos_neg_diff: The difference between the number of helpful and unhelpful votes.
#    2. score_average_rating: The ratio of helpful votes to the total votes.
#    3. wilson_lower_bound: The lower bound of the Wilson Score Confidence Interval.


df["helpful_no"] = df["total_vote"] - df["helpful_yes"]


def score_up_down_diff(up, down):
    return up - down


def score_average_rating(up, down):
    if up + down == 0:
        return 0
    return up / (up + down)


def wilson_lower_bound(up, down, confidence=0.95):
    """
    Wilson Lower Bound Score hesapla

    - Bernoulli parametresi p için hesaplanacak güven aralığının alt sınırı WLB skoru olarak kabul edilir.
    - Hesaplanacak skor ürün sıralaması için kullanılır.
    - Not:
    Eğer skorlar 1-5 arasıdaysa 1-3 negatif, 4-5 pozitif olarak işaretlenir ve bernoulli'ye uygun hale getirilebilir.
    Bu beraberinde bazı problemleri de getirir. Bu sebeple bayesian average rating yapmak gerekir.

    Parameters
    ----------
    up: int
        up count
    down: int
        down count
    confidence: float
        confidence

    Returns
    -------
    wilson score: float

    """
    n = up + down
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)


df["score_pos_neg_diff"] = df.apply(lambda x: score_up_down_diff(x["helpful_yes"], x["helpful_no"]), axis=1)
df.sort_values("score_pos_neg_diff", ascending=False).head(20)

df["score_average_rating"] = df.apply(lambda x: score_average_rating(x["helpful_yes"], x["helpful_no"]), axis=1)
df.sort_values("score_average_rating", ascending=False).head(20)

df["wilson_lower_bound"] = df.apply(lambda x: wilson_lower_bound(x["helpful_yes"], x["helpful_no"]), axis=1)
df.sort_values("wilson_lower_bound", ascending=False).head(20)

"""
Wilson Lower Bound (WLB):
- Wilson Lower Bound is particularly useful for making more reliable evaluations, especially for reviews with a low 
number of votes.
- WLB does not rely on categorizing reviews as "positive" or "negative" and, therefore, does not require specific 
assumptions about the voting system.
- It is used to balance out uncertain or low-vote reviews and provides a more general evaluation.
- WLB calculates a product's ranking by taking into account the "quality" of a review.

Score Average Rating:
- Score Average Rating represents a simple average rating approach.
- This method is based directly on review ratings and treats positive and negative votes equally.
- Score Average Rating assumes an equal weight for each review and places more emphasis on high-rated reviews.
- It is often used as a simpler approach and can allow for faster calculations, especially with large datasets.
"""
