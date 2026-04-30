import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Loading raw ratings...")
df = pd.read_csv("data/raw/ratings.csv")

logger.info(f"Loaded {len(df)} ratings")

df = df.drop_duplicates()
logger.info("Removed duplicate ratings")

df.to_csv("data/processed/cleaned_ratings.csv", index=False)

logger.info(f"Saved {len(df)} clean ratings")
logger.info(f"Users: {df['user_id'].nunique()}")
logger.info(f"Movies: {df['movie_id'].nunique()}")