import mysql_check
import pandas as pd


def question_3_example_get_customers(country):
    """
    This is an example of what your answers should look like.
    :param country:
    :return:
    """

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    # You will provide your SQL queries in this format. %s is a parameter.
    q = """
        select customerNumber, customerName, country
            from classicmodels.customers
            where
            country = %s
    """

    # Connect and run the query
    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q, [country])
    result = cur.fetchall()

    # Convert to a Data Frame and return
    result = pd.DataFrame(result)

    return result


def question_3_revenue_by_country():

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    # You will provide your SQL queries in this format.
    q = """
        SELECT country, SUM(priceEach * quantityOrdered) AS revenue 
        FROM classicmodels.orders NATURAL JOIN classicmodels.orderdetails
        NATURAL JOIN classicmodels.products NATURAL JOIN classicmodels.customers
        WHERE status = 'Shipped'
        GROUP BY country;
        """

    # Connect and run the query
    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)
    result = cur.fetchall()

    # Convert to a Data Frame and return
    result = pd.DataFrame(result)

    return result



def question_3_purchases_and_payments():

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    # You will provide your SQL queries in this format. %s is a parameter.
    q = """
    SELECT customerName, customerNumber, total_payments, spent_amount, (spent_amount - total_payments) AS unpaid_amount
    FROM classicmodels.customers NATURAL JOIN
    (
        SELECT payments_data.customerNumber, SUM(amount) AS total_payments, orders_data.spent_amount
        FROM classicmodels.payments AS payments_data
        NATURAL JOIN
        (
            SELECT customerNumber, SUM(quantityOrdered * priceEach) AS spent_amount
            FROM classicmodels.orders NATURAL JOIN classicmodels.orderdetails
            GROUP BY customerNumber
        ) AS orders_data
        GROUP BY customerNumber
    ) AS amounts_per_customer
    ORDER BY customerName
    """

    # Connect and run the query
    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)
    result = cur.fetchall()

    # Convert to a Data Frame and return
    result = pd.DataFrame(result)

    return result


def question_3_customers_and_lines():

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    # You will provide your SQL queries in this format.
    q = """
        SELECT DISTINCT all_customers.customerNumber, all_customers.customerName
        FROM classicmodels.customers AS all_customers
        LEFT JOIN
        (
            SELECT DISTINCT customerNumber
            FROM classicmodels.products NATURAL JOIN classicmodels.orders NATURAL JOIN classicmodels.customers
            WHERE productLine = 'Planes' OR productLine = 'Trucks and Buses'
        ) AS filtered_customers
        ON all_customers.customerNumber = filtered_customers.customerNumber
        WHERE filtered_customers.customerNumber is NULL;
        """

    # Connect and run the query
    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)
    result = cur.fetchall()

    # Convert to a Data Frame and return
    result = pd.DataFrame(result)

    return result


