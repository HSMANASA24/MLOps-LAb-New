import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Loading clean ratings...")
df = pd.read_csv("data/processed/cleaned_ratings.csv")

matrix = df.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)

logger.info(f"Ratings matrix shape: {matrix.shape}")

similarity = matrix.dot(matrix.T)

logger.info(f"Created {similarity.shape} similarity matrix")

similarity.to_pickle("models/user_similarity.pkl")

logger.info("Saved to models/user_similarity.pkl")