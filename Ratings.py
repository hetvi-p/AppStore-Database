import emoji

class Ratings:
  def __init__(self, app, title, stars, comment): #superclass
    self.app = app
    self.title = title
    self.stars = stars
    self.comment = comment

  # prints ratings 
  def __str__(self):
    if self.stars == 1:
      return "\n" + emoji.emojize(":star:") + f"\n\033[1m{self.title}\033[0m \n{self.comment}"
    if self.stars == 2:
      return "\n" + emoji.emojize(":star::star:") + f"\n\033[1m{self.title}\033[0m \n{self.comment}"
    if self.stars == 3:
      return "\n" + emoji.emojize(":star::star::star:") + f"\n\033[1m{self.title}\033[0m \n{self.comment}"
    if self.stars == 4:
      return "\n" + emoji.emojize(":star::star::star::star:") + f"\n\033[1m{self.title}\033[0m \n{self.comment}"
    if self.stars == 5:
      return "\n" + emoji.emojize(":star::star::star::star::star:") + f"\n\033[1m{self.title}\033[0m \n{self.comment}"

  # rating objects eqaual if they have same content
  def __eq__(self, other):
    if self.title == other.title and self.comment == other.comment and self.stars == other.stars:
      return True