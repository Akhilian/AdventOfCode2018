from unittest import TestCase

from Day2.InventorySystem import InventorySystem, LetterRepartition


class TestInventorySystem(TestCase):
    def test_checksum(self):
        list_of_box_ids = [
            'abcdef',
            'bababc',
            'abbcde',
            'abcccd',
            'aabcdd',
            'abcdee',
            'ababab',
        ]
        system = InventorySystem(list_of_box_ids)

        assert system.checksum() == 12


class TestInventorySystem(TestCase):
    def test_find_boxes_common_letters(self):
        list_of_box_ids = [
            'abcde',
            'fghij',
            'klmno',
            'pqrst',
            'fguij',
            'axcye',
            'wvxyz',
        ]
        system = InventorySystem(list_of_box_ids)

        assert system.find_boxes_common_letters() == 'fgij'

    def test_find_boxes_common_letters_with_different_position(self):
        list_of_box_ids = [
            'agirmdjvlhedpsyoqfzuknpjwt',
            'agitmdjvlhedpsyoqfzuknpjwt',
        ]
        system = InventorySystem(list_of_box_ids)

        assert system.find_boxes_common_letters() == 'agimdjvlhedpsyoqfzuknpjwt'

    def test_find_boxes_common_letters_with_different_position_both_ways(self):
        list_of_box_ids = [
            'agitmdjvlhedpsyoqfzuknpjwt',
            'agirmdjvlhedpsyoqfzuknpjwt',
        ]
        system = InventorySystem(list_of_box_ids)

        assert system.find_boxes_common_letters() == 'agimdjvlhedpsyoqfzuknpjwt'


class TestLetterRepartition(TestCase):
    def test__id_letter_repartition(self):
        assert LetterRepartition.letter_repartition('abcdef') == {
            'a': 1,
            'b': 1,
            'c': 1,
            'd': 1,
            'e': 1,
            'f': 1,
        }

    def test__id_letter_repartition_with_double_letter(self):
        assert LetterRepartition.letter_repartition('aacdef') == {
            'a': 2,
            'c': 1,
            'd': 1,
            'e': 1,
            'f': 1,
        }

    def test__id_letter_repartition_with_triple_letters(self):
        assert LetterRepartition.letter_repartition('ababab') == {
            'a': 3,
            'b': 3,
        }

