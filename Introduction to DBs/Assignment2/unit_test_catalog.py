import CSVCatalog
import json

# Chandan Suri
# CS4090

# Example test, you will have to update the connection info
# Implementation Provided
def create_table_test():
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    test_tables_dict = {"test_table_1":"test_path_file_1.csv",
                        "test_table_2":"test_path_file_2.csv",
                        "test_table_3":"test_path_file_3.csv",
                        "test_table_4":"test_path_file_4.csv",
                        "test_table_5":"test_path_file_5.csv"
                        }

    for test_table_name, test_file_name in test_tables_dict.items():
        print(f"Adding {test_table_name} with file name {test_file_name}...")
        cat.create_table(test_table_name, test_file_name)
        table_entry = cat.get_table(test_table_name)
        print("Table = ", table_entry)

    print('-----------------------------------------------------------------------------------')

#create_table_test()

def drop_table_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    table_names_to_drop = ["test_table_4", "test_table_5"]

    for table_name_to_drop in table_names_to_drop:
        print(f"Dropping {table_name_to_drop} ...")
        cat.drop_table(table_name_to_drop)

    print('-----------------------------------------------------------------------------------')

#drop_table_test()

def add_column_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    table_names = ["test_table_1", "test_table_2", "test_table_3"]
    table_columns_map = {
        table_names[0]: [("t1_tc_1", "text", True), ("t1_tc_2", "text", False), ("t1_tc_3", "number", False)],
        table_names[1]: [("t2_tc_1", "text", True), ("t2_tc_2", "text", False), ("t2_tc_3", "number", True)],
        table_names[2]: [("t3_tc_1", "number", True), ("t3_tc_2", "text", True), ("t3_tc_3", "text", False)]
    }

    for table_name in table_names:
        table = cat.get_table(table_name)
        for cols_data in table_columns_map[table_name]:
            col = CSVCatalog.ColumnDefinition(cols_data[0], cols_data[1], cols_data[2])
            table.add_column_definition(col)
            print(f'For table {table}, Column Definition Added:\n {col.__str__()}')

    print('-----------------------------------------------------------------------------------')

#add_column_test()

# Implementation Provided
# Fails because no name is given
def column_name_failure_test():
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    col = CSVCatalog.ColumnDefinition(None, "text", False)
    t = cat.get_table("test_table")
    t.add_column_definition(col)

    print('-----------------------------------------------------------------------------------')

#column_name_failure_test()

# Implementation Provided
# Fails because "canary" is not a permitted type
def column_type_failure_test():
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    col = CSVCatalog.ColumnDefinition("bird", "canary", False)
    t = cat.get_table("test_table")
    t.add_column_definition(col)

    print('-----------------------------------------------------------------------------------')

#column_type_failure_test()

# Implementation Provided
# Will fail because "happy" is not a boolean
def column_not_null_failure_test():
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    col = CSVCatalog.ColumnDefinition("name", "text", "happy")
    t = cat.get_table("test_table")
    t.add_column_definition(col)

    print('-----------------------------------------------------------------------------------')

#column_not_null_failure_test()


def add_index_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    table_names = ["test_table_1", "test_table_2", "test_table_3"]
    table_columns_map = {
        table_names[0]: ["t1_tc_1", "t1_tc_2", "t1_tc_3"],
        table_names[1]: ["t2_tc_1", "t2_tc_2", "t2_tc_3"],
        table_names[2]: ["t3_tc_1", "t3_tc_2", "t3_tc_3"]
    }
    table_indexes_map = {
        table_names[0]: ["t1_PK_index"],
        table_names[1]: ["t2_PK_index", "t2_index", "t2_unique_index"],
        table_names[2]: ["t3_PK_index", "t3_index"]
    }

    for i, table_name in enumerate(table_names):
        table = cat.get_table(table_name)
        columns = table_columns_map[table_name]

        if i == 0:
            # For the First Table, I only add a primary key index
            table.define_index(table_indexes_map[table_name][0], [columns[0]], "PRIMARY")
            pk_idx = table.get_index(table_indexes_map[table_name][0])
            print(f'For Table {table_name}, Index Definition Added:\n {pk_idx}')
        elif i == 1:
            # For the Second Table, I add a primary key index on the first column,
            # And add a index on the second column,
            # And add a unique index on the third column.
            table.define_index(table_indexes_map[table_name][0], [columns[0]], "PRIMARY")
            pk_idx = table.get_index(table_indexes_map[table_name][0])
            print(f'For Table {table_name}, Index Definition Added:\n {pk_idx}')

            table.define_index(table_indexes_map[table_name][1], [columns[1]], "INDEX")
            simple_idx = table.get_index(table_indexes_map[table_name][1])
            print(f'For Table {table_name}, Index Definition Added:\n {simple_idx}')

            table.define_index(table_indexes_map[table_name][2], [columns[2]], "UNIQUE")
            unique_idx = table.get_index(table_indexes_map[table_name][2])
            print(f'For Table {table_name}, Index Definition Added:\n {unique_idx}')
        else:
            # For the Third table, I add a primary key index on 1st and 2nd column,
            # And, add a index key on the third column
            table.define_index(table_indexes_map[table_name][0], [columns[0], columns[1]], "PRIMARY")
            pk_idx = table.get_index(table_indexes_map[table_name][0])
            print(f'For Table {table_name}, Index Definition Added:\n {pk_idx}')

            table.define_index(table_indexes_map[table_name][1], [columns[2]], "INDEX")
            simple_idx = table.get_index(table_indexes_map[table_name][1])
            print(f'For Table {table_name}, Index Definition Added:\n {simple_idx}')

    print("All the indexes were added successfully!!!")
    print('-----------------------------------------------------------------------------------')

#add_index_test()


def col_drop_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    table_names = ["test_table_1", "test_table_2", "test_table_3"]
    cols_to_drop = ["invalid_column", "t2_tc_3", "t3_tc_3"]

    for i, table_name in enumerate(table_names):
        table = cat.get_table(table_name)
        table.drop_column_definition(cols_to_drop[i])

    print("Intended Columns have been dropped!!!")
    print('-----------------------------------------------------------------------------------')


#col_drop_test()

def index_drop_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    table_names = ["test_table_1", "test_table_2", "test_table_3"]
    indexes_to_drop = ["invalid_index", "t2_index", "t3_PK_index"]

    for i, table_name in enumerate(table_names):
        table = cat.get_table(table_name)
        table.drop_index(indexes_to_drop[i])

    print("Intended Indexes have been dropped!!!")
    print('-----------------------------------------------------------------------------------')

#index_drop_test()

# Implementation provided
def describe_table_test():
    cat = CSVCatalog.CSVCatalog(
        dbhost="localhost",
        dbport=3306,
        dbuser="root",
        dbpw="dbuserdbuser",
        db="CSVCatalog")

    table_names = ["test_table_1", "test_table_2", "test_table_3"]

    for table_name in table_names:
        table = cat.get_table(table_name)
        desc = table.describe_table()
        print(f"DESCRIBE {table_name} = \n", json.dumps(desc, indent = 2))

    print('-----------------------------------------------------------------------------------')

#describe_table_test()

