import mysql_check
import pandas as pd

def schema_operation_1():
    """
    Creating the database schema RACI
    """
    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    CREATE SCHEMA IF NOT EXISTS RACI;
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res


def schema_operation_2():
    """
    Using the database schema RACI
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    USE RACI;
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def schema_operation_3():
    """
    Creating the Person table...
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    CREATE TABLE Person
    (
        UNI VARCHAR(10) NOT NULL PRIMARY KEY,
        last_name VARCHAR (255),
        first_name VARCHAR (255),
        email VARCHAR(255)
    );
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def schema_operation_4():
    """
    Creating the Project table...
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    CREATE TABLE Project
    (
        project_id   VARCHAR(255) NOT NULL PRIMARY KEY,
        project_name VARCHAR(255),
        start_date   DATETIME,
        end_date     DATETIME
    );
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def schema_operation_5():
    """
    Creating the ProjectPerson table...
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    CREATE TABLE ProjectPerson
    (
        UNI        VARCHAR(10) NOT NULL,
        project_id VARCHAR(255) NOT NULL,
        role       ENUM ('Responsible', 'Accountable', 'Consulted', 'Informed'),
        PRIMARY KEY (UNI, project_id),
        CONSTRAINT FK_Person_UNI FOREIGN KEY (UNI) REFERENCES Person(UNI),
        CONSTRAINT FK_Project_ID FOREIGN KEY (project_id) REFERENCES Project(project_id)
    );
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def schema_operation_6():
    """
    Creating the Trigger for "Before Insertion" to take care of the "Accountable" role.
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    CREATE TRIGGER ACCOUNTABLE_ROLE_INSERT BEFORE INSERT ON ProjectPerson
    FOR EACH ROW BEGIN
        DECLARE count_accountable_roles INT;
        IF new.role = 'Accountable' THEN
            SET count_accountable_roles = (SELECT COUNT(*) FROM ProjectPerson
                WHERE ProjectPerson.role = 'Accountable' AND ProjectPerson.project_id = new.project_id);

            IF count_accountable_roles > 0 THEN
                SIGNAL SQLSTATE '99999'
                    SET message_text ='ERROR: CANNOT INSERT FOR ROLE ACCOUNTABLE if it is already PRESENT in a project';
            END IF;
        END IF;
    END;
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res

def schema_operation_7():
    """
    Creating the Trigger for "Before Updation" to take care of the "Accountable" role.
    """

    res = None

    # You may need to set the connection info. I do just to be safe.
    mysql_check.set_connect_info("root", "dbuserdbuser", "localhost")

    q = """
    CREATE TRIGGER ACCOUNTABLE_ROLE_UPDATE BEFORE UPDATE ON ProjectPerson
    FOR EACH ROW BEGIN
        DECLARE count_accountable_roles INT;
        IF new.role = 'Accountable' THEN
            SET count_accountable_roles = (SELECT COUNT(*) FROM ProjectPerson
                WHERE ProjectPerson.role = 'Accountable' AND ProjectPerson.project_id = new.project_id);

            IF count_accountable_roles > 0 THEN
                SIGNAL SQLSTATE '99999'
                    SET message_text ='ERROR: CANNOT UPDATE TO ROLE ACCOUNTABLE if it is already PRESENT in a project';
            END IF;
        END IF;
    END;
    """

    conn = mysql_check.get_connection()
    cur = conn.cursor()
    res = cur.execute(q)

    return res