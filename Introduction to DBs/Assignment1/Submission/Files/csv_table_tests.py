"""

csv_table_tests.py

"""

from src.CSVDataTable import CSVDataTable

import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
data_dir = os.path.abspath("../Data/Baseball")


def tests_people():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }
    people = CSVDataTable("People", connect_info, ["playerID"])
    try:

        print()
        print("find_by_primary_key(): Known Record")
        print(people.find_by_primary_key(["aardsda01"]))

        print()
        print("find_by_primary_key(): Unknown Record")
        print(people.find_by_primary_key((["cah2251"])))

        print()
        print("find_by_primary_key(): Known Record with Field List Projected")
        field_list = ["playerID", "nameFirst", "nameLast", "nameGiven", "debut", "finalGame"]
        print(people.find_by_primary_key(["aardsda01"], field_list))

        print()
        field_list = ["playerID", "nameFirst", "nameLast", "nameGiven", "debut", "finalGame"]
        print("find_by_primary_key(): Unknown Record with Field List Projected")
        print(people.find_by_primary_key(["cah2251"], field_list))

        print()
        print("find_by_template(): Known Template")
        template = {"nameFirst": "David", "nameLast": "Aardsma", "nameGiven": "David Allan"}
        print(people.find_by_template(template))

        print()
        print("find_by_template(): Known Template - Multiple Records")
        template = {"birthState": "AL", "birthCity": "Mobile"}
        print(people.find_by_template(template))

        print()
        print("find_by_template(): Unknown Record with Empty Data Possibility")
        template = {"birthState": "GA", "birthCity": "Atlanta", "deathYear": "1984"}
        print(people.find_by_template(template))

        print()
        print("find_by_template(): Known Template - Field List Projected")
        field_list = ["playerID", "nameFirst", "nameLast", "nameGiven", "debut", "finalGame"]
        template = {"nameFirst": "David", "nameLast": "Aardsma", "nameGiven": "David Allan"}
        print(people.find_by_template(template, field_list))

        print()
        print("find_by_template(): Known Template - Multiple Records - Field List Projected")
        field_list = ["playerID", "nameFirst", "nameLast", "nameGiven", "debut", "finalGame"]
        template = {"birthState": "AL", "birthCity": "Mobile"}
        print(people.find_by_template(template, field_list))

        print()
        print("find_by_template(): Unknown Record with Empty Data Possibility - Field List Projected")
        field_list = ["playerID", "nameFirst", "nameLast", "nameGiven"]
        template = {"birthState": "GA", "birthCity": "Atlanta", "deathYear": "1984"}
        print(people.find_by_template(template, field_list))

        print()
        print("delete_by_key(): Known Record")
        print(people.delete_by_key(["akersbi01"]))

        print()
        print("delete_by_key(): UnKnown Record")
        print(people.delete_by_key(["csuri21296"]))

        print()
        print("delete_by_template(): Known Record")
        template = {"weight": "215", "height": "75", "bats": "R", "retroID": "aberr001"}
        print(people.delete_by_template(template))

        print()
        print("delete_by_template(): Known Records - Multiple Entries Matching")
        template = {"weight": "215", "height": "75"}
        print(people.delete_by_template(template))

        print()
        print("delete_by_template(): UnKnown Record")
        template = {"birthState": "GA", "birthCity": "Atlanta", "deathYear": "1984"}
        print(people.delete_by_template(template))

        print()
        print("delete_by_template(): UnKnown Key entered")
        template = {"birthState": "GA", "birthCity": "Atlanta", "dY": "1965"}
        print(people.delete_by_template(template))

        print()
        print("update_by_key(): Update Known Record's Columns - Columns don't contain the primary key components")
        primary_keys = ["akersje01"]
        new_records = {"birthYear": "1891", "birthMonth": "2", "birthDay": "21"}
        print("Record BEFORE updation:")
        print(people.find_by_primary_key(primary_keys))
        print(people.update_by_key(primary_keys, new_records))
        print("Record AFTER updation:")
        print(people.find_by_primary_key(primary_keys))

        print()
        print("update_by_key(): Update UnKnown Record's Columns")
        primary_keys = ["cs4090"]
        new_records = {"birthYear": "1891", "birthMonth": "2", "birthDay": "21"}
        print("Record BEFORE updation:")
        print(people.find_by_primary_key(primary_keys))
        print(people.update_by_key(primary_keys, new_records))
        print("Record AFTER updation:")
        print(people.find_by_primary_key(primary_keys))

        print()
        print(
            "update_by_key(): Update Known Record's Columns - "
            "Columns contain the primary key components")
        primary_keys = ["albieoz01"]
        new_primary_keys = ["alburvi01"]
        new_records = {"playerID": new_primary_keys[0], "deathYear": "2020", "deathMonth": "12", "deathDay": "7"}
        print("Record BEFORE updation:")
        print(people.find_by_primary_key(primary_keys))
        print(people.update_by_key(primary_keys, new_records))
        print("Record AFTER updation:")
        print(people.find_by_primary_key(primary_keys))
        print("Duplicate Record Found:")
        print((people.find_by_primary_key(new_primary_keys)))

        print()
        print("update_by_template(): Update Known Records' Columns - Columns don't contain the primary key components")
        template = {"birthYear": "1891", "birthMonth": "2", "birthDay": "21"}
        new_records = {"deathYear": "1994", "deathMonth": "7", "deathDay": "14"}
        print("Records BEFORE updation:")
        print(people.find_by_template(template))
        print(people.update_by_template(template, new_records))
        print("Records AFTER updation:")
        print(people.find_by_template(template))

        print()
        print("update_by_template(): Update UnKnown Records' Columns")
        template = {"playerID": "csuri21296", "retroID": "chan2102", "bbrefID": "chansu21"}
        new_records = {"deathCountry": "USA", "deathState": "CA", "deathCity": "Los Angeles"}
        print("Records BEFORE updation:")
        print(people.find_by_template(template))
        print(people.update_by_template(template, new_records))
        print("Records AFTER updation:")
        print(people.find_by_template(template))

        print()
        print(
            "update_by_template(): Update Known Record's Columns - "
            "Columns contain the primary key components")
        template = {"birthYear": "1891", "birthMonth": "2", "birthDay": "21"}
        new_primary_keys = ["chansu21"]
        new_records = {"playerID": new_primary_keys[0], "deathYear": "1994", "deathMonth": "7", "deathDay": "14",
                       "deathCountry": "USA", "deathState": "CA", "deathCity": "Los Angeles"}
        print("Records BEFORE updation:")
        print(people.find_by_template(template))
        print(people.update_by_template(template, new_records))
        print("Records AFTER updation:")
        print(people.find_by_template(template))

        print()
        print("insert(): No Duplication of Primary Key")
        primary_keys = ["chansu4090"]
        new_record = {"playerID": primary_keys[0], "birthYear": "1996", "birthMonth": "2", "birthDay": "21",
                      "birthCountry": "India", "birthState": "UP", "birthCity": "Lucknow",
                      "deathYear": "", "deathMonth": "", "deathDay": "", "deathCountry": "", "deathState": "",
                      "deathCity": "", "nameFirst": "Chandan", "nameLast": "Suri", "nameGiven": "Chandan",
                      "weight": "180", "height": "72", "bats": "R", "throws": "R", "debut": "2010-05-24",
                      "finalGame": "2020-02-26", "retroID": "chansuri49", "bbrefID": "chansu007"}
        print(people.insert(new_record))
        print("AFTER Insertion:")
        print(people.find_by_template(new_record))

        print()
        print("insert(): Duplication of Primary Key")
        primary_keys = ["chansu4090"]
        new_record = {"playerID": primary_keys[0], "birthYear": "1991", "birthMonth": "2", "birthDay": "21",
                      "birthCountry": "USA", "birthState": "NY", "birthCity": "New York",
                      "deathYear": "", "deathMonth": "", "deathDay": "", "deathCountry": "", "deathState": "",
                      "deathCity": "", "nameFirst": "Chan", "nameLast": "Su", "nameGiven": "Chan",
                      "weight": "185", "height": "73", "bats": "L", "throws": "L", "debut": "2008-05-24",
                      "finalGame": "2018-02-26", "retroID": "chansu4900", "bbrefID": "chansu001"}
        print(people.insert(new_record))
        print("AFTER Insertion:")
        print(people.find_by_template(new_record))
        print("Record with Duplicate PK Present:")
        print(people.find_by_primary_key(primary_keys))

        print()
        print("insert(): Primary Key Not Present as part of Insertion and No Default Set")
        primary_keys = ["chansu40902"]
        new_record = {"birthYear": "1991", "birthMonth": "2", "birthDay": "21",
                      "birthCountry": "USA", "birthState": "NY", "birthCity": "New York",
                      "deathYear": "", "deathMonth": "", "deathDay": "", "deathCountry": "", "deathState": "",
                      "deathCity": "", "nameFirst": "Chan", "nameLast": "Su", "nameGiven": "Chan",
                      "weight": "185", "height": "73", "bats": "L", "throws": "L", "debut": "2008-05-24",
                      "finalGame": "2018-02-26", "retroID": "chansu4900", "bbrefID": "chansu001"}
        print(people.insert(new_record))
        print("AFTER Insertion:")
        print(people.find_by_template(new_record))

        print()
        print("insert(): Primary Key Value set to NULL")
        primary_keys = ["chansu40903"]
        new_record = {"playerID": None, "birthYear": "1991", "birthMonth": "2", "birthDay": "21",
                      "birthCountry": "USA", "birthState": "NY", "birthCity": "New York",
                      "deathYear": "", "deathMonth": "", "deathDay": "", "deathCountry": "", "deathState": "",
                      "deathCity": "", "nameFirst": "Chan", "nameLast": "Su", "nameGiven": "Chan",
                      "weight": "185", "height": "73", "bats": "L", "throws": "L", "debut": "2008-05-24",
                      "finalGame": "2018-02-26", "retroID": "chansu4900", "bbrefID": "chansu001"}
        print(people.insert(new_record))
        print("AFTER Insertion:")
        print(people.find_by_template(new_record))

    except Exception as e:
        print("An error occurred:", e)


