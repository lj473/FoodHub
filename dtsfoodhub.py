# Created by 720018271 on 10/03/2023 for dtsfoodhub
# Updated by 720085401 on 13/03/2023 for dtsfoodhub

from PyQt5.QtWidgets import *
import dataRetrieveDB
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

        

        # on click for the "confirm" button -> call the login func to authenticate with DB
        self.login_ui.btnConfim.clicked.connect(self.login)

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

        # Change this later so that it only loads the items when the user is in the selected tab
        self.load_stock_categories() 
        self.load_stock_items() 

        self.homeScr.show()
    
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
