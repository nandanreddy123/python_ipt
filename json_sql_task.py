import json
import mysql.connector

name = input("enter your name")
age = int(input("enter your age"))
income = float(input("enter your income"))
age_limit = lambda age: True if (age > 18) else False
is_married = input("enter marital status (Y/N)")
married_status =lambda status: True if(status == "NO")else False
json_dic = {
    "name": name,
    "age": age,
    "income": income,
    "age_limit": age_limit(age),
    "married" : married_status(is_married)
}

with open("sample_json.json", "w") as output:
    output.write(json.dumps(json_dic))

with open("sample_json.json") as  json_file:
    json_data = json.load(json_file)

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="json_task"
)


cursor = database.cursor()


cursor.execute("CREATE TABLE json (name VARCHAR(255),age VARCHAR(25),income VARCHAR(25),"
               "age_limit VARCHAR(25),marital_status VARCHAR(25)")

sql = "INSERT INTO json (name, age,income,age_limit,marital_status) VALUES (%s, %s, %s, %s, %s)"
val = (
    json_data['name'],
    json_data['age'],
    json_data['income'],
    json_data['age_limit'],
    json_data['married']
)
cursor.execute(sql, val)

database.commit()

print(cursor.rowcount, "record inserted.")
