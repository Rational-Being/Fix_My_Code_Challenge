#!/usr/bin/python3
"""
te squaare code to complete
added braket to te declaration + other things
"""

class square():
    """
    takes width and height and claculates
    area and perimeter
    """

    width = 0
    height = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.width

    def permiter_of_my_square(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