def tests_batting():
    connect_info = {
        "directory": data_dir,
        "file_name": "Batting.csv"
    }
    batting = CSVDataTable("Batting", connect_info, ["playerID", "yearID", "stint"])
    try:
        print()
        print("find_by_primary_key(): Known Record")
        print(batting.find_by_primary_key(["abercda01", "1871", "1"]))

        print()
        print("find_by_primary_key(): Unknown Record - Partially Not Matching")
        print(batting.find_by_primary_key(["abercda01", "1894", "2"]))

        print()
        print("find_by_primary_key(): Unknown Record - Completely Not Matching")
        print(batting.find_by_primary_key(["chansu212", "1894", "2"]))

        print()
        print("find_by_primary_key(): Known Record with Field List Projected")
        field_list = ["playerID", "yearID", "stint", "teamID", "lgID", "G", "AB", "R", "H"]
        print(batting.find_by_primary_key(["goldswa01", "1871", "1"], field_list))

        print()
        print("find_by_primary_key(): Unknown Record - Partially Not Matching with Field List Projected")
        field_list = ["playerID", "yearID", "stint", "teamID", "lgID", "G", "AB", "R", "H"]
        print(batting.find_by_primary_key(["abercda01", "1894", "2"], field_list))

        print()
        print("find_by_primary_key(): Unknown Record - Completely Not Matching with Field List Projected")
        field_list = ["playerID", "yearID", "stint", "teamID", "lgID", "G", "AB", "R", "H"]
        print(batting.find_by_primary_key(["chansu212", "1894", "2"], field_list))

        print()
        print("find_by_template(): Known Template")
        template = {"2B": "7", "3B": "2", "HR": "1", "RBI": "31"}
        print(batting.find_by_template(template))

        print()
        print("find_by_template(): Known Template with subpart of Composite PK")
        template = {"playerID": "ganzech01", "2B": "7", "3B": "2", "HR": "1", "RBI": "31"}
        print(batting.find_by_template(template))

        print()
        print("find_by_template(): Unknown Record with Empty Data Possibility")
        template = {"SO": "31", "IBB": "2", "HBP": "1", "SH": "8", "SF": "1", "GIDP": "3"}
        print(batting.find_by_template(template))

        print()
        print("find_by_template(): Known Template - Field List Projected")
        field_list = ["playerID", "yearID", "teamID", "lgID", "G", "AB", "R", "H"]
        template = {"G": "66", "AB": "100", "R": "13", "H": "31"}
        print(batting.find_by_template(template, field_list))

        print()
        print("find_by_template(): Unknown Record with Empty Data Possibility - Field List Projected")
        field_list = ["playerID", "yearID", "teamID", "lgID", "G", "AB", "R", "H", "2B", "3B"]
        template = {"playerID": "barnero01", "G": "31", "AB": "157", "IBB": "2"}
        print(batting.find_by_template(template, field_list))

        print()
        print("delete_by_key(): Known Record")
        print(batting.delete_by_key(["moraljo01", "1977", "1"]))

        print()
        print("delete_by_key(): Unknown Record - Partially Matching Keys")
        print(batting.delete_by_key(["nolanga01", "1977", "3"]))

        print()
        print("delete_by_key(): Unknown Record - Not Matching")
        print(batting.delete_by_key(["csuri212", "1922", "10"]))

        print()
        print("delete_by_template(): Known Record")
        template = {"yearID": "1871", "stint": "1", "teamID": "CL1"}
        print(batting.delete_by_template(template))

        print()
        print("delete_by_template(): UnKnown Record")
        template = {"yearID": "1871", "stint": "1", "teamID": "CL1", "G": "20", "AB": "3"}
        print(batting.delete_by_template(template))

        print()
        print("delete_by_template(): UnKnown Key entered")
        template = {"yearID": "1871", "G": "20", "Ab": "94"}
        print(batting.delete_by_template(template))

        print()
        print("update_by_key(): Update Known Record's Columns - Columns don't contain the primary key components")
        primary_keys = ["stanlbo01", "1984", "1"]
        new_records = {"lgID": "NL", "G": "28", "AB": "49", "R": "22", "H": "44"}
        print("Record BEFORE updation:")
        print(batting.find_by_primary_key(primary_keys))
        print(batting.update_by_key(primary_keys, new_records))
        print("Record AFTER updation:")
        print(batting.find_by_primary_key(primary_keys))

        print()
        print("update_by_key(): Update UnKnown Record's Columns - Partially Matching PKs - Test 1")
        primary_keys = ["grimsja01", "1996", "3"]
        new_records = {"lgID": "NL", "G": "28", "AB": "49", "R": "22", "H": "44"}
        print("Record BEFORE updation:")
        print(batting.find_by_primary_key(primary_keys))
        print(batting.update_by_key(primary_keys, new_records))
        print("Record AFTER updation:")
        print(batting.find_by_primary_key(primary_keys))

        print()
        print("update_by_key(): Update UnKnown Record's Columns - Partially Matching PKs - Test 2")
        primary_keys = ["chansu4090", "2019", "3"]
        new_records = {"lgID": "NL", "G": "28", "AB": "49", "R": "22", "H": "44"}
        print("Record BEFORE updation:")
        print(batting.find_by_primary_key(primary_keys))
        print(batting.update_by_key(primary_keys, new_records))
        print("Record AFTER updation:")
        print(batting.find_by_primary_key(primary_keys))

        print()
        print("update_by_key(): Update Known Record's Columns - "
              "Columns contain the primary key components - Test 1")
        primary_keys = ["gomezch02", "1996", "1"]
        new_primary_keys = ["chansu4090", "1966", "3"]
        new_records = {"playerID": new_primary_keys[0], "yearID": new_primary_keys[1], "stint": new_primary_keys[2],
                       "lgID": "NA", "G": "99", "AB": "52"}
        print("Record BEFORE updation:")
        print(batting.find_by_primary_key(primary_keys))
        print(batting.update_by_key(primary_keys, new_records))
        print("Record AFTER updation:")
        print(batting.find_by_primary_key(new_primary_keys))

        print()
        print("update_by_key(): Update Known Record's Columns - "
              "Columns contain the primary key components - Test 2")
        primary_keys = ["orourjo01", "1879", "1"]
        new_primary_keys = ["quinnjo01", "1881", "2"]
        new_records = {"playerID": new_primary_keys[0], "yearID": new_primary_keys[1], "stint": new_primary_keys[2],
                       "lgID": "NA", "G": "99", "AB": "122"}
        print("Record BEFORE updation:")
        print(batting.find_by_primary_key(primary_keys))
        print(batting.update_by_key(primary_keys, new_records))
        print("Record AFTER updation:")
        print(batting.find_by_primary_key(primary_keys))
        print("Duplicate Record Found:")
        print(batting.find_by_primary_key(new_primary_keys))

        print()
        print("update_by_template(): Update Known Records' Columns - Columns don't contain the primary key components")
        template = {"teamID": "DET", "lgID": "AL", "2B": "0", "HBP": "1", "SH": "1"}
        new_records = {"3B": "1", "HR": "5", "SB": "1"}
        print("Records BEFORE updation:")
        print(batting.find_by_template(template))
        print(batting.update_by_template(template, new_records))
        print("Records AFTER updation:")
        print(batting.find_by_template(template))

        print()
        print("update_by_template(): Update UnKnown Records' Columns")
        template = {"teamID": "DET", "lgID": "AL", "2B": "9", "HBP": "1", "SH": "3"}
        new_records = {"3B": "1", "HR": "5", "SB": "1"}
        print("Records BEFORE updation:")
        print(batting.find_by_template(template))
        print(batting.update_by_template(template, new_records))
        print("Records AFTER updation:")
        print(batting.find_by_template(template))

        print()
        print("update_by_template(): Update Known Record's Columns - "
              "Columns contain the primary key components")
        template = {"teamID": "DET", "lgID": "AL", "2B": "0", "HBP": "1", "SH": "1"}
        new_primary_keys = ["chansu21", "2001", "2"]
        new_records = {"playerID": new_primary_keys[0], "yearID": new_primary_keys[1], "stint": new_primary_keys[2],
                       "G": "99", "AB": "122"}
        print("Records BEFORE updation:")
        print(batting.find_by_template(template))
        print(batting.update_by_template(template, new_records))
        print("Records AFTER updation:")
        print(batting.find_by_template(template))

        print()
        print("insert(): No Duplication of Primary Key")
        primary_keys = ["chansu4090", "1996", "2"]
        new_record = {"playerID": primary_keys[0], "yearID": primary_keys[1], "stint": primary_keys[2], "teamID": "CS1",
                      "lgID": "AL", "G": "99", "AB": "121", "R": "32", "H": "57", "2B": "6", "3B": "7", "HR": "2",
                      "RBI": "321", "SB": "4", "CS": "3", "BB": "21", "SO": "3", "IBB": "0", "HBP": "", "SH": "",
                      "SF": "", "GIDP": "2"}
        print(batting.insert(new_record))
        print("AFTER Insertion:")
        print(batting.find_by_template(new_record))

        print()
        print("insert(): Duplication of Primary Key")
        primary_keys = ["chansu4090", "1996", "2"]
        new_record = {"playerID": primary_keys[0], "yearID": primary_keys[1], "stint": primary_keys[2], "teamID": "CL2",
                      "lgID": "NA", "G": "122", "AB": "191", "R": "45", "H": "75", "2B": "2", "3B": "2", "HR": "5",
                      "RBI": "281", "SB": "3", "CS": "2", "BB": "11", "SO": "0", "IBB": "1", "HBP": "", "SH": "",
                      "SF": "", "GIDP": "2"}
        print(batting.insert(new_record))
        print("AFTER Insertion:")
        print(batting.find_by_template(new_record))
        print("Record with Duplicate PK Present:")
        print(batting.find_by_primary_key(primary_keys))

        print()
        print("insert(): Primary Key Not Present as part of Insertion and No Default Set - Test 1")
        primary_keys = ["chansu40901", "1995", "1"]
        new_record = {"playerID": primary_keys[0], "yearID": primary_keys[1], "teamID": "CL2",
                      "lgID": "NA", "G": "122", "AB": "191", "R": "45", "H": "75", "2B": "2", "3B": "2", "HR": "5",
                      "RBI": "281", "SB": "3", "CS": "2", "BB": "11", "SO": "0", "IBB": "1", "HBP": "", "SH": "",
                      "SF": "", "GIDP": "2"}
        print(batting.insert(new_record))
        print("AFTER Insertion:")
        print(batting.find_by_template(new_record))

        print()
        print("insert(): Primary Key Not Present as part of Insertion and No Default Set - Test 2")
        primary_keys = ["chansu40902", "1994", "0"]
        new_record = {"playerID": primary_keys[0], "teamID": "CL2",
                      "lgID": "NA", "G": "122", "AB": "191", "R": "45", "H": "75", "2B": "2", "3B": "2", "HR": "5",
                      "RBI": "281", "SB": "3", "CS": "2", "BB": "11", "SO": "0", "IBB": "1", "HBP": "", "SH": "",
                      "SF": "", "GIDP": "2"}
        print(batting.insert(new_record))
        print("AFTER Insertion:")
        print(batting.find_by_template(new_record))

        print()
        print("insert(): Primary Key Not Present as part of Insertion and No Default Set - Test 3")
        primary_keys = ["chansu40903", "1993", "3"]
        new_record = {"teamID": "CL2",
                      "lgID": "NA", "G": "122", "AB": "191", "R": "45", "H": "75", "2B": "2", "3B": "2", "HR": "5",
                      "RBI": "281", "SB": "3", "CS": "2", "BB": "11", "SO": "0", "IBB": "1", "HBP": "", "SH": "",
                      "SF": "", "GIDP": "2"}
        print(batting.insert(new_record))
        print("AFTER Insertion:")
        print(batting.find_by_template(new_record))

        print()
        print("insert(): Primary Key Value set to NULL - Test 1")
        primary_keys = ["chansu40901", "1995", "1"]
        new_record = {"playerID": primary_keys[0], "yearID": primary_keys[1], "stint": None, "teamID": "CL2",
                      "lgID": "NA", "G": "122", "AB": "191", "R": "45", "H": "75", "2B": "2", "3B": "2", "HR": "5",
                      "RBI": "281", "SB": "3", "CS": "2", "BB": "11", "SO": "0", "IBB": "1", "HBP": "", "SH": "",
                      "SF": "", "GIDP": "2"}
        print(batting.insert(new_record))
        print("AFTER Insertion:")
        print(batting.find_by_template(new_record))

        print()
        print("insert(): Primary Key Value set to NULL - Test 2")
        primary_keys = ["chansu40902", "1994", "0"]
        new_record = {"playerID": primary_keys[0], "yearID": None, "stint": None, "teamID": "CL2",
                      "lgID": "NA", "G": "122", "AB": "191", "R": "45", "H": "75", "2B": "2", "3B": "2", "HR": "5",
                      "RBI": "281", "SB": "3", "CS": "2", "BB": "11", "SO": "0", "IBB": "1", "HBP": "", "SH": "",
                      "SF": "", "GIDP": "2"}
        print(batting.insert(new_record))
        print("AFTER Insertion:")
        print(batting.find_by_template(new_record))

        print()
        print("insert(): Primary Key Value set to NULL - Test 3")
        primary_keys = ["chansu40903", "1993", "3"]
        new_record = {"playerID": None, "yearID": None, "stint": None, "teamID": "CL2",
                      "lgID": "NA", "G": "122", "AB": "191", "R": "45", "H": "75", "2B": "2", "3B": "2", "HR": "5",
                      "RBI": "281", "SB": "3", "CS": "2", "BB": "11", "SO": "0", "IBB": "1", "HBP": "", "SH": "",
                      "SF": "", "GIDP": "2"}
        print(batting.insert(new_record))
        print("AFTER Insertion:")
        print(batting.find_by_template(new_record))

    except Exception as e:
        print("An error occurred:", e)


if __name__ == '__main__':
    tests_people()
    tests_batting()
