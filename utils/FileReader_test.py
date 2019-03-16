from unittest import mock
import io

from utils.FileReader import FileReader



class TestFileReader:
    class Test_read:
        @mock.patch('builtins.open', return_value=io.StringIO("line1\nline2\n"))
        def test_read_should_return_array_of_lines(self, mock):
            lines = FileReader.read('./path/to/file.txt')
            assert lines == ['line1', 'line2']