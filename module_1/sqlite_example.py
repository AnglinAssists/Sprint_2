# Step 0 - import sqlite3
import sqlite3
import queries as q
import pandas as pd

# DB connect function
def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)


def execute_q(conn, query):
    # Make the "cursor"
    curs = conn.cursor()
    # Execute the query
    curs.execute(query)
    # Pull(and return) the results
    return curs.fetchall()


if __name__ == "__main__":
    conn = connect_to_db()
    # print(execute_q(conn, q.SELECT_ALL)[:5])
    results = execute_q(conn, q.AVG_ITEM_WEIGHT_PER_CHARACTER)
    df = pd.DataFrame(results)
    df.columns = ['name','average_item_weight']
    df.to_csv('rpg_db.csv', index=False)
    # print(df.head())

# Step 1 - connect to the database
# triple-check the spelling of your database filename
# connection = sqlite3.connect('rpg_db.sqlite3')
# Step 2 - Make the "cursor"
# cursor = connection.cursor()
#  Step 3 - Write a query
# (See the queries.py file)
# Step 4 - execute the query on the cursor and fetch the results
# #pulling the results from the cursor
# results = cursor.execute(q.SELECT_ALL).fetchall()
