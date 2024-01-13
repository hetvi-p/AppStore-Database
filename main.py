from QuestionMethods import QuestionMethods
from Database import Database
from Login import Login

# Database/Login/QuestionMethod objects initalized
database = Database()
database.add_existing_reviews('existing_reviews.txt')
login = Login(database)
system = QuestionMethods()

# main method (imported from QuestionMethods)
system.main(database, login)