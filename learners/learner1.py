from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

driver = GraphDatabase.driver(
  os.getenv("NEO4J_URI"),       # (1)
  auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD")) # (2)
)

#driver.verify_connectivity()

test = driver.execute_query(
    "RETURN COUNT {()} AS count"
)

first = test[0]
print(first[0][0])  # (3)

driver.close()