from dotenv import load_dotenv
import os

load_dotenv()

print("HOST:", os.getenv("DATABRICKS_SERVER_HOSTNAME"))
print("PATH:", os.getenv("DATABRICKS_HTTP_PATH"))
print("TOKEN:", os.getenv("DATABRICKS_TOKEN"))