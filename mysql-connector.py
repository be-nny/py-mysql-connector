import mysql.connector

"""
Basic mySQL connector
"""

class MyConnector:
    def __int__(self):
        """
        Constructor for creating a mySQL connector
        :return: NONE
        :raises: mysql.connector.errors.DatabaseError
        """
        db_name = input("Database Name >>")
        host = input("IP >>")
        port = input("Port Number >>")
        user = input("\nUsername >>")
        password = input("Password >>")
        print("Creating Connection")

        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.db_name = db_name
        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.db_name
            )
            self.connect()
        except mysql.connector.errors.DatabaseError:
            print("Data Base failed to connect")
            print(mysql.connector.errors.DatabaseError.args)

    def connect(self):
        """
        Checks if the instance has connected properly
        :return: NONE
        """
        if self.mydb.is_connected():
            print("INFO:" + self.mydb.get_server_info())
            print("VERSION" + self.mydb.get_server_version())
            print("\nDatabase Successfully Connected")
        else:
            print("Error connecting to database!")
            print("Is your IP whitelisted on the mySQL server?")

    def getDataBase(self):
        """
        Gets the database instance
        :return: the database instance
        """
        return self.mydb

    def getCursor(self):
        """
        Gets the cursor - This will allow queries to be executed
        :return: cursor
        """
        return self.mydb.cursor()


def connectToDatabase():
    """
    Get a new database instance
    :return: new database object
    """
    db = MyConnector()
    db.__int__()
    return db
