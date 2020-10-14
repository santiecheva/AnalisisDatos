import sqlite3
import pandas as pd

from sqlite3 import Error
def sql_connection():

    try:

        con = sqlite3.connect('/home/santiago/trabajo/tech_db.sqlite')

        return con

    except Error:

        print(Error)


def sql_table(con):

    cursorObj = con.cursor()

    df_train =  pd.read_sql_query("SELECT * from train", con)
    df_test =  pd.read_sql_query("SELECT * from test", con)
    #df_ix_train_index =  pd.read_sql_query("SELECT * from ix_train_index", con)
    #df_ix_test_index =  pd.read_sql_query("SELECT * from ix_test_index", con)


    con.commit()

    print(df_train)

con = sql_connection()

sql_table(con)





