import pytest
from Day1.Chronal_Calibration import Device


class TestDevice:
    def test_chronal_calibration_should_start_at_zero(self):
        device = Device()
        device.calibrate()
        assert device.final_frequency == 0

    def qtest_chronal_calibration_should_increment_from_change_sequence(self):
        device = Device()
        device.calibrate(['+1'])
        assert device.final_frequency == 1

    def test_chronal_calibration_should_deacrease_from_change_sequence(self):
        device = Device()
        device.calibrate(['-3'])
        assert device.final_frequency == -3

    class Test_calibrate:
        @pytest.mark.parametrize("sequence,result", [
            (['-3', '-1'], -4),
            (['8', '-2'], 6),
        ])
        def test_chronal_calibration_should_work_with_given_examples(self, sequence, result):
            device = Device()
            device.calibrate(sequence)
            assert device.final_frequency == result

    class Test_frequency:
        @pytest.mark.parametrize("sequence,result", [
            (['+0'], 0),
            (['+1', '-1'], 0),
            (['+2', '-1', '+1', '+4'], 2),
            (['+3', '+3', '+4', '-2', '-4'], 10),
            (['-6', '+3', '+8', '+5', '-6'], 5),
            (['+7', '+7', '-2', '-7', '-4'], 14),
            (['+1', '-2', '+3', '+1'], 2),
        ])
        def test_chronal_calibration_should_return_first_sequence(self, sequence, result):
            device = Device()
            device.calibrate(sequence)
            assert device.frequency == result