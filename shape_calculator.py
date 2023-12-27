class Rectangle:

  def __init__(self, w, h):
    self.width = w
    self.height = h

  def set_width(self, w):
    self.width = w

  def set_height(self, h):
    self.height = h

  def get_area(self):
    area = (self.width * self.height) 
    return area

  def get_perimeter(self):
    perimeter = (2 * self.width + 2 * self.height)
    return perimeter

  def get_diagonal(self):
    diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
    return diagonal

  def get_picture(self):
    picture = str()
    if self.width > 50 or self.height > 50:
      picture += "Too big for picture."
      return picture
    x = 0
    y = 0
    while y < self.height:
      while x < self.width:
        picture += "*"
        x += 1
      picture += "\n"
      x = 0
      y += 1
    return picture

  def __str__(self):
    string = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    return string

  def get_amount_inside(self, shape):
    amount = ((self.width * self.height) / (shape.width * shape.height))
    return int(amount)

class Square(Rectangle):

  def __init__(self, s):
    self.width = s
    self.height = s
  
  def set_side(self, s):
    self.width = s
    self.height = s

  def __str__(self):
    string = "Square(side=" + str(self.width) + ")"
    return string