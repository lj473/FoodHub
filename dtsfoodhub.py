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
        self.login_ui.editboxUsr.setText('nfhtest') # ONLY FOR TESTING
        self.login_ui.editboxPass.setText('nfhtestpwd') # ONLY FOR TESTING

        # On click for the "confirm" button -> call the login func to authenticate with DB
        self.login_ui.btnConfim.clicked.connect(self.login)
        self.login_ui.btnClear.clicked.connect(self.loginScr.close)

    def show_home_screen(self):
        """
        Display the home page.
        Currently the code will fail due to homeScr.py line 394, 
        (if you temporarily remove that line from homeScr.py the code will work)
        """
        # Once we are logged in we can show the Home Screen
        self.homeScr = QWidget() 
        self.home_ui = Ui_homeScr() # From Qt Designer
        self.home_ui.setupUi(self.homeScr)

        # Setting up Stock Categories tab and assigning slots to signals
        self.home_ui.SC_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.home_ui.SC_table.cellClicked.connect(self.SCtableSelect)
        self.home_ui.SC_plusBtn.clicked.connect(self.SCaddMode)

        self.home_ui.SC_addBtn.setHidden(True)
        self.home_ui.SC_deleteBtn.setHidden(True)
        self.home_ui.SC_updateBtn.setHidden(True)

        self.home_ui.SC_deleteBtn.clicked.connect(self.SCdeleteCategory)
        self.home_ui.SC_updateBtn.clicked.connect(self.SCupdateCategory)
        self.home_ui.SC_addBtn.clicked.connect(self.SCaddCategory)

        self.home_ui.SC_cancelBtn.clicked.connect(self.homeScr.close)

        # Setting up Stock Items tab and assigning slots to signals
        self.home_ui.SI_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.home_ui.SI_table.cellClicked.connect(self.SItableSelect)
        self.home_ui.SI_plusBtn1.clicked.connect(self.SIaddMode)
        self.home_ui.SI_addBtn1.setHidden(True)
        self.home_ui.SI_deleteBtn1.setHidden(True)
        self.home_ui.SI_updateBtn1.setHidden(True)

        self.home_ui.SI_deleteBtn1.clicked.connect(self.SIdeleteItem)
        self.home_ui.SI_updateBtn1.clicked.connect(self.SIupdateItem)
        self.home_ui.SI_addBtn1.clicked.connect(self.SIaddItem)

        self.home_ui.SI_cancelBtn1.clicked.connect(self.homeScr.close)

        # Loading our data unto the Stock Category and Item tables
        self.load_stock_categories() 
        self.load_stock_items() 

        self.homeScr.show()
    
    def SCaddMode(self):
        # Changing mode by hiding specific buttons
        self.home_ui.SC_addBtn.setHidden(False)
        self.home_ui.SC_deleteBtn.setHidden(True)
        self.home_ui.SC_updateBtn.setHidden(True)
        
        # Setting up the default values
        self.home_ui.SC_IdEbox.setPlainText(str(dataRetrieveDB.getNextId(type='SC') + 1)) # This logic won't work if values get deleted as there will be repeating id's
        self.home_ui.SC_stockCatEbox.setPlainText("")
        self.home_ui.SC_spinBox.setValue(0)
    
    def SCtableSelect(self,row):
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
        id = self.home_ui.SC_IdEbox.toPlainText()
        dataRetrieveDB.deleteStockCategory(id)
        self.load_stock_categories() # Refreshing values in the table to ensure parity with db
        self.load_stock_items() 

    def SCupdateCategory(self):
        id = self.home_ui.SC_IdEbox.toPlainText()
        category = self.home_ui.SC_stockCatEbox.toPlainText()
        displayOrder = self.home_ui.SC_spinBox.value()
        dataRetrieveDB.updateStockCategory(id, category, displayOrder)
        self.load_stock_categories() # Refreshing values in the table to ensure parity with db
        self.load_stock_items()

    def SCaddCategory(self):
        category = self.home_ui.SC_stockCatEbox.toPlainText()
        displayOrder = self.home_ui.SC_spinBox.value()
        dataRetrieveDB.addStockCategory(category, displayOrder)
        self.load_stock_categories() # Refreshing values in the table to ensure parity with db
        self.SCaddMode()
        self.load_stock_items()

    def SIaddMode(self):
        # Changing mode by hiding specific buttons
        self.home_ui.SI_addBtn1.setHidden(False)
        self.home_ui.SI_deleteBtn1.setHidden(True)
        self.home_ui.SI_updateBtn1.setHidden(True)

        # Setting up the default values
        self.home_ui.SI_idEbox.setPlainText(str(dataRetrieveDB.getNextId(type='SI') + 1)) # This logic won't work if values get deleted as there will be repeating id's
        self.home_ui.SI_itemNameEbox.setPlainText("")
        self.home_ui.SI_itemUnitEbox.setPlainText("")
        self.home_ui.SI_itemPriceEbox.setPlainText("")
        self.home_ui.SI_categoryCbox.setCurrentText("Category Select") 
        self.home_ui.SI_availCbox.setCurrentText("Availability Select")
        self.home_ui.SI_addInfoEbox.setPlainText("")

    def SItableSelect(self,row):
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
        self.home_ui.SI_availCbox.setCurrentText( "Available" if availability == 'Y' else 'Not Available') # how to edit Cbox
        self.home_ui.SI_addInfoEbox.setPlainText(addtl_info)

    def SIdeleteItem(self):
        id = self.home_ui.SI_idEbox.toPlainText()
        dataRetrieveDB.deleteStockItem(id)

    def SIupdateItem(self):
        id = self.home_ui.SI_idEbox.toPlainText()
        item_name = self.home_ui.SI_itemNameEbox.toPlainText()
        item_unit = self.home_ui.SI_itemUnitEbox.toPlainText()
        item_price = self.home_ui.SI_itemPriceEbox.toPlainText()
        categoryid = dataRetrieveDB.getCategoryId(self.home_ui.SI_categoryCbox.currentText())
        availability = 'Y' if self.home_ui.SI_availCbox.currentText() == 'Available' else 'N'
        addtl_info = self.home_ui.SI_addInfoEbox.toPlainText()

        # Category as ID and not name 
        dataRetrieveDB.updateStockItem(id, item_name, item_unit, item_price, categoryid, availability, addtl_info)

    def SIaddItem(self):
        id = self.home_ui.SI_idEbox.toPlainText()
        item_name = self.home_ui.SI_itemNameEbox.toPlainText()
        item_unit = self.home_ui.SI_itemUnitEbox.toPlainText()
        item_price = self.home_ui.SI_itemPriceEbox.toPlainText()
        categoryid = dataRetrieveDB.getCategoryId(self.home_ui.SI_categoryCbox.currentText())
        availability = 'Y' if self.home_ui.SI_availCbox.currentText() == 'Available' else 'N'
        addtl_info = self.home_ui.SI_addInfoEbox.toPlainText()

        # Category as ID and not name 
        dataRetrieveDB.addStockItem(id, item_name, item_unit, item_price, categoryid, availability, addtl_info)
    
    def login(self):
        """
        User authenticates against the database. Uses the functions from the SQL Connection Layer.
        """

        # Using the SQL Connectivity Layer functions to check if the user exists in the database 
        # and check whether their password is correct.
        if dataRetrieveDB.checkUser(self.login_ui.editboxUsr.text()) and dataRetrieveDB.checkPassword(self.login_ui.editboxUsr.text(), self.login_ui.editboxPass.text()):
            message = QMessageBox()
            message.setText("Logged in.")
            message.setIcon(QMessageBox.Information)
            message.setWindowTitle(' ')
            message.exec_()
            # Once authenticated we hide the login screen and call the show home screen function
            self.loginScr.hide()
            self.show_home_screen()
        else:
            message = QMessageBox()
            message.setText("Please check your username and password.")
            message.setIcon(QMessageBox.Critical)
            message.setWindowTitle("Login Unsuccesful")
            message.setInformativeText("Try again.")
            message.exec_()

    def load_stock_items(self):
        # Stock items
        stock_items = dataRetrieveDB.getStockItems()
        
        # Setup drop down to select category
        self.home_ui.SI_categoryCbox.clear()
        self.home_ui.SI_categoryCbox.addItem("Category Select") # Default
        stock_categories = dataRetrieveDB.getStockCategories() 
        for i in stock_categories:
            self.home_ui.SI_categoryCbox.addItem(i["stockcategory"])
            
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
    
    def load_stock_categories(self):
        # Stock categories
        stock_categories = dataRetrieveDB.getStockCategories()
        row = 0
        self.home_ui.SC_table.setRowCount(len(stock_categories))
        for item in stock_categories: # Inserting them into our QTableWidget with a grid-like structure
            self.home_ui.SC_table.setItem(row, 0,  QTableWidgetItem(str(item['id'])))
            self.home_ui.SC_table.setItem(row, 1,  QTableWidgetItem(item['stockcategory']))
            self.home_ui.SC_table.setItem(row, 2,  QTableWidgetItem(str(item['displayorder'])))
            row += 1

def main():
    dataRetrieveDB.connectToDB() # Connect to the database before user attempts to log in
    app = QApplication([])
    window = MainWindow()
    app.exec()

main()
