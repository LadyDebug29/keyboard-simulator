import json
import unittest

import utils.utils


class TestWritingJSON(unittest.TestCase):

    def test_writing_JSON(self):
        data = {
            "count_characters_entered": [
                1, 2, 3
            ],
            "count_words_entered": [
                5, 6, 7
            ],
            "print_speed": [
                29, 42, 55
            ],
            "training_dynamics":
                {
                    1: 7,
                    2: 3
                }

        }

        # with open('test.json', 'w') as file:
        #     json.dump(data, file, indent=4)
        utils.utils.writeToJson("test.json", data)
        with open('test.json', 'r') as file:
            self.assertEqual(json.load(file), {
                "count_characters_entered": [
                    1, 2, 3
                ],
                "count_words_entered": [
                    5, 6, 7
                ],
                "print_speed": [
                    29, 42, 55
                ],
                "training_dynamics":
                    {
                        "1": 7,
                        "2": 3
                    }
            })

    def test_reading_JSON(self):
        update_data = utils.utils.readFromJson("test.json")
        self.assertEqual(update_data, {
            "count_characters_entered": [
                1, 2, 3
            ],
            "count_words_entered": [
                5, 6, 7
            ],
            "print_speed": [
                29, 42, 55
            ],
            "training_dynamics":
                {
                    "1": 7,
                    "2": 3
                }
        })


if __name__ == '__main__':
    unittest.main()
