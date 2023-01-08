import sqlite3
from sqlite3 import Error

    
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
   # finally:
      #  if conn:
      #      conn.close()
    return conn


                
def create_table(db_file):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    conn = create_connection(db_file)
    print(conn)
    create_table_sql= f"""CREATE TABLE IF NOT EXISTS Concrete (
                cement REAL,
                blast_furnace_slag REAL,
                fly_ash REAL,
                water REAL,
                superplasticizer REAL,
                coarse_aggregate REAL,
                fine_aggregate REAL,
                age INTEGER,
                concrete_compressive_strength REAL
                );"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)



if __name__ == '__main__':
    db_file = 'Concrete_strength.db'

    create_table(db_file)
    