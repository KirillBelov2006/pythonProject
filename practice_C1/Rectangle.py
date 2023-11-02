class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_area(self):
        return  self.height * self.width

