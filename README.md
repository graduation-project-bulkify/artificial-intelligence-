# Bulkify Recommendation System

## Overview
This project implements a recommendation system designed to help users discover products tailored to their preferences on the Bulkify platform. The system generates personalized product suggestions based on users' past ratings and similar users' preferences.

## Approach
The recommendation system utilizes **Collaborative Filtering**, a popular technique that leverages user-item interactions without requiring detailed product information. Collaborative Filtering identifies users with similar rating patterns and recommends products liked by those similar users.

### Why Collaborative Filtering?
- Does not require product metadata (descriptions or categories).
- Relies solely on user-product interaction data.
- Well-suited for platforms with large numbers of users and ratings.

## Algorithm Used: Singular Value Decomposition (SVD)
The system applies the SVD matrix factorization technique to analyze and reduce the dimensionality of the user-product rating matrix.

### Implementation Steps:
1. **Build the Ratings Matrix:**
   - Rows represent users.
   - Columns represent products.
   - Values are the ratings given by users to products.
2. **Convert the matrix to a Sparse Matrix format** to optimize memory usage.
3. **Apply SVD** to decompose the matrix into three matrices:  
   \( R \approx U \times \Sigma \times V^T \)
4. **Reconstruct predicted ratings** for user-product pairs that lack explicit ratings.

## Recommendation Logic
- **Existing Users:**  
  Recommend the highest predicted rated products that the user has not rated yet.
- **New Users:**  
  Recommend the most popular products based on overall ratings from all users.

## Deployment
- Built a RESTful API using **FastAPI**, a modern and fast Python web framework.
- Containerized the application with **Docker** for environment consistency.
- Deployed on **Railway.app**, a free and easy-to-use cloud platform for backend services.
- The API offers an interactive documentation interface accessible at `/docs` via Swagger UI, enabling straightforward integration with frontend or other services.

## Summary
- Scalable and maintainable recommendation system.
- Supports data updates and retraining of the model at any time.
- Provides a robust backend API for easy access to personalized recommendations.

