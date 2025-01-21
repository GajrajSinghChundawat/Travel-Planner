from os import getenv
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
MYSQL_DB = getenv("MYSQL_DB")
MYSQL_DB_HOST = getenv("MYSQL_DB_HOST")
MYSQL_DB_USER = getenv("MYSQL_DB_USER")
MYSQL_DB_PASS = getenv("MYSQL_DB_PASS")

travel_planner = mysql.connector.connect(
  host=MYSQL_DB_HOST,
  user=MYSQL_DB_USER,
  password=MYSQL_DB_PASS,
  database=MYSQL_DB
)
