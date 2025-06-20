from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import os
from scipy.sparse import csr_matrix
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Recommendation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Allow all origins
    allow_credentials=True,# Allow cookies or authentication headers
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all request headers (e.g., Authorization, Content-Type)
)


# Load predicted ratings and matrix
predicted_ratings = joblib.load("model_components/predicted_ratings.pkl")
ratings_matrix = joblib.load("model_components/ratings_matrix.pkl")
df = joblib.load("model_components/original_df.pkl")

# Most popular fallback
most_popular = df.groupby('prod_id').agg({'rating': 'count'}) \
                 .sort_values('rating', ascending=False)


class RecommendRequest(BaseModel):
    user_id: str
    num_recommendations: int = 5


def recommend_items(user_id, num_recommendations=5):
    if user_id not in ratings_matrix.index:
         # If user is not in the matrix → return most popular products
        popular_products = most_popular.head(num_recommendations)
        return list(popular_products.index)

    user_index = ratings_matrix.index.get_loc(user_id)
    actual_ratings = ratings_matrix.iloc[user_index].values

    if hasattr(predicted_ratings, 'toarray'):
        predicted_user_ratings = predicted_ratings[user_index].toarray().flatten()
    else:
        predicted_user_ratings = predicted_ratings.iloc[user_index].values

    recommendations_df = pd.DataFrame({
        "actual": actual_ratings,
        "predicted": predicted_user_ratings
    }, index=ratings_matrix.columns)

    unseen_items = recommendations_df[recommendations_df.actual == 0]
    top_recommendations = unseen_items.sort_values(by="predicted", ascending=False).head(num_recommendations)

    return list(top_recommendations.index)


@app.post("/recommend")
def get_recommendations(request: RecommendRequest):
    try:
        recommendations = recommend_items(request.user_id, request.num_recommendations)
        return {"user_id": request.user_id, "recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Error: {str(e)}")
