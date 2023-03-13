# Created by 720018271 on 10/03/2023 for dtsfoodhub
# Updated by 720085401 on 13/03/2023 for dtsfoodhub

from PyQt5.QtWidgets import *
import dataRetrieveDB
from loginScr import Ui_loginScr # Import login screen class from Qt
from homeScr import Ui_homeScr # Import home screen class from Qt

# print(dataRetrieveDB.DBTest()) #Testing only

'''
For login screen:
- Use dataRetrieveDB.checkUser() first to see if entered UserName exists
- Then use dataRetrieveDB.checkPassword() to see if password entered matches the one in the DB
'''

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
        self.ui = Ui_loginScr() # From Qt Designer
        self.ui.setupUi(self.loginScr)
        self.loginScr.show()

        dataRetrieveDB.connectToDB() # Connect to the database before user attempts to log in

        # on click for the "confirm" button -> call the login func to authenticate with DB
        self.ui.btnConfim.clicked.connect(self.login)

    def show_home_screen(self):
        """
        Display the home page.
        Currently the code will fail due to homeScr.py line 397, 
        (if you temporarily remove that line from homeScr.py the code will work)
        """
        # Once we are logged in we can show the Home Screen
        self.homeScr = QWidget() 
        self.ui = Ui_homeScr() # From Qt Designer
        self.ui.setupUi(self.homeScr)
        self.homeScr.show()
    
    def login(self):
        """
        User authenticates against the database. Uses the functions from the SQL Connection Layer.
        """

        # Using the SQL Connectivity Layer functions to check if the user exists in the database 
        # and check whether their password is correct.
        if dataRetrieveDB.checkUser(self.ui.editboxUsr.text()) and dataRetrieveDB.checkPassword(self.ui.editboxUsr.text(), self.ui.editboxPass.text()):
            message = QMessageBox()
            message.setText("Logged in.")
            message.exec_()
            # Once authenticated we hide the login screen and call the show home screen function
            self.loginScr.hide()
            self.show_home_screen()
        else:
            message = QMessageBox()
            message.setText("Invalid Login.")
            message.exec_()

def main():
    app = QApplication([])
    window = MainWindow()
    app.exec()

main()
