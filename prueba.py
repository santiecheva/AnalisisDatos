import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sqlite3 import Error
from sklearn.datasets import *


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

    print('de la tabla train: \n %s' % df_train.isnull().sum())   
    print('de la tabla train: \n %s' % df_train.isnull().sum())   



con = sql_connection()

sql_table(con)





