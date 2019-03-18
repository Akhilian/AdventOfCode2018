class Diplomat:
    def __init__(self, list_of_claims = []):
        self.list_of_claims = list_of_claims

    def number_of_conflicts(self):
        count_of_conflict = 0
        list_of_claimed_areas = []
        for index, current_claim in enumerate(self.list_of_claims):
            print('Iteration', index)

            is_in_conflict = False
            for area in current_claim.rectangle.areas():
                if area in list_of_claimed_areas:
                    is_in_conflict = True
                else:
                    list_of_claimed_areas = list_of_claimed_areas + [area]

            if is_in_conflict:
                count_of_conflict = count_of_conflict + 1

        return count_of_conflict