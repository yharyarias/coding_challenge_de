import mysql.connector

class MySQLHelper:
    def __init__(self):
        self.host = "34.30.86.163"
        self.user = "challenge_client"
        self.password = "ch4ll3ng3*"
        self.database = "challenge"
        self.connection = None
        self.cursor = None
        self.batchSize = 1000


    def insertBatchEmployees(self, data):
      #  if len(data) > 1000:
      #      raise Exception("Max batch size is 1000")
        try:
            self.cursor.executemany('INSERT INTO hired_employees (id, name, datetime, department_id, job_id) VALUES (%s, %s, %s, %s, %s)', data)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print("Error during employee insertion:", e)

    
    def insertBatchDepartments(self, data):
        if len(data) > 1000:
            raise Exception("Max batch size is 1000")
        try:
            self.cursor.executemany('INSERT INTO departments (id, department) VALUES (%s, %s)', data)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print("Error during employee insertion:", e)

    
    def insertBatchJobs(self, data):
        if len(data) > 1000:
            raise Exception("Max batch size is 1000")
        print(data)
        try:
            self.cursor.executemany('INSERT INTO jobs (id, job) VALUES (%s, %s)', data)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print("Error during employee insertion:", e)

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor(buffered=True)

    def disconnect(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor.fetchall()
        except mysql.connector.Error as error:
            print("Error executing query:", error)

    def fetch_all(self, table):
        query = "SELECT * FROM {}".format(table)
        return self.execute_query(query)