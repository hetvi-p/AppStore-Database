import random

class QuestionMethods: 
  
  dash = "------------------------------------------"

  # pick selection
  def question1(self, y, database, login):
    try:
      input1 = int(input("\nWould you like to: \n1: Rate apps \n2: Check top apps \n3: Check previous ratings \n4: Log-out \n"))
      #rate apps
      if input1 == 1:
        self.question2(y, database, login)
      # check top apps
      elif input1 == 2:
        database.top_apps()
        input("\nPress Enter to go back: ")
        print(QuestionMethods.dash)
        self.question1(y, database, login)
      # check previous ratings
      elif input1 == 3:
        print(QuestionMethods.dash)
        y.print_ratings()
        input2 = int(input("\nTo go back, enter 0 or, \nTo edit any ratings, enter number: \n")) 
        # go back to question 1
        if input2 == 0: 
          print(QuestionMethods.dash)
          self.question1(y, database, login)
        # edit rating
        try: 
          def edit_rating():
            if input2 != 0:
              new_star = int(input("\nEnter new stars: "))
              new_title = input("Enter new title: ")
              new_comment = input("Enter new comment: ")
              unmodified_rating = y.find_rating(input2)
              database.find_app(unmodified_rating.get_app()).get_rating().edit_rating(unmodified_rating, new_title, new_star, new_comment)
              y.edit_rating(input2, new_title, new_star, new_comment)
              input(("Rating Updated! \n\nTo go back, press Enter"))
              print(QuestionMethods.dash)
              self.question1(y,database, login)
              edit_rating()
        except: #invalid input
          print("Invalid Input -- Please try again.")
          edit_rating()
      # log-out
      elif input1 == 4:
        print(QuestionMethods.dash)
        self.main(database, login)
      # invalid input
      else: 
        print("Invalid Input -- Please try again.")
        self.question1(y, database, login)
    # invalid input
    except: 
      print("Invalid Input -- Please try again.")
      self.question1(y, database, login)
      

  # pick category
  def question2(self, y, database, login):
    try: 
      input2 = int(input("\nPlease pick from the categories below: \n1: Social \n2: Productivity \n3: Education \n4: Games \n5: Utilities \n6: Search for app \n7: Go back \n"))
      # search for apps
      if input2 == 6:
        input3 = input("\nSearch for app: ")
        if database.find_app(input3) == None: # invalid input
          input("App not found. \n\nPress Enter to go back: ")
          self.question2(y, database, login)
        else: 
          self.question4(database.find_app(input3), y, database.find_category_index(database.find_app(input3)), database.find_index(database.find_app(input3)), database, login)
      # go back
      elif input2 == 7:
        self.question1(y, database, login)
      # selection of category
      elif input2 > 0 and input2 < 6:  
        self.question3(y, input2, database, login)
      # invalid input
      else:
        print("Invalid Input -- Please try again.")
        self.question2(y, database, login)
    # invalid input
    except:
      print("Invalid Input -- Please try again.")
      self.question2(y, database, login)

      
  # pick an app from category
  def question3(self, y, category, database, login):
    try:
      print("\nPlease pick an app from below:")
      i = database.print_categories(category)
      input3 = int(input())
      # show app info
      if input3 < i:
        self.question4(database.get_app_info(category, input3), y, category, input3, database, login)
      # go back
      elif input3 == i:
        self.question2(y, database, login)
      # invalid input
      else: 
        print("Invalid Input -- Please try again.")
        self.question3(y, category, database, login)
    # invalid input
    except:
      print("Invalid Input -- Please try again.")
      self.question3(y, category, database, login)

      
  # show app info and ask to rate or view ratings
  def question4(self, app, y, category, index, database, login):
    try:
      print(QuestionMethods.dash)
      print(app)
      input4 = int(input("\nWould you like to: \n1: Rate this app \n2: View ratings \n3: Go back\n"))
      # rate app
      if input4 == 1:
        stars = int(input("\nStars out of /5?: "))
        # invalid input
        if stars < 1 or stars > 5:
          print("Invalid Input -- Please try again.")
          self.question4(app, y, category, index, database, login)
        title = input("Title: ")
        comments = input("Comments: ")
        feedback = input("Feedback to creator(optional): ")
        app.get_rating().add_rating(app.get_name(), title, stars, comments)
        if feedback != "": 
          app.get_rating().add_feedback(app.get_name(), title, stars, comments, feedback)
        y.add_rating(app.get_name(), title, stars, comments)
        print("Rating Submitted!")
        # reccomend app from same category
        x = True
        while x == True:
          rand_num = random.randint(0, len(database.get_app()[category])-1)
          if rand_num != index:
            x = False
        recom_app = database.get_app_info(category, rand_num)
        def reccomend_app():
          # ask to rate similar app or view app ratings
          input5 = int(input(f"\nWould you like to \n1: Rate a similar app  [{recom_app.get_name()}]\n2: View ratings \n3: Go back to home\n"))
          # rate similar app
          if input5 == 1: 
            self.question4(recom_app, y, category, index, database, login)
          # view ratings 
          if input5 == 2:
            self.question5(app, y, category, index, database, login)
          # go back home
          if input5 == 3:
            self.question1(y, database, login)
          # invalid input
          else: 
            print("Invalid Input -- Please try again.")
            reccomend_app()
        reccomend_app()
      # view ratings
      elif input4 == 2:
        self.question5(app, y, category, index, database, login)
      # Go back
      elif input4 == 3:
        self.question3(y, database.find_category_index(app), database, login)
      # invalid input
      else: 
        print("Invalid Input -- Please try again.")
        self.question4(app, y, category, index, database, login)
    # invalid input
    except:
      print("Invalid Input -- Please try again.")
      self.question4(app, y, category, index, database, login)


  # show ratings
  def question5(self, app, y, category, index, database, login):
    print(f"{QuestionMethods.dash}\n{app.get_name()} Ratings \nAverage Stars: {app.average_star()}")
    app.get_rating().print_ratings()
    input("Press Enter to go back: ")
    self.question4(app, y, category, index, database, login) 


  # admin account selection
  def selection1(self, database, login):
    try: 
      print(f"{QuestionMethods.dash}\nWelcome to your account Admin!")
      # ask for input
      input1 = int(input("\nPlease pick from the selection below: \n1: View and edit users \n2: View Apps \n3: Add Apps \n4: Log-out \n"))
      # view and edit users
      if input1 == 1:
        login.view_users()
        input2 = input("\nTo go back, press Enter or, \nTo edit any ratings, enter number: \n")
        # go back
        if not input2:
          self.selection1(database, login)
        elif int(input2) > login.getLoginUsers():
            print("No possible user\n")
            self.selection1(database, login)
        else:
          # edit user
          new_name = input("\nEnter new name: ")
          new_username = input("Enter new username: ")
          new_password = input("Enter new password: ")
          login.edit_users(int(input2), new_name, new_username, new_password)
          input("Press Enter to go back: ")
          self.selection1(database, login) 
      # view apps
      elif input1 == 2:
        database.print_app_name()
        input("Press Enter to go back: ")
        self.selection1(database, login)
      # add apps
      elif input1 == 3:
        name = input("\nPlease enter app name: ")
        category = int(input("App category: \n(1: Social) \n(2: Productivity) \n(3: Education) \n(4: Games) \n(5: Utilities)\n"))
        creator = input("App creator: ")
        description = input("App description: ")
        age = input("App age recommendation: ")
        price = input("Price: ")
        database.add_app(name, category, creator, description, age, price)
        print("App Created!\n")
        input("Press Enter to go back: ")
        self.selection1(database, login)
      # log-out
      elif input1 == 4:
        print(QuestionMethods.dash)
        self.main(database, login)
      # invalid input
      else:
        print("Invalid Input -- Please try again.")
        self.selection1(database, login)
    #invalid input
    except:
      print("Invalid Input -- Please try again.")
      self.selection1(database, login)

      
  # main
  def main(self, database, login):
    y = 2
    while y == 2:
      y = login.login()
    # continue to admin account
    if y == 1: 
      self.selection1(database, login)
    # continue to app developer account
    if y == 3:
      self.main(database, login)
    # continue to user account
    else: 
      self.question1(y, database, login)