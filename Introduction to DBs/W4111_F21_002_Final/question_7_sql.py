import mysql_check
import pandas as pd

def schema_operation_1():
    """
    Create star schema
    """
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    CREATE SCHEMA IF NOT EXISTS classicmodels_star;
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res


def schema_operation_2():
    """
    Use star schema.
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    USE classicmodels_star;
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def schema_operation_3():
    """
    Create Date Dimension Table.
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    CREATE TABLE date_dimension
    (
        orderDate DATETIME,
        quarter INT,
        month INT,
        year INT,
        PRIMARY KEY (orderDate)
    );
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def schema_operation_4():
    """
    Create Location Dimension Table.
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    CREATE TABLE location_dimension 
    (
        customerNumber INT,
        city VARCHAR(255),
        country VARCHAR (255),
        region ENUM ('EMEA', 'NA', 'AP'),
        PRIMARY KEY (customerNumber)
    );
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def schema_operation_5():
    """
    Create Product Type Dimension Table.
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    CREATE TABLE product_type_dimension 
    (
        productCode varchar (255),
        scale varchar(255),
        productLine varchar (255),
        PRIMARY KEY (productCode)
    );
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def schema_operation_6():
    """
    Use star schema.
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    CREATE TABLE fact 
    (
        customerNumber INT,
        productCode VARCHAR (255),
        orderDate DATETIME,
        quantityOrdered INT,
        priceEach INT,
        PRIMARY KEY (customerNumber, productCode, orderDate),
        CONSTRAINT FK_Date_Dim_Order_Date FOREIGN KEY (orderDate) REFERENCES date_dimension (OrderDate),
        CONSTRAINT FK_Loc_Dim_Cus_Num FOREIGN KEY (customerNumber) REFERENCES location_dimension (customerNumber),
        CONSTRAINT FK_Prod_Type_Dim_Prod_Code FOREIGN KEY (productCode) REFERENCES product_type_dimension (productCode)
    );
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res


def data_transformation_1():
    """
    Insert data in Date Dimension Table.
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    INSERT INTO classicmodels_star.date_dimension
    SELECT DISTINCT orderDate, QUARTER(orderDate), MONTH(orderDate), YEAR(orderDate)
    FROM classicmodels.orderdetails NATURAL JOIN classicmodels.orders;
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res


def data_transformation_2():
    """
    Insert data in Location Dimension Table.
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    INSERT INTO classicmodels_star.location_dimension
    SELECT DISTINCT classicmodels.customers.customerNumber, classicmodels.customers.city, classicmodels.customers.country,
    CASE
        WHEN classicmodels.customers.country IN ('USA', 'Canada') THEN 'NA'
        WHEN classicmodels.customers.country IN ('Philipines', 'Hong Kong', 'Singapore', 'Japan', 'Australia', 'New Zealand')
        THEN 'AP'
        ELSE 'EMEA'
    END
    FROM classicmodels.customers;
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def data_transformation_3():
    """
    Insert data in Product Type Dimension Table.
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    INSERT INTO classicmodels_star.product_type_dimension
    SELECT DISTINCT productCode, productscale, productLine
    FROM classicmodels.products;
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def data_transformation_4():
    """
    Insert data in Fact Table.
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    INSERT INTO classicmodels_star.fact
    SELECT customerNumber, productCode, orderDate, quantityOrdered, priceEach
    FROM classicmodels.orderdetails NATURAL JOIN classicmodels.orders;
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def sales_by_year_region():

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    SELECT region, year, SUM(classicmodels_star.fact.priceEach * classicmodels_star.fact.quantityOrdered) AS sales
    FROM classicmodels_star.date_dimension NATURAL JOIN classicmodels_star.fact
    NATURAL JOIN classicmodels_star.location_dimension
    GROUP BY region, year;
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    cur.execute(q)
    res = pd.DataFrame(cur.fetchall())
    
    return res


def sales_by_quarter_year_county_region():
    
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    SELECT quarter, year, country, region, SUM(classicmodels_star.fact.PriceEach * classicmodels_star.fact.QuantityOrdered)
    AS sales
    FROM classicmodels_star.date_dimension NATURAL JOIN classicmodels_star.fact
    NATURAL JOIN classicmodels_star.location_dimension
    GROUP BY quarter, year, country, region;
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    cur.execute(q)
    res = pd.DataFrame(cur.fetchall())
    
    return res


def sales_by_product_line_scale_year():
    
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    SELECT productLine, scale, year, SUM(classicmodels_star.fact.PriceEach * classicmodels_star.fact.QuantityOrdered)
    AS sales
    FROM classicmodels_star.date_dimension NATURAL JOIN classicmodels_star.fact
    NATURAL JOIN classicmodels_star.product_type_dimension
    GROUP BY productLine, scale, year;
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    cur.execute(q)
    res = pd.DataFrame(cur.fetchall())
    
    return res