import pymysql
from sqlalchemy import create_engine
import json
import pandas as pd

_my_sql_connection = None
_my_sql_engine = None

_db_connect_info = {
    "user": None,
    "password": None,
    "host": None,
    "autocommit": True,
    "port": 3306,
    "cursorclass": pymysql.cursors.DictCursor
}


def set_connect_info(db_user, db_password, db_host):
    _db_connect_info["user"] = db_user
    _db_connect_info["password"] = db_password
    _db_connect_info["host"] = db_host


def get_connection():

    global _my_sql_connection

    if _my_sql_connection is None:
        _my_sql_connection = pymysql.connect(**_db_connect_info)

    return _my_sql_connection


def get_engine():

    global _my_sql_engine

    if _my_sql_engine is None:
        url = "mysql+pymysql://{user}:{password}@{host}/"
        url = url.format(user=_db_connect_info["user"],
                         password=_db_connect_info["password"],
                         host=_db_connect_info["host"])
        _my_sql_engine = create_engine(url)

    return _my_sql_engine


def test_pymysql():

    con = get_connection()
    cursor = con.cursor()

    q = "show tables from classicmodels"
    res = cursor.execute(q)
    res_data = cursor.fetchall()

    df = pd.DataFrame(res_data)
    return df


def test_sql_alchemy():

    engine = get_engine()

    q = """
        select customerNumber, customerName, country from classicmodels.customers
            where country='France'
        """

    result = pd.read_sql(q, con=engine)
    return result









