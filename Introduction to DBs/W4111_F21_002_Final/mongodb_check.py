import pymongo
import pandas as pd
import csv


_connect_url = None
_mongo_client = None


def set_connect_url(url):

    global _connect_url

    _connect_url = url


def get_mongo_client():

    global _mongo_client

    if _mongo_client is None:
        _mongo_client = pymongo.MongoClient(_connect_url)

    return _mongo_client


def load_and_test_mongo():

    customer_csv = []

    with open("./classicmodels_customers.csv", "r") as in_file:

        c_rdr = csv.DictReader(in_file)

        for c in c_rdr:
            customer_csv.append(c)

    mongo_c = get_mongo_client()

    mongo_c.classicmodels.customers.drop()

    for c in customer_csv:
        mongo_c.classicmodels.customers.insert_one(c)

    res = mongo_c.classicmodels.customers.find(
        {"country": "France"},
        {
            "customerNumber": 1,
            "customerName": 1,
            "country": 1
        }
    )

    the_df = pd.DataFrame(list(res))
    return the_df


if __name__ == "__main__":

    set_connect_url("mongodb://localhost:27017/")
    load_and_test_mongo()

    df = load_and_test_mongo()
    print("Test result = \n", df)


