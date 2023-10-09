# Rating Product & Sorting Reviews on Amazon

This project focuses on solving two key problems in e-commerce: accurately calculating ratings for products based on recent reviews and sorting reviews effectively. Solving these problems can lead to improved customer satisfaction, increased product visibility for sellers, and a seamless shopping experience for buyers.

## Dataset

The dataset contains Amazon product data, including various metadata and user reviews. It focuses on the electronics category and includes user ratings and comments for the product with the highest number of reviews.

- `reviewerID`: User ID
- `asin`: Product ID
- `reviewerName`: User Name
- `helpful`: Helpful rating
- `reviewText`: Review text
- `overall`: Product rating
- `summary`: Review summary
- `unixReviewTime`: Review timestamp
- `reviewTime`: Review timestamp (Raw)
- `day_diff`: Days since the review was posted
- `helpful_yes`: Number of times the review was found helpful
- `total_vote`: Total number of votes for the review

## Tasks

### Calculate Weighted Average Rating

- Read the Dataset and Calculate the Initial Average Rating
- Weighted averages are computed for four different time periods.
- The results are compared to the initial average product rating.

### Determine the Top 20 Reviews for Display
- The `helpful_no` variable, representing the number of unhelpful votes, is generated.
- Three sorting scores are calculated for each review:
  1. `score_pos_neg_diff`: The difference between the number of helpful and unhelpful votes.
  2. `score_average_rating`: The ratio of helpful votes to the total votes.
  3. `wilson_lower_bound`: The lower bound of the Wilson Score Confidence Interval.

#### Wilson Lower Bound (WLB):
- Wilson Lower Bound is particularly useful for making more reliable evaluations, especially for reviews with a low number of votes.
- WLB does not rely on categorizing reviews as "positive" or "negative" and, therefore, does not require specific assumptions about the voting system.
- It is used to balance out uncertain or low-vote reviews and provides a more general evaluation.
- WLB calculates a product's ranking by taking into account the "quality" of a review.

#### Score Average Rating:
- Score Average Rating represents a simple average rating approach.
- This method is based directly on review ratings and treats positive and negative votes equally.
- Score Average Rating assumes an equal weight for each review and places more emphasis on high-rated reviews.
- It is often used as a simpler approach and can allow for faster calculations, especially with large datasets.

## How to Use

1. Clone this repository to your local machine.
2. Ensure you have Python and the required libraries installed.
3. Run the Jupyter Notebook or Python script to execute the code.
4. Use the provided Python code and the "amazon_review.csv" dataset to perform the analysis.


Enjoy increasing product visibility for sellers and a seamless shopping experience for buyers!
