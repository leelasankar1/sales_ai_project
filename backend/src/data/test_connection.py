import os
from dotenv import load_dotenv
from databricks import sql

load_dotenv()

host = os.getenv("DATABRICKS_SERVER_HOSTNAME")
path = os.getenv("DATABRICKS_HTTP_PATH")
token = os.getenv("DATABRICKS_TOKEN")

print("host :", repr(host))
print("path :", repr(path))
print("token:", (token[:4] + "..." + str(len(token)) + " chars") if token else None)

with sql.connect(server_hostname=host, http_path=path, access_token=token) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT 1")
        print("OK:", cur.fetchone())