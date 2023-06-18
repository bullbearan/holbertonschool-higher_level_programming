#!/usr/bin/python3
'''This is a module'''


from .base import Base


class Rectangle(Base):
    '''This is a class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''This is a method'''
        return self.__width

    @width.setter
    def width(self, value):
        '''This is a method'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''This is a method'''
        return self.__height

    @height.setter
    def height(self, value):
        '''This is a method'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''This is a method'''
        return self.__x

    @x.setter
    def x(self, value):
        '''This is a method'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''This is a method'''
        return self.__y

    @y.setter
    def y(self, value):
        '''This is a method'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''This is a method'''
        return self.width * self.height

    def display(self):
        '''This is a method'''
        for row in range(self.y):
            print()
        for row in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        '''This is a method'''
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        '''This is a method'''
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        '''This is a method'''
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
