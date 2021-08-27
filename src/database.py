import sqlite3

class Table:
    def __init__(self,database,tableName):
        self.database = database
        self.tableName = tableName
        try:
            queryString = "SELECT name FROM sqlite_master WHERE type='table' AND name='" + self.tableName + "';"
            results = self.database.cursor.execute(queryString).fetchall()
            if results == []:
                raise ValueError
        except:
            raise ValueError

    def insertRecord(self,record):
        try:
            queryString = "INSERT INTO " + str(self.tableName) + " VALUES ("
            for item in record:
                queryString += "'" + item + "', "
            
            queryString = queryString[:-2] + ")"
            self.database.connection.execute(queryString)
            self.database.connection.commit()

            return True

        except Exception as e:
            raise ValueError

    def insertRecords(self,records):
        try:
            queryString = "INSERT INTO " + str(self.tableName) + " VALUES ("
            for item in records:
                queryString += "?, "
            
            queryString = queryString[:-2] + ")"
            self.database.connection.executemany(queryString,records)
            self.database.connection.commit()
            
            return True
            
        except Exception as e:
            raise ValueError

    def readRecord(self):
        return
        
    def updateRecord(self):
        return

    def deleteRecord(self):
        return




class Database:

    def __init__(self,databaseFile):
        try:
            self.databaseFile = databaseFile
            self.connection = sqlite3.connect(self.databaseFile)
            self.cursor = self.connection.cursor()
        except Exception as e:
            raise FileNotFoundError

    def createTable(self, tableName, columnKeyPairs):
        try:
            queryString = 'CREATE TABLE ' + str(tableName) + '('
            
            for key,value in columnKeyPairs.items():
                queryString += key + ' ' + value + ', '

            queryString = queryString[:-2] + ');'

            self.cursor.execute(queryString)
            self.connection.commit()
            return True
        except:
            raise ValueError
    
    def selectTable(self,tableName):
        try:
            return Table(self,tableName)
        except:
            raise ValueError

    def dropTable(self, tableName):
        try:
            queryString = "DROP TABLE " + str(tableName) + ";"
            self.cursor.execute(queryString)
            self.connection.commit()
            return True
        except:
            raise ValueError