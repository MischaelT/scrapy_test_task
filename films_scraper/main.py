import pandas as pd
from films_scraper.logger import logger

df = pd.read_csv('items.csv')

logger.info(df)