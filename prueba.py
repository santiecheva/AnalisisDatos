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



    con.commit()

    print('de la tabla train se tienen nulos: \n %s' % df_train.isnull().sum())   
    print('de la tabla test se tienen nulos: \n %s' % df_test.isnull().sum())   

    print('de la tabla train se tiene el porcentaje de nulos: \n ' , df_train.isnull().sum()/len(df_train)*100)   
    print('de la tabla test se tiene el porcentaje de nulos: \n ' , df_test.isnull().sum()/len(df_test)*100)  

con = sql_connection()

sql_table(con)





