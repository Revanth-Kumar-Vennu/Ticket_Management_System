import mysql.connector as mysql

from config import *


# Function to connect to MySQL server and optionally, database
def connection(database=None):
    args = {
        'host': HOST,
        'port': PORT,
        'user': USER,
        'password': PASSWORD,
        'use_pure': True
    }
    if database:
        args['database'] = database
    return mysql.connect(**args)

# Trying Connecting to MySQL server with credentials in config file
# Connection to start as soon as this script is imported
try:
    print(f"Connecting to MySQL server on {HOST}:{PORT}...")
    conn = connection()
except mysql.errors.ProgrammingError:
    print("MySQL User or password incorrect in config.ini")
    exit()
except mysql.errors.InterfaceError:
    print("Can't connect to the MySQL Server.")
    print("Make sure that the server is running")
    exit()

# Function to create new Database
def createDB():
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE {DATABASE}")
    cursor.close()



def sourceProc(procedure, *args, output=True, lastRowId=False):
    cursor = conn.cursor(buffered=output)
    if args:
        cursor.callproc(procedure, args) if procedure else None
    else:
        cursor.callproc(procedure) if procedure else None
    if output:
        for res in cursor.stored_results():
            result = res.fetchall()        
        
    if lastRowId:
        result = cursor.lastrowid
    conn.commit()
    cursor.close()
    if output or lastRowId:
        return result






# This section will run as soon as this script is imported
# To check if the database for this app exists or not
# The name of database is taken from the config file
# If not existing already (e.g. running this app for the first time),
# automatically creates the database and tables
# Also connects to the database of MySQL server
print(f"Connecting to {DATABASE} database...")
cur = conn.cursor(buffered=True)
newDB = False
cur.execute("SHOW DATABASES")
if (DATABASE,) not in cur.fetchall():
    print(f"No database named {DATABASE} found. Creating Database...")
    createDB()
    newDB = True
cur.close()
conn.close()
conn = connection(DATABASE)

   



