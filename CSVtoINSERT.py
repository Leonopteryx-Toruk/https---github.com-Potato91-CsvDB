import csv

def keys_to_string(keys, nomeTabella):
    string = ""
    idTabella = "id" + nomeTabella.lower()
    i = 0
    while i < len(keys) - 1:
        if(not idTabella == keys[i].lower()):
            string += keys[i] + ", "
        i = i + 1
    if(not idTabella == keys[i].lower()):
        string += keys[i]
    else:
        string = string[:len(string)-2]
    return string

def values(row, nomeTabella):
    string = ""
    idTabella = "id" + nomeTabella.lower()
    keys = row.keys()
    i = 0
    while(i < len(keys) - 1):
        if(not idTabella == keys[i].lower()):
            if(row[keys[i]] == ""):
                string += "NULL, "
            elif(not row[keys[i]].isdigit()):
                string += "\'" + row[keys[i]] + "\'" + ", "
            else:
                string += row[keys[i]] + ", "
        i = i + 1
    if (not idTabella == keys[i].lower()):
        if (row[keys[i]] == ""):
            string += "NULL"
        elif (not row[keys[i]].isdigit()):
            string += "\'" + row[keys[i]] + "\'"
        else:
            string += row[keys[i]]
    else:
        string = string[:len(string) - 2]
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
                row.keys(), tableName) + """)""" + """VALUES(""" + values(row, tableName) + """)"""
            else:
                sql_insert += """, (""" + values(row, tableName) + """)"""
            j = j + 1
            rows.append(row)
    return sql_insert

if __name__ == "__main__":
    res = readCsv("varco.csv", "VARCO")
    print res