#!/usr/bin/python3
"""
te squaare code to complete
added braket to te declaration + other things
"""

class square():
    """
    takes __width and __height and claculates
    area and perimeter
    """

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    def area_of_my_square(self):
        """Area of the square"""
        return self.__width * self.__width

    def permiter_of_my_square(self):
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        return "{}/{}".format(self.__width, self.__height)


if __name__ == "__main__":

    s = square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
