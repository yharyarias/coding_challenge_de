import mysql.connector

mydb = mysql.connector.connect(
  host="34.30.86.163",
  user="challenge_client",
  password="ch4ll3ng3*"
)

print(mydb)