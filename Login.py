from Users import Users

class Login:
  def __init__(self, database):
    self.__database = database
    self.__admin_login = "admin"
    self.__admin_password = "password"
    self.__app_login = {"Google":"password", "Facebook":"password", "WhatsApp":"password"}
    self.__stored_info = {"h":"p", "a":"b", "c":"d"}
    self.__users = [Users("Hetvi","h","p"),Users("John","a","b"), Users("Jake","c","d") ]
  
  # log-in method
  def login(self):
    print("Welcome to Appster! Please login below:\n")
    username = input("Username: ")
    password = input("Password: ")
    # log into admin account
    if username == self.__admin_login and password == self.__admin_password:
      return self.signup() 
    # log into app developer account
    elif (username, password) in self.__app_login.items():
      self.app_acc(username)
      return 3 
    # log into user account
    elif (username, password) in self.__stored_info.items():
      for users in self.__users:
        if username == users.get_username():
          print(f"------------------------------------------\nWelcome to your account {users.get_name()}!")
          return users #returns user object
    # wrong username/password
    else: 
      print("Login information incorrect. Please try again!\n")
      return 2 #login screen

  # sign up method
  def signup(self):
    print("\nHello Admin!")
    register = int(input("Would you like to register a new user? \n1: Yes \n2: No \n"))
    # add user
    if register == 1:
      name = input("\nEnter name: ")
      username = input("Enter new username: ")
      password = input("Enter new password: ")
      self.__stored_info[username] = password 
      self.__users.append(Users(name, username, password))
      print("Account Created Successfully! :P")
      y = int(input("\nPlease pick from below: \n1: Continue to your account \n2: Log-out\n"))
      print("")
      return y #1: continue to admin account; 2: log-out 
    else:
      return 1 #continue to admin account

  # app developer account 
  def app_acc(self, username):
    print("\nWelcome to your app account! \nHere are the feedback recieved from users to improve your app:")
    self.__database.find_app(username).get_rating().print_feedback()
    input("\nTo directly contact users of these ratings, please let admin know. If any questions persist, please contact admin. \n\nPress Enter to log-out: ")
    print(f"\n{dash}")
    
  # view list of all users
  def view_users(self):
    print("\nThese are the current users: ")
    i = 1
    for users in self.__users:
      print(f"\n{i}: \nName: {users.get_name()} \nUsername: {users.get_username()} \nPassword: {users.get_password()} ")
      i += 1

  # edit user info
  def edit_users(self, number, new_name, new_username, new_password):
    user = self.__users[number-1]
    del self.__stored_info[user.get_username()] 
    self.__stored_info[new_username] = new_password
    user.edit_info(new_name, new_username, new_password)
    print("User Information Updated!\n")

  # view amount of users
  def getLoginUsers(self):
    return len(self.__users)