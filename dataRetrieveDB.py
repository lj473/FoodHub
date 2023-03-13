# Created by 720018271 on 10/03/2023 for dtsfoodhub

import pyodbc
import socket
from global_vars import dbinfo

def connectToDB(): #Function to connect to database
    DeviceName = str(socket.gethostname()) #Get device name to access local SQL server
    DBConnection = pyodbc.connect('Driver={SQL Server};' #Connect to database
                      f'Server={DeviceName}\SQLEXPRESS;'
                      'Database=nfhcw2;'
                      'Trusted_Connection=yes;')
    global DBLink
    DBLink = DBConnection.cursor() #Set database link object to use later

def DBTest(): #Used for testing
    Result = DBLink.execute('SELECT * FROM Contact')
    
    return responseToDict(Result)

def responseToDict(response): #Function to connect to database
    Columns = [Column[0] for Column in response.description] #Get names of columns
    
    Output = []
    for Row in response.fetchall(): #For each row in the table
        Output.append(dict(zip(Columns, Row))) #Put row details and column names together
        
    return Output

#Functionality functions

def checkUser(enteredUserName):
    if len(responseToDict(DBLink.execute(f"SELECT * FROM Users WHERE UserName = '{enteredUserName}'")))>0: #If entered username is found in the database
        return True
    else:
        return False

def checkPassword(UserName,enteredPassword):
    if responseToDict(DBLink.execute(f"SELECT * FROM Users WHERE UserName = '{UserName}'"))[0].get('UserPwd') == enteredPassword: #If entered password equals the one in database
        return True
    else:
        return False