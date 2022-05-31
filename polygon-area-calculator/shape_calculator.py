class Rectangle:
  def __init__(self,width,height):
      self.width = width
      self.height = height
  def __str__(self):
      return (f'Rectangle(width={self.width}, height={self.height})')
  def set_width(self,width):
      self.width = width
  def set_height(self,height):
      self.height = height
  def get_area(self):
      return self.width*self.height
  def get_perimeter(self):
      return (2*self.width)+(2*self.height)
  def get_diagonal(self):
      return ((self.width**2)+(self.height**2))**0.5
  def get_picture(self):
      piclist = []
      if self.width > 50 or self.height > 50:
        return("Too big for picture.")
      else:
        for i in range(self.height):
          piclist.extend('*'*self.width+'\n')
      return ''.join(piclist)
  def get_amount_inside(self,shape):
      possible = False
      if self.height > shape.height and self.width > shape.width:
        possible = True
      if possible == True:
        return((self.width//shape.width)*(self.height//shape.height))
      else:
        return (0)

class Square(Rectangle):
  def __init__(self,side):
    self.side = side
    Rectangle.width = self.side
    Rectangle.height = self.side
  def __str__(self):
    return (f'Square(side={self.side})')
  def set_side(self,side):
    self.side = side
    Rectangle.width = self.side
    Rectangle.height = self.side
  def set_width(self,width):
    self.side = width
  def set_height(self,height):
    self.side = height 