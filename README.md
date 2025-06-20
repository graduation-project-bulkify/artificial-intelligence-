# artificial-intelligence-
1. Introduction This documentation outlines the development and deployment of a
Recommendation System using Collaborative Filtering. The goal of the system is to suggest
personalized product recommendations to users based on the preferences and behaviors of
other users. The system was implemented in Python and deployed using FastAPI as a web
framework and Railway.app for hosting.
2. Problem Statement In modern e-commerce and content platforms, helping users discover
relevant products is crucial. Traditional sorting by popularity or category is limited and not
tailored. Hence, a recommendation engine was developed to enhance user experience by
providing personalized suggestions.
3. Data Description The dataset used includes:
• user_id: Unique identifier for users
• prod_id: Product identifier
• rating: User rating for a product (typically from 1 to 5)
From this, a user-item interaction matrix was constructed, which serves as the basis for
collaborative filtering.
4. Methodology: Collaborative Filtering We used memory-based collaborative filtering with
user-item ratings matrix. This technique works on the assumption that if two users rate items
similarly in the past, they are likely to rate other items similarly in the future.
Steps followed:
1. Data Preprocessing:
o Constructed a sparse matrix of users vs products
o Missing values filled with zeros (indicating no interaction)
2. Model Construction:
o Predicted missing ratings using similarity of users
o The predicted matrix was saved as predicted_ratings.pkl
o Original matrix and raw dataframe also saved for lookup
5. Backend API with FastAPI The core logic was deployed using FastAPI. The main endpoint is:
• POST /recommend: Takes a user_id and optional num_recommendations
The logic inside the API performs:
• If the user exists in the matrix, it retrieves predicted ratings
• Filters unseen items
• Returns top-N items with highest predicted ratings
• If user not found, fallback to most popular products
API Request Example:
{
"user_id": "U123",
"num_recommendations": 5
}
API Response Example:
{
"user_id": "U123",
"recommendations": ["P102", "P330", "P218" , "P370" , "P430"]
}
6. Deployment
• The FastAPI application was containerized using Docker
• A Dockerfile was created to build the image
• The app was deployed on Railway.app
