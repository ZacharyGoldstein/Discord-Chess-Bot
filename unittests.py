import unittest
import calcs

class TestStringMethods(unittest.TestCase):

    def test_rating_is_numeric(self):
        self.assertEqual(calcs.process_inputs("milocannestra", "wrong", "Rapid"), 
        ("Error: rating must be a positive integer.", None, None))

    def test_rating_is_bewlow_3200(self):
        self.assertEqual(calcs.process_inputs("milocannestra", "3201", "Rapid"), 
        ("Error: please submit a rating below 3200.", None, None))

    def test_variant_type(self):
        self.assertEqual(calcs.process_inputs("milocannestra", "2000", "Puzzles"), 
        ("Error: variant not supported. Try bullet, blitz, rapid, or classical.",None,None))

    def test_variant_in_user_history(self):
        self.assertEqual(calcs.score("milocannestra", 2000, "Classical", calcs.model_params), 
        ("Error: user milocannestra has no rating history for variant Classical.", None, None))

    def test_user_hit_rating(self):
        self.assertEqual(calcs.score("milocannestra", 1600, "Rapid", calcs.model_params), 
        ("Congrats! milocannestra has already achieved the target rating 1600 Rapid.", None, None))

    def test_target_less_than_1000_plus_current_rating(self):
        self.assertEqual(calcs.score("milocannestra", 3000, "Rapid", calcs.model_params), 
        ("Error: please submit a target rating gain of less than +1000 points.", None, None))

    def test_user_doesnt_exist(self):
        self.assertEqual(calcs.score("rwafrsdsgga", 3000, "Rapid", calcs.model_params), 
        ("Error: can't retrieve lichess data for user rwafrsdsgga.", None, None))

if __name__ == '__main__':
    unittest.main()