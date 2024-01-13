from App import App

class Database:
  def __init__(self):
    self.__number_of_apps = 25
    self.__apps = [[App("Facebook", "Social", "Meta Platforms Inc", "Connect with your loved ones", "12+", "Free"), 
                    App("WhatsApp", "Social", "WhatsApp Inc", "Privately message and call", "12+", "Free"),
                    App("BeReal", "Social", "BeReal Inc", "Be your true self", "12+", "Free"),
                    App("Discord", "Social", "Discord Inc", "Group Chat, Friends & Gaming", "17+", "Free"),
                    App("Instagram", "Social", "Instagram Inc", "Share your stories with others", "12+", "Free")],
                   [App("Google", "Productivity", "Google LLC", "Ask Google anything", "17+", "Free"),
                    App("Microsoft Word", "Productivity", "Microsoft Corp.", "Create and design documents", "4+", "Free"),
                    App("Gmail", "Productivity", "Google LLC", "Secure, fast & organized email", "4+", "Free"),
                    App("Shift Worker", "Productivity", "Seekr Tech", "Shift management made simple", "4+", "$5.49"),
                    App("Notion", "Productivity", "Notion Labs", "The all-in-one workspace", "4+", "Free")],
                   [App("Google Classroom", "Education", "Google LLC", "Instant. Paperless. Easy", "4+", "Free"),
                    App("Duolingo", "Education", "Duolingo Inc", "Learn any language you want", "4+", "Free"),
                    App("Photomath", "Education", "Photomath Inc", "Math explained step-by-step", "4+", "Free"),
                    App("Kahoot", "Education", "Kahoot ASA", "Learn at school, home or work", "4+", "Free"),
                    App("Brightspace Pulse", "Education", "D2L Corp.", "Education workspace for students", "4+", "Free")],
                   [App("Minecraft", "Games", "Mojang", "Create, explore and survive!", "9+", "$9.99"),
                    App("Chess", "Games", "Chess.com", "PLay with friends", "4+", "Free"),
                    App("Call of Duty", "Games", "Activision", "Multiplayer, FPS, shooter", "17+", "Free"),
                    App("Subway Surfers", "Games", "Sybo Games", "Join the endless running fun!", "9+", "Free"),
                    App("Among Us", "Games", "InnerSloth LLC", "Find the imposter", "9+", "Free")],
                    [App("Calculator", "Utilities", "Apple", "Calculate anything", "4+", "Free"), 
                     App("Camera", "Utilities", "Apple", "Capture memories", "4+", "Free"),
                     App("Alarmy", "Utilities", "Meta Platforms Inc", "Wake up on time", "4+", "$3.99"),
                   App("Compass", "Utilities", "Apple", "Find the correct direction", "4+", "Free"),
                   App("Voice Memos", "Utilities", "Apple", "Record", "4+", "Free"),]]

  #acessors
  def get_app(self):
    return self.__apps
  def get_number_of_apps(self):
    return self.__number_of_apps

  # find's app's category's index
  def find_category_index(self, app):
    for i in range (5): 
      if app in self.__apps[i]:
        return i+1

  # finds app's index
  def find_index(self, app):
    x = self.find_category_index(app)-1
    return self.__apps[x].index(app)+1

  # get app object given index
  def get_app_info(self, category, app):
    return self.__apps[category-1][app-1]

  # get app object given name
  def find_app(self,app_name):
    for category in self.__apps:
      for apps in category:
        if app_name == apps.get_name():
          return apps
    
  #prints app categories
  def print_categories(self, category):
    i = 1
    for apps in self.__apps[category-1]:
        print(f"{i}: {apps.get_name()}")
        i += 1
    print(f"{i}: Go back")
    return i

  # prints app names in alphabetical order
  def print_app_name(self):
    print("\nApp Names: (alphabetical order)")
    i=1
    app_list = []
    for categories in self.__apps:
      for apps in categories:
        app_list.append(apps.get_name())
    #sorting algorithm
    def selectionSort(array, size):
      for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
          if array[i] < array[min_idx]:
            min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
    selectionSort(app_list, len(app_list))
    for apps in app_list:
      print(f"{i}: {apps}")
      i += 1
    print("")

  # prints top 10 apps
  def top_apps(self):
    ratings_dict = {}
    for categories in self.__apps:
      for app in categories:
        ratings_dict[app.get_name()] = app.average_star()
    sorted_ratings_dict = dict(sorted(ratings_dict.items(), key=lambda x:x[1], reverse=True))
    top_10 = (list(sorted_ratings_dict.keys()))[:10]
    print("-----------------------------------------\nTop 10 Apps Trending Today: \n")
    i = 1
    for apps in top_10:
      avg_star = "["+ str(self.find_app(apps).average_star()) + "]"
      str_i= str(i) + ":"
      print(f"{str_i:<3} {apps:<20} {avg_star:>10}")
      i += 1

  # adds app  
  def add_app(self, name, category, creator, description, age, price):
    if category == 1: category_str = "Social"
    if category == 2: category_str = "Productivity"
    if category == 3: category_str = "Education"
    if category == 4: category_str = "Games"
    if category == 5: category_str = "Utilities"
    app = App(name, category_str, creator, description, age, price)
    self.__apps[category-1].append(app)
    self.__number_of_apps =+ 1
    
  # adds app reviews from text file
  def add_existing_reviews(self, inputsource):
    file = open(inputsource, "r")
    rawdata = file.read()
    lines = rawdata.splitlines()
    for y in range (5):
      for x in range (5):
        for ratings in range (4):
          name = lines.pop(0)
          title = lines.pop(0)
          stars = int(lines.pop(0))
          comment = lines.pop(0)
          feedback = lines.pop(0)
          self.__apps[y][x].get_rating().add_rating(name, title, stars, comment)
          self.__apps[y][x].get_rating().add_feedback(name, title, stars, comment, feedback)