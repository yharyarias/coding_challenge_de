import mysql.connector

class MySQLHelper:
    def __init__(self):
        """
        Constructor method for the MySQLHelper class.

        Initializes the connection parameters and sets the default batch size.

        """
        self.host = "34.30.86.163"
        self.user = "challenge_client"
        self.password = "ch4ll3ng3*"
        self.database = "globant"
        self.connection = None
        self.cursor = None
        self.batchSize = 1000


    def insertBatchEmployees(self, data):
        """
        Insert a batch of employee data into the hired_employees table.

        data: List of employee data to be inserted.

        """
        self.insert_batch_data('hired_employees', data)

    def insertBatchDepartments(self, data):
        """
        Insert a batch of employee data into the departments table.

        data: List of employee data to be inserted.

        """
        self.insert_batch_data('departments', data)

    def insertBatchJobs(self, data):
        """
        Insert a batch of employee data into the jobs table.

        data: List of employee data to be inserted.

        """
        self.insert_batch_data('jobs', data)

    def insert_batch_data(self, table, data):
        """
        Insert a batch of data into the specified table.

        table: The name of the table to insert data into.
        data: List of data to be inserted.

        """
        if len(data) > 10000000:
            raise Exception("Max batch size is 1000")
        try:
            # Prepare the SQL statement based on the table name
            if table == 'hired_employees':
                sql = 'INSERT INTO hired_employees (id, name, datetime, department_id, job_id) VALUES (%s, %s, %s, %s, %s)'
            elif table == 'departments':
                sql = 'INSERT INTO departments (id, department) VALUES (%s, %s)'
            elif table == 'jobs':
                sql = 'INSERT INTO jobs (id, job) VALUES (%s, %s)'

            # Execute the SQL statement to insert the data
            self.cursor.executemany(sql, data)
            # Commit the changes to the database
            self.connection.commit()
        except Exception as e:
            # Roll back the changes in case of an error
            self.connection.rollback()
            print(f"Error during {table} insertion:", e)

    def connect(self):
        """
        Establish a connection to the MySQL database.

        """
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor(buffered=True)

    def disconnect(self):
        """
        Close the connection to the MySQL database.

        """
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()

    def execute_query(self, query, params=None):
        """
        Execute a SQL query.

        query: The SQL query to be executed.
        params: Optional parameters for the query.

        Returns:
        result: The result of the query.

        """
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor.fetchall()
        except mysql.connector.Error as error:
            print("Error executing query:", error)

    def fetch_all(self, table):
        """
        Fetch all rows from a table in the database.

        table: The name of the table to fetch data from.

        Returns:
        result: The result of the query
        """
        query = "SELECT * FROM {}".format(table)
        return self.execute_query(query)