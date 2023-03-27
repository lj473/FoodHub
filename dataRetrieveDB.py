# Created by 720018271 on 10/03/2023 for dtsfoodhub
# Updated by 720085401 on 17/03/2023 for dtsfoodhub 

import pyodbc
import socket

def connectToDB(server,database, uid,pwd):
    '''
    Creates a database connection and cursor object (based on the credentials passed) using pyodbc
    '''
    if not server: # Using default value if no server provided
        DeviceName = str(socket.gethostname()) # Get device name to access local SQL server
        server = DeviceName + '\SQLEXPRESS'

    # ! Connection values are set at the top-level in dtsfoodhub.py !
    DBConnection = pyodbc.connect('Driver={SQL Server};' # Connect to database
                      f'Server={server};'
                      f'Database={database};'
                      f'UID={uid};'
                      f'PWD={pwd};')
                    #  'Trusted_Connection=yes;') # Use this for testing
    global DBLink
    DBLink = DBConnection.cursor() # Set database link object to use later

def responseToDict(response):
    '''
    This function allows us to transform SQL responses into a useful format for our application
    '''
    Columns = [Column[0] for Column in response.description] # Get names of columns
    
    Output = []
    for Row in response.fetchall(): # For each row in the table
        Output.append(dict(zip(Columns, Row))) # Put row details and column names together
        
    return Output

# Functionality functions - To be imported and called at the top-level application code

def checkUser(enteredUserName):
    '''
    Searches for the user in the database and returns a True or False statement. This will be useful for logging into the application.
    '''
    if len(responseToDict(DBLink.execute(f"SELECT * FROM Users WHERE UserName = '{enteredUserName}'")))>0: #If entered username is found in the database
        return True
    else:
        return False

def checkPassword(UserName,enteredPassword):
    '''
    Checks to see whether the password provided matches the password for the provided user. This will be useful for logging into the application.
    '''
    if responseToDict(DBLink.execute(f"SELECT * FROM Users WHERE UserName = '{UserName}'"))[0].get('UserPwd') == enteredPassword: #If entered password equals the one in database
        return True
    else:
        return False

def getStockItems():
    '''
    Gets all the stock items and returns as a dictionary, this will be loaded unto the tables in the UI
    '''
    query = "SELECT StockItem.id, itemname, itemunit, itemprice, stockcategory, available, itemaddlinfo FROM StockItem INNER JOIN StockCategory ON StockItem.categoryid=StockCategory.id"
    result = responseToDict(DBLink.execute(query))
    return result

def getStockCategories():
    '''
    Gets all the stock categories and returns as a dictionary, this will be loaded unto the tables in the UI.
    '''
    query = "SELECT id, stockcategory, displayorder FROM StockCategory"
    result = responseToDict(DBLink.execute(query))
    return result

def deleteStockCategory(id):
    '''
    Given the categoryid, deletes the stock category record in the database
    '''
    DBLink.execute(f"DELETE FROM StockCategory WHERE id = '{id}'")
    DBLink.commit()
    
def updateStockCategory(id,category,displayOrder):
    '''
    Given all the values for a particular stock category record, this function updates the record with those values
    '''
    DBLink.execute(f"UPDATE StockCategory SET stockcategory = '{category}', displayorder = {displayOrder} WHERE id = '{id}'")
    DBLink.commit()
    
def addStockCategory(category, displayOrder):
    '''
    Given the category name and display order, this function creates a new stock category record
    '''
    DBLink.execute(f"BEGIN TRANSACTION INSERT INTO StockCategory (stockcategory, displayorder) VALUES ('{category}',{displayOrder}) COMMIT TRANSACTION")
    DBLink.commit()
    
def deleteStockItem(id):
    '''
    Given the item's id, deletes the stock item record in the database
    '''
    DBLink.execute(f"DELETE FROM StockItem WHERE id = '{id}'")
    DBLink.commit()
    
def updateStockItem(id,name,unit,price,categoryid,available,info):
    '''
    Given all the column values for a stock item (including its id), this function updates the stock item record with those values
    '''
    DBLink.execute(f"UPDATE StockItem SET itemname = '{name}', itemunit = '{unit}', itemprice = '{price}', categoryid = '{categoryid}', available = '{available}', itemaddlinfo = '{info}' WHERE id = '{id}'")
    DBLink.commit()
    
def addStockItem(name,unit,price,categoryid,available,info):
    '''
    This function creates a new stock item record with teh values provided
    '''
    DBLink.execute(f"INSERT INTO StockItem (itemname, itemunit, itemprice, available, categoryid, itemaddlinfo) VALUES ('{name}','{unit}','{price}','{available}','{categoryid}','{info}')")
    DBLink.commit()

def getCategoryId(category_name):
    '''
    As the data may be manipulated for better readability for the user, they would select the item's category through its name rather than id
    This function finds the id of a particular category based on its name
    '''
    category_id = (responseToDict(DBLink.execute(f"SELECT id FROM StockCategory WHERE stockcategory = '{category_name}'")))[0]['id']
    return category_id

def getCurrentId(type):
    '''
    Gets the table's current auto-increment id, which allows us to know what ID will be used for the next record we want to create
    '''
    table = 'StockCategory' if type == 'SC' else 'StockItem' if type == 'SI' else False
    last_id = (responseToDict(DBLink.execute(f"SELECT IDENT_CURRENT('{table}') as [id];")))[0]['id']
    return last_id
