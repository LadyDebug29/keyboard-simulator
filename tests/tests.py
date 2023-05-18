import json
import unittest


class TestWritingJSON(unittest.TestCase):

    def test_writing_JSON(self):
        data = {"score": [1, 2, 3, 4, 5, 29, 42]}

        with open('test.json', 'w') as file:
            update_data = json.dumps(data)
            file.write(update_data)
        with open('test.json', 'r') as file:
            self.assertEqual(json.loads(file.read()), {"score": [1, 2, 3, 4, 5, 29, 42]})

    def test_reading_JSON(self):
        with open("test.json", 'r') as file:
            data = json.loads(file.read())
            self.assertEqual(data, {"score": [1, 2, 3, 4, 5, 29, 42]})


if __name__ == '__main__':
    unittest.main()
