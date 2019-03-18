from Day3.Claim import Claim


class TestClaim:
    class Test_parse:
        def test_parse_should_return_a_claim(self):
            claim = Claim.parse('#123 @ 3,2: 5x4')
            assert isinstance(claim, Claim)

        def test_parse_should_return_a_claim_with_an_id(self):
            claim = Claim.parse('#123 @ 3,2: 5x4')
            assert claim.id == 123

        def test_parse_should_return_a_claim_the_dimensions(self):
            claim = Claim.parse('#123 @ 3,2: 5x4')

            assert claim.rectangle.width == 5
            assert claim.rectangle.height == 4
            assert claim.rectangle.inches_from_left_side == 3
            assert claim.rectangle.inches_from_top_side == 2

        def test_parse_should_return_a_claim_with_more_that_digit(self):
            claim = Claim.parse('#1 @ 56,249: 24x16')

            assert claim.rectangle.width == 24
            assert claim.rectangle.height == 16
            assert claim.rectangle.inches_from_left_side == 56
            assert claim.rectangle.inches_from_top_side == 249

    class Test_is_in_conflict_with:
        def test_when_no_conflict_should_return_true(self):
            claim_one = Claim.parse('#123 @ 0,0: 1x1')
            claim_false = Claim.parse('#123 @ 0,0: 2x2')

            assert claim_one.is_in_conflict_with(claim_false) is True

        def test_when_no_conflict_should_return_false(self):
            claim_one = Claim.parse('#123 @ 0,0: 1x1')
            claim_false = Claim.parse('#123 @ 2,2: 1x1')

            assert claim_one.is_in_conflict_with(claim_false) == False
