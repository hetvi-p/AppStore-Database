from Ratings import Ratings
from Feedback import Feedback

class RatingDatabase:
  def __init__(self, name):
    self.__name = name
    self.__ratings = []
    self.__feedback = []
    self.__number_of_ratings = 0

  # acessors
  def get_name(self):
    return self.__name
  def get_ratings(self):
    return self.__ratings
  def get_feedback(self):
    return self.__feedback
  def get_number(self):
    return self.__number_of_ratings

  # add rating
  def add_rating(self, app, title, stars, comment):
    rating = Ratings(app, title, stars, comment)
    self.__ratings.append(rating)
    self.__number_of_ratings += 1

  # add feedback
  def add_feedback(self, app, title, stars, comment, feedback):
    feedback = Feedback(app, title, stars, comment, feedback)
    self.__feedback.append(feedback)

  # edit rating
  def edit_rating(self, rating, new_title, new_stars, new_comment):
    for ratings in self.__ratings:
      if ratings == rating:
        ratings.title = new_title
        ratings.stars = new_stars
        ratings.comment = new_comment

  # caluclates average star from ratings
  def average_stars(self):
    if self.__number_of_ratings == 0:
      return 0
    total_stars = 0
    for ratings in self.__ratings:
      total_stars += ratings.stars
    return (total_stars/self.__number_of_ratings)

  # prints ratings
  def print_ratings(self):
    for rating in self.__ratings:
      print(rating)

  #prints feedback
  def print_feedback(self):
    for feedback in self.__feedback:
      print(feedback)