# Import libraries
import pandas as pd
import psycopg2
import seaborn as sns
import matplotlib.pyplot as plt

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    dbname="play",
    user="postgres",
    password="KEVINsan0.",
    port="5432"
)


# Query to get the rating and price data
query = """
SELECT 
    CAST(REPLACE("Price"::TEXT, '$', '') AS FLOAT) AS price, 
    "Rating"
FROM googleplaystore
WHERE "Price" IS NOT NULL 
    AND "Rating" IS NOT NULL
    AND REPLACE("Price"::TEXT, '$', '') ~ '^[0-9.]+$';

"""

df = pd.read_sql(query, conn)
conn.close()

# Visualization
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x="price", y="Rating", color="purple")
plt.title("Apps by Rating and Price")
plt.xlabel("Price")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()
