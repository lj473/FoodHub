# Created by 720085401 on 13/03/2023 for dtsfoodhub

class dbinfo :          # Setting variables to be used by the other application components
    database_name = 'nfhcw2'
    db_server = '\SQLEXPRESS'
    adminuser = 'hrtest'
    adminpwd = 'hrtest'
    connection_count = 0 # Used to count the number of connections to the database
    loggedin = False
