from Day3.Rectangle import Rectangle


class Claim:

    def __init__(self, id:int, width:int, height:int, position_from_left:int, position_from_top:int):
        self.id = id
        self.rectangle = Rectangle(position_from_left, position_from_top, width, height)

    @staticmethod
    def parse(scheme:str):
        portions = scheme.split()
        width = int(portions[3].split('x')[0])
        height = int(portions[3].split('x')[1])
        position_from_left = int(portions[2].split(',')[0])
        position_from_top = int(portions[2].split(',')[1][0:-1])

        return Claim(
            int(portions[0][1:]),
            width,
            height,
            position_from_left,
            position_from_top,
        )

    def is_in_conflict_with(self, claim):
        return self.rectangle.overlap(claim.rectangle)