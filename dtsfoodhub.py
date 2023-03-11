# Created by 720018271 on 10/03/2023 for dtsfoodhub

import dataRetrieveDB

dataRetrieveDB.connectToDB() #Setup connection to database

print(dataRetrieveDB.DBTest()) #Testing only

'''
For login screen:
- Use dataRetrieveDB.checkUser() first to see if entered UserName exists
- Then use dataRetrieveDB.checkPassword() to see if password entered matches the one in the DB
'''