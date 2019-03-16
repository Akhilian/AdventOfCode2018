class LetterRepartition:
    @staticmethod
    def letter_repartition(id)-> dict:
        letters = list(id)
        repartition = dict()
        for letter in letters:
            if letter in repartition:
                repartition[letter] = repartition[letter] + 1
            else:
                repartition[letter] = 1

        return repartition

class InventorySystem:
    def __init__(self, list_of_box_ids = []):
        self.list_of_box_ids = list_of_box_ids

    def checksum(self):
        count_of_ids_with_letters_existing_twice = 0
        count_of_ids_with_letters_existing_thrice = 0

        for id in self.list_of_box_ids:
            id_letters_repartition = LetterRepartition.letter_repartition(id)
            dict_with_2_occurences = {letter: count for (letter, count) in id_letters_repartition.items() if count == 2}
            dict_with_3_occurences = {letter: count for (letter, count) in id_letters_repartition.items() if count == 3}

            if len(dict_with_2_occurences) > 0:
                count_of_ids_with_letters_existing_twice = count_of_ids_with_letters_existing_twice + 1
            if len(dict_with_3_occurences) > 0:
                count_of_ids_with_letters_existing_thrice = count_of_ids_with_letters_existing_thrice + 1


        return count_of_ids_with_letters_existing_twice * count_of_ids_with_letters_existing_thrice

    def find_boxes_common_letters(self):
        result = None
        for index, idA in enumerate(self.list_of_box_ids):
            for idB in self.list_of_box_ids[index+1:]:

                letters_in_a = list(idA)
                letters_in_b = list(idB)

                diff = 0
                for i in range(len(letters_in_a) - 1):
                    if letters_in_a[i] != letters_in_b[i]:
                        diff = diff + 1

                if diff == 1:
                    letters_diff_for_idA = [letter for letter in list(idA) if letter not in list(idB)]
                    letters_diff_for_idB = [letter for letter in list(idB) if letter not in list(idA)]

                    if len(letters_diff_for_idA) == 1:
                        result = ''.join([letter for letter in list(idA) if letter not in letters_diff_for_idA])
                    elif len(letters_diff_for_idB) == 1:
                        result = ''.join([letter for letter in list(idB) if letter not in letters_diff_for_idB])

        return result
