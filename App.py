from RatingDatabase import RatingDatabase

class App:
  def __init__(self, name, category, creator, description, age, price):
    self.__name = name
    self.__category = category
    self.__creator = creator
    self.__description = description
    self.__age = age
    self.__price = price
    self.__ratings = RatingDatabase(name)

  # accessors
  def get_name(self):
    return self.__name
  def get_category(self):
    return self.__category
  def get_creator(self):
    return self.__creator
  def get__description(self):
    return self.__description
  def get__age(self):
    return self.__age
  def get_price(self):
    return self.__price
  def get_rating(self):
    return self.__ratings

  # returns average stars of app
  def average_star(self):
    return round(self.__ratings.average_stars(), 2)
  
  # prints app info
  def __str__(self):
    return f"Name: {self.__name} \nAverage Stars: {round(self.average_star(),2)} \nCategory: {self.__category} \nCreator: {self.__creator} \nDescription: {self.__description} \nAge: {self.__age} \nPrice: {self.__price}"