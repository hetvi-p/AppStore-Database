from Ratings import Ratings

class Users:
  def __init__(self, name, username, password):
    self.__name = name
    self.__username = username
    self.__password = password
    self.__ratings = []
    self.__number_of_ratings = 0

  # accessors
  def get_name(self):
    return self.__name
  def get_username(self):
    return self.__username
  def get_password(self):
    return self.__password
  def get_ratings(self):
    return self.__ratings
  def get_number_of_ratings(self):
    return self.__number_of_ratings

  # add rating to user's database
  def add_rating(self, app, title, stars, comment):
    rating = Ratings(app, title, stars, comment)
    self.__ratings.append(rating)
    self.__number_of_ratings += 1

  # finds ratings based on index
  def find_rating(self, number):
    rating = self.__ratings[number-1]
    return rating 

  # edit rating
  def edit_rating(self, number, new_title, new_stars, new_comment):
    rating = self.__ratings[number-1]
    rating.title = new_title
    rating.stars = new_stars
    rating.comment = new_comment

  # edit user info
  def edit_info(self, new_name, new_username, new_password):
    self.__name = new_name
    self.__username = new_username
    self.__password = new_password

  # prints user's previous ratings
  def print_ratings(self):
    if self.__number_of_ratings == 0: 
      print("You have no ratings yet!")
      return 0
    i=1
    print("These are your previous ratings:\n")
    for rating in self.__ratings:
      print(f"{i}: {rating}")
      i += 1