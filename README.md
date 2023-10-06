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

## Task 1: Calculate Weighted Average Rating

- Read the Dataset and Calculate the Initial Average Rating
- Time-based weighted average ratings are calculated based on the age of the reviews (quartiles).
- Weighted averages are computed for four different time periods.
- The results are compared to the initial average product rating.

## Task 2: Determine the Top 20 Reviews for Display
- The `helpful_no` variable, representing the number of unhelpful votes, is generated.
- It is derived from existing variables since there is no direct `helpful_no` column.
- Three sorting scores are calculated for each review:
  1. `score_pos_neg_diff`: The difference between the number of helpful and unhelpful votes.
  2. `score_average_rating`: The ratio of helpful votes to the total votes.
  3. `wilson_lower_bound`: The lower bound of the Wilson Score Confidence Interval.
- The top 20 reviews are determined for each sorting score.
- These reviews are suitable for display on the product detail page.

## How to Use

1. Clone this repository to your local machine.
2. Ensure you have Python and the required libraries installed.
3. Run the Jupyter Notebook or Python script to execute the code.
4. Use the provided Python code and the "amazon_review.csv" dataset to perform the analysis.
   

Enjoy increasing product visibility for sellers and a seamless shopping experience for buyers!
