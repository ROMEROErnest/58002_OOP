class Circle():

  def radius(self, radius):
      rad = radius
  def area(self, rad):
      area = 3.142*rad*rad
      print("The Area of the Circle is: ", area)
  def peri(self, rad):
      area = 2*3.14*rad
      print("The Perimeter of the Circle is: ", area)

c = Circle()
radius = int(input("Enter the Radius of the Circle: "))
c.area(radius)
c.peri(radius)