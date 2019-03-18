class Rectangle:

    def __init__(self, inches_from_left_side = 0, inches_from_top_side = 0, width = 0, height = 0):
        self.inches_from_top_side = inches_from_top_side
        self.inches_from_left_side = inches_from_left_side
        self.height = height
        self.width = width

    def areas(self):
        list_of_areas = list()
        for x_position in range(self.inches_from_top_side, self.inches_from_top_side + self.width):
            for y_position in range(self.inches_from_left_side, self.inches_from_left_side + self.height):
                list_of_areas.append((y_position, x_position))

        return list_of_areas

    def overlap(self, rectangle):
        result = False
        for area in rectangle.areas():
            if area in self.areas():
                result = True

        return result