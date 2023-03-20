# Created by 720018271 on 10/03/2023 for dtsfoodhub
# Updated by 720085401 on 17/03/2023 for dtsfoodhub

import pyodbc
import socket

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

def getStockItems():
    query = "SELECT StockItem.id, itemname, itemunit, itemprice, stockcategory, available, itemaddlinfo FROM StockItem INNER JOIN StockCategory ON StockItem.categoryid=StockCategory.id ORDER BY displayorder"
    result = responseToDict(DBLink.execute(query))
    return result

def getStockCategories():
    query = "SELECT id, stockcategory, displayorder FROM StockCategory"
    result = responseToDict(DBLink.execute(query))
    return result

def deleteStockCategory(id):
    DBLink.execute(f"DELETE FROM StockCategory WHERE id = '{id}'")
    DBLink.commit()
    
def updateStockCategory(id,category,displayOrder):
    DBLink.execute(f"UPDATE StockCategory SET stockcategory = '{category}', displayorder = {displayOrder} WHERE id = '{id}'")
    DBLink.commit()
    
def addStockCategory(category, displayOrder):
    DBLink.execute(f"BEGIN TRANSACTION INSERT INTO StockCategory (stockcategory, displayorder) VALUES ('{category}',{displayOrder}) COMMIT TRANSACTION")
    DBLink.commit()
    
def deleteStockItem(id):
    DBLink.execute(f"DELETE FROM StockItem WHERE id = '{id}'")
    DBLink.commit()
    
def updateStockItem(id,name,unit,price,categoryid,available,info):
    DBLink.execute(f"UPDATE StockItem SET itemname = '{name}', itemunit = '{unit}', itemprice = '{price}', categoryid = '{categoryid}', available = '{available}', itemaddinfo = '{info}' WHERE id = '{id}'")
    DBLink.commit()
    
def addStockItem(name,unit,price,categoryid,available,info):
    DBLink.execute(f"INSERT INTO StockItem (itemname, itemunit, itemprice, available, categoryid, itemaddlinfo) VALUES ('{name}','{unit}','{price}','{available}','{categoryid}','{info}')")
    DBLink.commit()

def getCategoryId(category_name):
    category_id = (responseToDict(DBLink.execute(f"SELECT id FROM StockCategory WHERE stockcategory = '{category_name}'")))[0]['id']
    return category_id

def getNextId(type):
    table = 'StockCategory' if type == 'SC' else 'StockItem'
    last_id = (responseToDict(DBLink.execute(f"SELECT IDENT_CURRENT('{table}') as [id];")))[0]['id']
    return last_id
