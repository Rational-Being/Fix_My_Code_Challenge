#!/usr/bin/python3
"""
te squaare code to complete
added braket to te declaration + other things
"""

class Square():
    """
    takes __width and __height and claculates
    area and perimeter
    """

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """ the constructor """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if value <= 0:
            raise ValueError
        elif type(value) is not int:
            raise TypeError
        else:
            self.__width = value

    @property
    def height(self):
        """heihgt getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if value <= 0:
            raise ValueError
        elif type(value) is not int:
            raise TypeError
        else:
            self.__height = value

    def area_of_my_square(self):
        """Area of the square"""
        return self.__width * self.__height

    def permiter_of_my_square(self):
        """calculating perimeter"""
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ defualt string """
        return "{}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    """Using the object the right way"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
