import CSVTable
import CSVCatalog
import json
import csv
import time

# Chandan Suri
# CS4090

#Must clear out all tables in CSV Catalog schema before using if there are any present
#Please change the path name to be whatever the path to the CSV files are
#First methods set up metadata!! Very important that all of these be run properly

# Only need to run these if you made the tables already in your CSV Catalog tests
# You will not need to include the output in your submission as executing this is not required
# Implementation is provided
def drop_tables_for_prep():
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    cat.drop_table("people")
    cat.drop_table("batting")
    cat.drop_table("appearances")

    print('-----------------------------------------------------------------------------------')

#drop_tables_for_prep()

# Implementation is provided
# You will need to update these with the correct path
def create_lahman_tables():
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    cat.create_table("people", "People.csv")
    cat.create_table("batting","Batting.csv")
    cat.create_table("appearances", "Appearances.csv")

    print('-----------------------------------------------------------------------------------')

#create_lahman_tables()

# Note: You can default all column types to text
def update_people_columns():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    table_name = 'people'
    file_name = 'People.csv'
    table = cat.get_table(table_name)
    primary_key_columns = ['playerID']

    with open(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        column_names = reader.fieldnames

    for column_name in column_names:
        if column_name not in primary_key_columns:
            col_def = CSVCatalog.ColumnDefinition(column_name)
        else:
            col_def = CSVCatalog.ColumnDefinition(column_name, not_null=True)
        table.add_column_definition(col_def)
        print(f"For table {table_name}, Column Definition Added:\n {col_def}")

    print('-----------------------------------------------------------------------------------')


#update_people_columns()

def update_appearances_columns():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    table_name = 'appearances'
    file_name = 'Appearances.csv'
    table = cat.get_table(table_name)
    primary_key_columns = ['playerID', 'yearID', 'teamID']

    with open(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        column_names = reader.fieldnames

    for column_name in column_names:
        if column_name not in primary_key_columns:
            col_def = CSVCatalog.ColumnDefinition(column_name)
        else:
            col_def = CSVCatalog.ColumnDefinition(column_name, not_null=True)
        table.add_column_definition(col_def)
        print(f"For table {table_name}, Column Definition Added:\n {col_def}")

    print('-----------------------------------------------------------------------------------')


#update_appearances_columns()

def update_batting_columns():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    table_name = 'batting'
    file_name = 'Batting.csv'
    table = cat.get_table(table_name)
    primary_key_columns = ['playerID', 'yearID', 'stint']

    with open(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        column_names = reader.fieldnames

    for column_name in column_names:
        if column_name not in primary_key_columns:
            col_def = CSVCatalog.ColumnDefinition(column_name)
        else:
            col_def = CSVCatalog.ColumnDefinition(column_name, not_null=True)
        table.add_column_definition(col_def)
        print(f"For table {table_name}, Column Definition Added:\n {col_def}")

    print('-----------------------------------------------------------------------------------')


#update_batting_columns()

#Add primary key indexes for people, batting, and appearances in this test
def add_index_definitions():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    table_names = ['people', 'batting', 'appearances']
    table_pks_map = {
        table_names[0]: ['playerID'],
        table_names[1]: ['playerID', 'yearID', 'stint'],
        table_names[2]: ['playerID', 'yearID', 'teamID']
    }
    pk_index_names = ['PK People', 'PK Batting', 'PK Appearances']

    for i, table_name in enumerate(table_names):
        table = cat.get_table(table_name)
        pk_cols = table_pks_map[table_name]
        pk_index_name = pk_index_names[i]

        table.define_index(pk_index_name, pk_cols, "PRIMARY")
        pk_idx = table.get_index(pk_index_name)
        print(f'For Table {table_name}, Index Definition Added:\n {pk_idx}')

    print('-----------------------------------------------------------------------------------')

#add_index_definitions()


def test_load_info():
    table = CSVTable.CSVTable("people")
    print(table.__description__.file_name)
    print('-----------------------------------------------------------------------------------')

#test_load_info()

def test_get_col_names():
    table = CSVTable.CSVTable("people")
    names = table.__get_column_names__()
    print(names)
    print('-----------------------------------------------------------------------------------')

#test_get_col_names()

def add_other_indexes():
    """
    We want to add indexes for common user stories
    People: nameLast, nameFirst
    Batting: teamID
    Appearances: None that are too important right now
    :return:
    """
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    table_names = ['people', 'batting']
    table_indexes_map = {
        table_names[0]: ['nameLast', 'nameFirst'],
        table_names[1]: ['teamID']
    }
    index_names = ['last_first', 'TeamID']

    for i, table_name in enumerate(table_names):
        table = cat.get_table(table_name)
        cols = table_indexes_map[table_name]
        index_name = index_names[i]

        table.define_index(index_name, cols, "INDEX")
        idx = table.get_index(index_name)
        print(f'For Table {table_name}, Index Definition Added:\n {idx}')

    print('-----------------------------------------------------------------------------------')


#add_other_indexes()

def load_test():
    batting_table = CSVTable.CSVTable("batting")
    print(batting_table)
    print('-----------------------------------------------------------------------------------')

#load_test()


def dumb_join_test():
    start = time.time()
    batting_table = CSVTable.CSVTable("batting")
    appearances_table = CSVTable.CSVTable("appearances")
    result = batting_table.dumb_join(appearances_table, ["playerID", "yearID"],
                                     {"playerID": "baxtemi01", "teamID": "NYN"},
                                     ["playerID", "yearID", "teamID", "AB", "H", "G_all", "G_batting"])
    end = time.time()
    print(result)
    print(f"Time in searching and retrieval: {end - start}")

    print('-----------------------------------------------------------------------------------')

    start = time.time()
    people_table = CSVTable.CSVTable("people")
    appearances_table = CSVTable.CSVTable("appearances")
    result = people_table.dumb_join(appearances_table, ["playerID"], {"playerID": "baxtemi01"},
                                     ["playerID", "yearID", "teamID", "nameLast", "nameFirst", "height",
                                      "weight", "G_all", "G_batting"])
    end = time.time()
    print(result)
    print(f"Time in searching and retrieval: {end - start}")

    print('-----------------------------------------------------------------------------------')

    start = time.time()
    people_table = CSVTable.CSVTable("people")
    appearances_table = CSVTable.CSVTable("batting")
    result = people_table.dumb_join(appearances_table, ["playerID"],
                                         {"nameLast": "Baxter", "nameFirst": "Mike", "teamID": "NYN"},
                                         ["playerID", "yearID", "teamID", "nameLast", "nameFirst", "height",
                                          "weight", "R", "AB"])
    end = time.time()
    print(result)
    print(f"Time in searching and retrieval: {end - start}")

    print('-----------------------------------------------------------------------------------')

#dumb_join_test()


def get_access_path_test():
    # Test Case-1
    batting_table = CSVTable.CSVTable("batting")
    template = {"teamID": "NYN", "playerID": "baxtemi01", "yearID": "2012"}
    print(f"Test Case -1: Batting Table: Template: {template}")
    index_result, count = batting_table.__get_access_path__(template)
    print(f"Index: {index_result}")
    print(f"Count: {count}")
    print('-----------------------------------------------------------------------------------')

    # Test Case-2
    batting_table = CSVTable.CSVTable("batting")
    template = {"teamID": "NYN", "playerID": "baxtemi01", "yearID": "2012", "stint": "1"}
    print(f"Test Case -2: Batting Table: Template: {template}")
    index_result, count = batting_table.__get_access_path__(template)
    print(f"Index: {index_result}")
    print(f"Count: {count}")
    print('-----------------------------------------------------------------------------------')

    # Test Case-3
    appearances_table = CSVTable.CSVTable("appearances")
    template = {"teamID": "NYN", "playerID": "baxtemi01", "yearID": "2012", "lgID": "NA"}
    print(f"Test Case -3: Appearances Table: Template: {template}")
    index_result, count = appearances_table.__get_access_path__(template)
    print(f"Index: {index_result}")
    print(f"Count: {count}")
    print('-----------------------------------------------------------------------------------')

    # Test Case-4
    appearances_table = CSVTable.CSVTable("appearances")
    template = {"teamID": "NYN", "playerID": "baxtemi01", "lgID": "NA"}
    print(f"Test Case -4: (No Best Index will be Found!) Appearances Table: Template: {template}")
    index_result, count = appearances_table.__get_access_path__(template)
    print(f"Index: {index_result}")
    print(f"Count: {count}")
    print('-----------------------------------------------------------------------------------')

#get_access_path_test()

def sub_where_template_test():
    # ************************ TO DO ***************************
    table_name = "batting"
    batting_table = CSVTable.CSVTable(table_name)
    where_template = {"playerID": "baxtemi01",
                      "teamID": "NYN",
                      "yearID": "2012",
                      "G": "89",
                      "AB": "179",
                      "R": "26",
                      "ABC": "12345"}
    print(f"Test for Table {table_name} and template: {where_template}")
    sub_template = batting_table.__get_sub_where_template__(where_template)
    print(f"Sub Template: {sub_template}")
    print('-----------------------------------------------------------------------------------')

    table_name = "people"
    people_table = CSVTable.CSVTable(table_name)
    where_template = {"playerID": "aguilje01",
                      "nameFirst": "Chris",
                      "nameLast": "Aguila",
                      "throws": "R",
                      "random_col_1": "1234",
                      "random_col_2": "5678",
                      "weight": "200"}
    print(f"Test for Table {table_name} and template: {where_template}")
    sub_template = people_table.__get_sub_where_template__(where_template)
    print(f"Sub Template: {sub_template}")
    print('-----------------------------------------------------------------------------------')

    table_name = "appearances"
    appearances_table = CSVTable.CSVTable(table_name)
    where_template = {"playerID": "addybo01",
                      "teamID": "RC1",
                      "yearID": "1871",
                      "lgID": "NA",
                      "random_col_1": "1234",
                      "random_col_2": "5678",
                      "GS": "25"}
    print(f"Test for Table {table_name} and template: {where_template}")
    sub_template = appearances_table.__get_sub_where_template__(where_template)
    print(f"Sub Template: {sub_template}")
    print('-----------------------------------------------------------------------------------')

#sub_where_template_test()


def test_find_by_template_index():
    # ************************ TO DO ***************************
    table_name = "batting"
    batting_table = CSVTable.CSVTable(table_name)
    idx_name = 'PK Batting'
    where_template = {"playerID": "baxtemi01",
                      "stint": "1",
                      "yearID": "2012",
                      "lgID": "NL",
                      "AB": "179"
                      }
    fields = ["playerID", "yearID", "stint", "lgID", "AB", "G", "R", "H", "2B", "3B"]
    print(f"Test for Table {table_name}, template: {where_template} "
          f"with index {idx_name} and projection fields {fields}")
    matching_rows = batting_table.__find_by_template_index__(where_template, idx_name, fields)
    print(f"Matching Rows: \n{matching_rows}")
    print('-----------------------------------------------------------------------------------')

    idx_name = 'TeamID'
    where_template = {"teamID": "RC1",
                      "G": "25"
                      }
    fields = ["playerID", "yearID", "stint", "lgID", "AB", "G", "R", "H", "2B", "3B"]
    print(f"Test for Table {table_name}, template: {where_template} "
          f"with index {idx_name} and projection fields {fields}")
    matching_rows = batting_table.__find_by_template_index__(where_template, idx_name, fields)
    print(f"Matching Rows: \n{matching_rows}")
    print('-----------------------------------------------------------------------------------')

    idx_name = 'PK Batting'
    where_template = {"teamID": "RC1",
                      "G": "25",
                      "stint": "1"
                      }
    fields = ["playerID", "yearID", "stint", "lgID", "AB", "G", "R", "H", "2B", "3B"]
    print(f"When No Indexing Happens: Test for Table {table_name}, template: {where_template} "
          f"with index {idx_name} and projection fields {fields}")
    matching_rows = batting_table.__find_by_template_index__(where_template, idx_name, fields)
    print(f"Matching Rows: \n{matching_rows}")
    print('-----------------------------------------------------------------------------------')

#test_find_by_template_index()

def smart_join_test():
    # ************************ TO DO ***************************
    start = time.time()
    batting_table = CSVTable.CSVTable("batting")
    appearances_table = CSVTable.CSVTable("appearances")
    result = batting_table.__smart_join__(appearances_table, ["playerID", "yearID"],
                                     {"playerID": "baxtemi01", "teamID": "NYN"},
                                     ["playerID", "yearID", "teamID", "AB", "H", "G_all", "G_batting"])
    end = time.time()
    print(result)
    print(f"Time in searching and retrieval: {end - start}")
    print('-----------------------------------------------------------------------------------')

    start = time.time()
    people_table = CSVTable.CSVTable("people")
    appearances_table = CSVTable.CSVTable("appearances")
    result = people_table.__smart_join__(appearances_table, ["playerID"], {"playerID": "baxtemi01"},
                                    ["playerID", "yearID", "teamID", "nameLast", "nameFirst", "height",
                                     "weight", "G_all", "G_batting"])
    end = time.time()
    print(result)
    print(f"Time in searching and retrieval: {end - start}")
    print('-----------------------------------------------------------------------------------')

    start = time.time()
    people_table = CSVTable.CSVTable("people")
    appearances_table = CSVTable.CSVTable("batting")
    result = people_table.__smart_join__(appearances_table, ["playerID"],
                                         {"nameLast": "Baxter", "nameFirst": "Mike", "teamID": "NYN"},
                                         ["playerID", "yearID", "teamID", "nameLast", "nameFirst", "height",
                                          "weight", "R", "AB"])
    end = time.time()
    print(result)
    print(f"Time in searching and retrieval: {end - start}")
    print('-----------------------------------------------------------------------------------')

#smart_join_test()
