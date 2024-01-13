from Ratings import Ratings

class Feedback(Ratings): #subclass 
  def __init__(self, app, title, stars, comment, feedback):
      super().__init__(app, title, stars, comment)
      self.feedback = feedback

  #print feedback
  def __str__(self):
    if self.stars == 1:
      return "\n" + emoji.emojize(":star:") + f"\n\033[1m{self.title}\033[0m \n{self.comment}\n\033[1mFEEDBACK: {self.feedback}\033[0m"
    if self.stars == 2:
      return "\n" + emoji.emojize(":star::star:") + f"\n\033[1m{self.title}\033[0m \n{self.comment}\n\033[1mFEEDBACK: {self.feedback}\033[0m"
    if self.stars == 3:
      return "\n" + emoji.emojize(":star::star::star:") + f"\n\033[1m{self.title}\033[0m \n{self.comment}\n\033[1mFEEDBACK: {self.feedback}\033[0m"
    if self.stars == 4:
      return "\n" + emoji.emojize(":star::star::star::star:") + f"\n\033[1m{self.title}\033[0m \n{self.comment}\n\033[1mFEEDBACK: {self.feedback}\033[0m"
    if self.stars == 5:
      return "\n" + emoji.emojize(":star::star::star::star::star:") + f"\n\033[1m{self.title}\033[0m \n{self.comment}\\033[1mFEEDBACK: {self.feedback}\033[0m"