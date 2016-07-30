import csv

def keys_to_string(keys):
    string = ""
    i = 0
    while i < len(keys) - 1:
        string += keys[i] + ", "
        i = i + 1
    string += keys[i]
    return string

def values(row):
    string = ""
    keys = row.keys()
    i = 0
    while(i < len(keys) - 1):
        if(row[keys[i]] == ""):
            string += "NULL, "
        elif(not row[keys[i]].isdigit()):
            string += "\'" + row[keys[i]] + "\'" + ", "
        else:
            string += row[keys[i]] + ", "
        i = i + 1
    if (row[keys[i]] == ""):
        string += "NULL"
    elif (not row[keys[i]].isdigit()):
        string += "\'" + row[keys[i]] + "\'"
    else:
        string += row[keys[i]]
    return string


def readCsv(fileName, tableName):
    sql_insert = ""
    rows = []
    with open(fileName) as csv_file:
        reader = csv.DictReader(csv_file)
        j = 0
        for row in reader:
            if(j == 0):
                sql_insert = """INSERT INTO """ + tableName + """(""" + keys_to_string(
                row.keys()) + """)""" + """VALUES(""" + values(row) + """)"""
            else:
                sql_insert += """, (""" + values(row) + """)"""
            j = j + 1
            rows.append(row)
    return sql_insert

if __name__ == "__main__":
    res = readCsv("guidatore.csv", "GUIDATORE")
    print res