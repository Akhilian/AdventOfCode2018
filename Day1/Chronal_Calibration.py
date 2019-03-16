class Device:

    def __init__(self):
        self.final_frequency = 0
        self.frequency = None

    def calibrate(self, sequence=[]):
        parsed_sequence_values = list(map(int, sequence))

        self.final_frequency = sum(parsed_sequence_values)
        self.frequency = self.__find_stable_frequency(parsed_sequence_values)

    def __find_stable_frequency(self, sequence_changes) -> object:
        number_of_entries_in_log = len(sequence_changes)

        index = 0
        first_sequence_occuring_twice = None
        sequence_log = [0]
        while first_sequence_occuring_twice is None:
            next_frequency = sequence_log[-1] + sequence_changes[index]

            if next_frequency in sequence_log:
                first_sequence_occuring_twice = next_frequency

            sequence_log = sequence_log + [next_frequency]

            index = index + 1
            if index >= number_of_entries_in_log:
                index = 0

        return first_sequence_occuring_twice
