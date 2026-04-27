import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

# establishing connection with snowflake :
def get_connection():
    return snowflake.connector.connect(
        user = os.getenv("SNOWFLAKE_USER"),
        password = os.getenv("SNOWFLAKE_PASSWORD"),
        account = os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse = os.getenv("SNOWFLAKE_WAREHOUSE"),
        database = os.getenv("SNOWFLAKE_DATABASE"),
        schema = os.getenv("SNOWFLAKE_SCHEMA"),
        role = os.getenv("SNOWFLAKE_ROLE")
    )

# fetching data from snowflake :
def fetch_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("USE WAREHOUSE demo_wh")
    cursor.execute("USE DATABASE db")
    cursor.execute("USE SCHEMA my_schema")

    cursor.execute("SELECT * FROM worker")
    
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

