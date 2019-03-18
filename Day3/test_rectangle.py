import pytest
from Day3.Rectangle import Rectangle

class TestRectangle:
    @pytest.mark.parametrize("from_left,from_top,height,width,result", [
        (0, 0, 1, 1, [(0,0)]),
        (0, 1, 1, 1, [(0,1)]),
        (0, 0, 1, 2, [(0,0), (0,1)]),
        (0, 0, 2, 1, [(0,0), (1,0)]),
        (1, 0, 1, 1, [(1,0)]),
        (2, 2, 3, 3, [
            (2,2), (3,2), (4,2),
            (2,3), (3,3), (4,3),
            (2,4), (3,4), (4,4),
        ]),
    ])
    def test_should_have_areas(self, from_left, from_top, height, width, result):
        rectangle = Rectangle(from_left, from_top, width, height)

        assert rectangle.areas() == result

    class Test_overlap:
        def test_should_return_false_when_not_overlap(self):
            rectangle_one = Rectangle(0, 0, 1, 1)
            rectangle_two = Rectangle(2, 2, 2, 2)

            assert rectangle_one.overlap(rectangle_two) == False
            assert rectangle_two.overlap(rectangle_one) == False

        def test_should_return_true_when_not_overlap(self):
            rectangle_one = Rectangle(0, 0, 3, 3)
            rectangle_two = Rectangle(2, 2, 2, 2)

            assert rectangle_one.overlap(rectangle_two) == True
            assert rectangle_two.overlap(rectangle_one) == True