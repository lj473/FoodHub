# Created by 720018271 on 10/03/2023 for dtsfoodhub
# Updated by 720085401 on 13/03/2023 for dtsfoodhub

from PyQt5.QtWidgets import *
import dataRetrieveDB # Import functions to contact db
from loginScr import Ui_loginScr # Import login screen class from Qt
from homeScr import Ui_homeScr # Import home screen class from Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Showing the login screen as soon as the user starts the application
        self.show_login_screen()

    def show_login_screen(self):
        """
        Display the login page.
        Makes call to login function to authenticate the user to the database.
        """
        self.loginScr = QWidget()
        self.login_ui = Ui_loginScr() # From Qt Designer
        self.login_ui.setupUi(self.loginScr)
        self.loginScr.show()

        # Call the login function to authenticate using the credentials provided by the user
        self.login_ui.btnConfim.clicked.connect(self.login)

        # Allowing the user to exit the program by clicking the 'Cancel' button
        self.login_ui.btnClear.clicked.connect(self.loginScr.close)

    def show_home_screen(self):
        """
        Display the home page.
        This function uses multiple signals as part of event-driven programming. These signals trigger other functions that
        allow the user to perform CRUD operations on the database
        """
        # Once we are logged in we can show the Home Screen
        self.homeScr = QWidget() 
        self.home_ui = Ui_homeScr() # From Qt Designer
        self.home_ui.setupUi(self.homeScr)

        # Setting up Stock Categories tab and assigning slots to signals
        self.home_ui.SC_table.setEditTriggers(QAbstractItemView.NoEditTriggers) # Stops the user from double-clicking to edit the table
        self.home_ui.SC_table.cellClicked.connect(self.SCtableSelect)
        self.home_ui.SC_plusBtn.clicked.connect(self.SCaddMode)

        self.home_ui.SC_addBtn.setHidden(True)
        self.home_ui.SC_deleteBtn.setHidden(True)
        self.home_ui.SC_updateBtn.setHidden(True)

        # Assigning functions we created that handle CRUD operations to signals
        self.home_ui.SC_deleteBtn.clicked.connect(self.SCdeleteCategory)
        self.home_ui.SC_updateBtn.clicked.connect(self.SCupdateCategory)
        self.home_ui.SC_addBtn.clicked.connect(self.SCaddCategory)

        # Allowing the user to exit the program through the 'Cancel' button
        self.home_ui.SC_cancelBtn.clicked.connect(self.homeScr.close)


        # Setting up Stock Items tab and assigning slots to signals
        self.home_ui.SI_table.setEditTriggers(QAbstractItemView.NoEditTriggers) # Stops the user from double-clicking to edit the table
        self.home_ui.SI_table.cellClicked.connect(self.SItableSelect)
        self.home_ui.SI_plusBtn1.clicked.connect(self.SIaddMode)

        self.home_ui.SI_addBtn1.setHidden(True)
        self.home_ui.SI_deleteBtn1.setHidden(True)
        self.home_ui.SI_updateBtn1.setHidden(True)

        # Assigning functions we created that handle CRUD operations to signals
        self.home_ui.SI_deleteBtn1.clicked.connect(self.SIdeleteItem)
        self.home_ui.SI_updateBtn1.clicked.connect(self.SIupdateItem)
        self.home_ui.SI_addBtn1.clicked.connect(self.SIaddItem)

        # Allowing the user to exit the program through the 'Cancel' button
        self.home_ui.SI_cancelBtn1.clicked.connect(self.homeScr.close)

        # Loading our data unto the Stock Category and Item tables
        self.load_stock_categories() 
        self.load_stock_items() 

        self.homeScr.show()
    
    def SCaddMode(self):
        '''
        Stock Categories:
        Setting up the environment for the 'Add' mode where the user can create records for the stock categories
        '''
        # Changing mode by hiding specific buttons
        self.home_ui.SC_addBtn.setHidden(False)
        self.home_ui.SC_deleteBtn.setHidden(True)
        self.home_ui.SC_updateBtn.setHidden(True)
        
        # Setting up the default values
        self.home_ui.SC_IdEbox.setPlainText(str(dataRetrieveDB.getCurrentId(type='SC') + 1)) # This logic won't work if values get deleted as there will be repeating id's
        self.home_ui.SC_stockCatEbox.setPlainText("")
        self.home_ui.SC_spinBox.setValue(0)
    
    def SCtableSelect(self,row):
        '''
        Stock Categories:
        Setting up the environment for the 'Edit' mode and populating the edit boxes (and other input methods in the screen)
        with the information from the record that was selected by the user clicking on it 
        '''
        # Changing mode by hiding specific buttons
        self.home_ui.SC_addBtn.setHidden(True)
        self.home_ui.SC_deleteBtn.setHidden(False)
        self.home_ui.SC_updateBtn.setHidden(False)

        # Declaring variables with row data
        id = self.home_ui.SC_table.item(row,0).text()
        category = self.home_ui.SC_table.item(row,1).text()
        displayOrder = self.home_ui.SC_table.item(row,2).text()
        
        # Showing data in edit boxes (etc) at the bottom
        self.home_ui.SC_IdEbox.setPlainText(id)
        self.home_ui.SC_stockCatEbox.setPlainText(category)
        self.home_ui.SC_spinBox.setValue(int(displayOrder))

    def SCdeleteCategory(self):
        '''
        Stock Categories:
        Calling the deleteStockCategory function from our SQL connectivity layer to delete the record selected by the user
        '''
        id = self.home_ui.SC_IdEbox.toPlainText()
        dataRetrieveDB.deleteStockCategory(id)
        self.load_stock_categories() # Refreshing values in the table to ensure parity with db
        self.load_stock_items() # Refreshing Category Combo Box for Stock items with the changes
        self.SCaddMode()

    def SCupdateCategory(self):
        '''
        Stock Categories:
        Calling the updateStockCategory function from our SQL connectivity layer to update the record selected by the user with the information changed on the 
        edit boxes or spin box
        '''
        try: # To catch errors interacting with the database without breaking the UI
            # Declaring variables with data input by the user in the boxes
            id = self.home_ui.SC_IdEbox.toPlainText()
            category = self.home_ui.SC_stockCatEbox.toPlainText()
            displayOrder = self.home_ui.SC_spinBox.value()
            dataRetrieveDB.updateStockCategory(id, category, displayOrder)
            self.load_stock_categories() # Refreshing values in the table to ensure parity with db
            self.load_stock_items()
        except:
            self.input_error_msg()

    def SCaddCategory(self):
        '''
        Stock Categories:
        Calling the addStockCategory function from our SQL connectivity layer to create a record with the information entered on the 
        edit boxes or spin box by the user (the id is automatically generated for data integrity)
        '''
        try: # To catch errors interacting with the database without breaking the UI
            # Declaring variables with data input by the user in the boxes
            category = self.home_ui.SC_stockCatEbox.toPlainText()
            displayOrder = self.home_ui.SC_spinBox.value()
            dataRetrieveDB.addStockCategory(category, displayOrder)
            
            self.load_stock_categories() # Refreshing values in the table to ensure parity with db
            self.SCaddMode()
            self.load_stock_items() # Refreshing the data in the comboBox for Categories (in the StockItems tab)
        except:
            self.input_error_msg()

    def SIaddMode(self):
        '''
        Stock Items:
        Setting up the environment for the 'Add' mode where the user can create records for the stock categories
        '''
        # Changing mode by hiding specific buttons
        self.home_ui.SI_addBtn1.setHidden(False)
        self.home_ui.SI_deleteBtn1.setHidden(True)
        self.home_ui.SI_updateBtn1.setHidden(True)

        # Setting up the default values
        self.home_ui.SI_idEbox.setPlainText(str(dataRetrieveDB.getCurrentId(type='SI') + 1)) # This logic won't work if values get deleted as there will be repeating id's
        self.home_ui.SI_itemNameEbox.setPlainText("")
        self.home_ui.SI_itemUnitEbox.setPlainText("")
        self.home_ui.SI_itemPriceEbox.setPlainText("")
        self.home_ui.SI_categoryCbox.setCurrentText("Category Select") 
        self.home_ui.SI_availCbox.setCurrentText("Availability Select")
        self.home_ui.SI_addInfoEbox.setPlainText("")

    def SItableSelect(self,row):
        '''
        Stock Items:
        Setting up the environment for the 'Edit' mode and populating the edit boxes (and other input methods in the screen)
        with the information from the record that was selected by the user clicking on it 
        '''
        # Changing mode by hiding specific buttons
        self.home_ui.SI_addBtn1.setHidden(True)
        self.home_ui.SI_deleteBtn1.setHidden(False)
        self.home_ui.SI_updateBtn1.setHidden(False)

        # Declaring variables with row data
        id = self.home_ui.SI_table.item(row,0).text()
        item_name = self.home_ui.SI_table.item(row,1).text()
        item_unit = self.home_ui.SI_table.item(row,2).text()
        item_price = self.home_ui.SI_table.item(row,3).text()
        category = self.home_ui.SI_table.item(row,4).text()
        availability = self.home_ui.SI_table.item(row,5).text()
        addtl_info = self.home_ui.SI_table.item(row,6).text()

        # Showing data in edit boxes (etc) at the bottom
        self.home_ui.SI_idEbox.setPlainText(id)
        self.home_ui.SI_itemNameEbox.setPlainText(item_name)
        self.home_ui.SI_itemUnitEbox.setPlainText(item_unit)
        self.home_ui.SI_itemPriceEbox.setPlainText(item_price)
        self.home_ui.SI_categoryCbox.setCurrentText(category)
        self.home_ui.SI_availCbox.setCurrentText( "Available" if availability == 'Y' else 'Not Available') # the data is stored raw as 'Y' and 'N'
        self.home_ui.SI_addInfoEbox.setPlainText(addtl_info)

    def SIdeleteItem(self):
        '''
        Stock Items:
        Calling the deleteStockCategory function from our SQL connectivity layer to delete the record selected by the user
        '''
        id = self.home_ui.SI_idEbox.toPlainText()
        dataRetrieveDB.deleteStockItem(id)
        self.load_stock_items() # Refreshing the items in the table 
        self.SIaddMode()

    def SIupdateItem(self):
        '''
        Stock Items:
        Calling the updateStockCategory function from our SQL connectivity layer to update the record selected by the user with the information changed on the 
        edit boxes or combo boxes
        '''
        try: # To catch errors interacting with the database without breaking the UI
            id = self.home_ui.SI_idEbox.toPlainText()
            item_name = self.home_ui.SI_itemNameEbox.toPlainText()
            item_unit = self.home_ui.SI_itemUnitEbox.toPlainText()
            item_price = self.home_ui.SI_itemPriceEbox.toPlainText()
            categoryid = dataRetrieveDB.getCategoryId(self.home_ui.SI_categoryCbox.currentText()) # Due to manipulation we have to get the id from the category name
            availability = 'Y' if self.home_ui.SI_availCbox.currentText() == 'Available' else 'N'
            addtl_info = self.home_ui.SI_addInfoEbox.toPlainText()

            # Using SQL connectivity layer function to update the record
            dataRetrieveDB.updateStockItem(id, item_name, item_unit, item_price, categoryid, availability, addtl_info)
            self.load_stock_items() # Refreshing the items in the table
        except:
            self.input_error_msg()
        
    def SIaddItem(self):
        '''
        Stock Items:
        Calling the addStockCategory function from our SQL connectivity layer to create a record with the information entered on the 
        edit boxes or spin box by the user (the id is automatically generated for data integrity)
        '''
        try: # To catch errors interacting with the database without breaking the UI
            item_name = self.home_ui.SI_itemNameEbox.toPlainText()
            item_unit = self.home_ui.SI_itemUnitEbox.toPlainText()
            item_price = self.home_ui.SI_itemPriceEbox.toPlainText()
            categoryid = dataRetrieveDB.getCategoryId(self.home_ui.SI_categoryCbox.currentText()) # Due to manipulation we have to get the id from the category name
            availability = 'Y' if self.home_ui.SI_availCbox.currentText() == 'Available' else 'N'
            addtl_info = self.home_ui.SI_addInfoEbox.toPlainText()

            # Using SQL connectivity layer function to add the record
            dataRetrieveDB.addStockItem(item_name, item_unit, item_price, categoryid, availability, addtl_info)
            self.load_stock_items() # Refreshing the items in the table
            self.SIaddMode()
        except:
            self.input_error_msg()
    
    def input_error_msg(self):
        '''
        This function displays an error message whenever the user tries to operate the database in a way that is invalid/raises an error.
        '''
        message = QMessageBox()
        message.setText("Cannot complete database operation.")
        message.setIcon(QMessageBox.Critical)
        message.setWindowTitle("Invalid input")
        message.setInformativeText("Please make sure you fill all the relevant values and that they are valid.")
        message.exec_()
    
    def login(self):
        """
        User authenticates against the database. Uses the functions from the SQL Connection Layer to validate the credentials.
        """
        # Using the SQL Connectivity Layer functions to check if the user exists in the database 
        # and check whether their password is correct.
        if dataRetrieveDB.checkUser(self.login_ui.editboxUsr.text()) and dataRetrieveDB.checkPassword(self.login_ui.editboxUsr.text(), self.login_ui.editboxPass.text()):
            # Displays message response to user to know they are now logged in
            message = QMessageBox()
            message.setText("Logged in.")
            message.setIcon(QMessageBox.Information)
            message.setWindowTitle(' ')
            message.exec_()

            # Once authenticated we hide the login screen and call the show home screen function
            self.loginScr.hide()
            self.show_home_screen()
        else:
            # Displays message response to user to know that the credentials were invalid
            message = QMessageBox()
            message.setText("Please check your username and password.")
            message.setIcon(QMessageBox.Critical)
            message.setWindowTitle("Login Unsuccesful")
            message.setInformativeText("Try again.")
            message.exec_()

    def load_stock_items(self):
        '''
        Gets the records for StockItems in the database and puts the values into the table to display to the user.
        '''

        # Getting a list of our stock items
        stock_items = dataRetrieveDB.getStockItems()
        
        # Setup drop down to select category
        self.home_ui.SI_categoryCbox.clear()
        self.home_ui.SI_categoryCbox.addItem("Category Select") # Adding the default value
        stock_categories = dataRetrieveDB.getStockCategories() 
        for i in stock_categories:
            self.home_ui.SI_categoryCbox.addItem(i["stockcategory"])
            
        # Loading Stock item data into the Stock Items table
        row = 0
        self.home_ui.SI_table.setRowCount(len(stock_items))
        for item in stock_items: # Inserting them into our QTableWidget with a grid-like structure
            self.home_ui.SI_table.setItem(row, 0,  QTableWidgetItem(str(item['id'])))
            self.home_ui.SI_table.setItem(row, 1,  QTableWidgetItem(item['itemname']))
            self.home_ui.SI_table.setItem(row, 2,  QTableWidgetItem(item['itemunit']))

            price = format(float(item['itemprice']), ',.2f') # Formatting itemprice to follow currency format
            self.home_ui.SI_table.setItem(row, 3,  QTableWidgetItem( str(price) ) )

            self.home_ui.SI_table.setItem(row, 4,  QTableWidgetItem(item['stockcategory']))
            self.home_ui.SI_table.setItem(row, 5,  QTableWidgetItem(item['available']))
            self.home_ui.SI_table.setItem(row, 6,  QTableWidgetItem(item['itemaddlinfo']))
            row += 1
        
        # Hiding availability and additional info columns as instructed in requirements
        self.home_ui.SI_table.hideColumn(5)
        self.home_ui.SI_table.hideColumn(6)
    
    def load_stock_categories(self):
        '''
        Gets the records for StockCategory in the database and puts the values into the table to display to the user.
        '''
        # Stock categories
        stock_categories = dataRetrieveDB.getStockCategories()
        row = 0
        self.home_ui.SC_table.setRowCount(len(stock_categories))
        for item in stock_categories: # Inserting them into our QTableWidget with a grid-like structure
            self.home_ui.SC_table.setItem(row, 0,  QTableWidgetItem(str(item['id'])))
            self.home_ui.SC_table.setItem(row, 1,  QTableWidgetItem(item['stockcategory']))
            self.home_ui.SC_table.setItem(row, 2,  QTableWidgetItem(str(item['displayorder'])))
            row += 1

if __name__ == "__main__":
    '''
    Connecting to DB and initialising the application with a call to our PyQt5Widget
    '''

    # SQL Connection values - Change here if connecting to a remote database, etc
    server = 0 # Enter 0 for default value or enter actual server name as a string like 'DESKTOP-****\SQLEXPRESS'
    database = "nfhcw2"
    uid = "nfhuser" # User to access the database
    pwd = "nfhuserpwd" # Password to access the database

    try:
        dataRetrieveDB.connectToDB(server, database,uid,pwd) # Connect to the database before user attempts to log in
        app = QApplication([])
        window = MainWindow()
        app.exec()
    except:
        print("Login to database failed, please make sure the database is connected properly")
