import matplotlib.pyplot as plt
import time

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def scatter(self, ax=plt):
        ax.scatter(self.x, self.y) #Рисуем точку
    def scale(ax=plt):
        ax.set_ylim(Shape.y_lim)
        ax.set_xlim(Shape.x_lim)
        ax.set_aspect('equal', adjustable='box')
    

class Shape(Point):
    x_lim = (0, 1)
    y_lim = (0, 1)

    def __init__(self):
        super().__init__()
    def __repr__(self):
        return "x"


class Circle(Shape):

    def __init__(self, centr : Point, radius):
        super().__init__()
        self.x = centr.x
        self.y = centr.y
        self.r = radius

    def draw(self, ax=plt):
        cl = plt.Circle((self.x, self.y), self.r, color='r', alpha = 0.3)
        ax.add_artist(cl)
        Shape.x_lim = min((self.x - self.r - 0.5, Shape.x_lim[0])), max((self.x + self.r + 0.5, Shape.x_lim[1]))
        Shape.y_lim = min((self.y - self.r - 0.5, Shape.y_lim[0])), max((self.y + self.r + 0.5, Shape.y_lim[1]))
        Shape.scale(ax)

    def is_inside(self, p:Point):
        if (p.x - self.x)**2+(p.y - self.y)**2 <= self.r ** 2:
            return True
        else:
            return False




class Square(Shape):

    def __init__(self, sm_centr: Point, width):
        super().__init__()
        self.c = sm_centr
        self.w = width
        self.h = width

    def draw(self, ax = plt):
        c2 = plt.Rectangle((self.c.x, self.c.y), self.w, self.h,  color='b', alpha = 0.3)
        ax.add_artist(c2)
        Shape.x_lim = min((self.c.x - 0.5, Shape.x_lim[0])), max((self.c.x + self.w + 0.5, Shape.x_lim[1]))
        Shape.y_lim = min((self.c.y - 0.5, Shape.y_lim[0])), max((self.c.y + self.h + 0.5,  Shape.y_lim[1]))
        Shape.scale(ax)

    def is_inside(self, p:Point):
        if ((self.c.x - p.x <= 0) and (self.c.x - self.w - p.x <= 0)) and ((self.c.y - p.y <= 0) and (self.c.y - self.w - p.y <= 0)):
            return True
        else:
            return False


class Union(Shape):
    def __init__(self, spis):
        super().__init__()
        self.spis = spis

    def draw(self, ax):
        for fig in self.spis:
            fig.draw(ax)

    def is_inside(self, point:Point):
        ans = False
        for fig in self.spis:
            ans = ans or fig.is_inside(point)
        return ans

class Intersection(Shape):

    
    def __init__(self, lst):
        super().__init__()
        self.lst = lst

    def draw(self, ax):
        for fig in self.lst:
            fig.draw(ax)

    def is_inside(self, point):
        ans = True
        for fig in self.lst:
            s = fig.is_inside(point)
            ans = ans and s
        return ans
    

current_time = time.time()
myPoint = Point(1, 4)
print(time.time() - current_time)
myPoint2 = Point(3, 1)
myPoint3 = Point(1, 5)
myPoint4 = Point(1, 4)
myPoint5 = Point(5,6)
fig, ax = plt.subplots()
current_time1 = time.time()
okr = Circle(myPoint2, 7)
print(time.time() - current_time1)
okr1 = Circle(myPoint3, 8)
sq = Square(myPoint, 7)
sq2 = Square(myPoint2, 7)
sq5 = Square(myPoint2, 6)



myPoint1 = Point(1,2)
a = [okr, sq2, sq]
i = Intersection(a)
i.draw(ax)
myPoint.scatter(ax)
myPoint2.scatter(ax)
myPoint5.scatter(ax)
plt.show()
print(i.is_inside(myPoint5))
print(i.is_inside(myPoint))
print(i.is_inside(myPoint2))