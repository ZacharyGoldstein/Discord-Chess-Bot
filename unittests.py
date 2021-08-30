import unittest
import calcs
import aiounittest

class TestDiscordBotProcessInputsFuncs(aiounittest.AsyncTestCase):

    async def test_rating_is_numeric(self):
        self.assertEqual(await calcs.process_inputs("nihalsarin2004", "wrong", "Rapid"), 
        ("Error: rating must be a positive integer.", None, None))

    async def test_rating_is_below_3200(self):
        self.assertEqual(await calcs.process_inputs("ZackAttack614", "3201", "rapid"), 
        ("Error: please submit a rating below 3200.", None, None))

    async def test_variant_type(self):
        self.assertEqual(await calcs.process_inputs("johndavis_59", "2000", "Puzzles"), 
        ("Error: variant not supported. Try bullet, blitz, rapid, or classical.",None,None))

    async def test_variant_type_2(self):
        self.assertEqual(await calcs.process_inputs("HumanSponge", "2000", "fun_chess_variant_5"), 
        ("Error: variant not supported. Try bullet, blitz, rapid, or classical.",None,None))

    async def test_default_variant_is_rapid(self):
        self.assertTrue(await calcs.process_inputs("bali1331", "2100"), 
         await calcs.process_inputs("bali1331", "2100", "rapid"))

    async def test_switching_inputs(self):
        self.assertTrue(await calcs.process_inputs("2000", "milocannestra"), 
        "Error: rating must be a positive integer.")

    async def test_negative_target_rating(self):
        self.assertTrue(await calcs.process_inputs("grandmastergauri", "-1000"), 
        "Error: rating must be a positive integer.")

    async def test_decimal_target_rating(self):
        self.assertTrue(await calcs.process_inputs("EricRosen", "2800.8"), 
        "Error: rating must be a positive integer.")

class TestDiscordBotScoreFuncs(aiounittest.AsyncTestCase):
    async def test_variant_in_user_history(self):
        self.assertEqual(await calcs.score("milocannestra", 2000, "classical", calcs.model_params), 
        ("Error: user milocannestra has no rating history for variant Classical.", None, None))

    async def test_user_hit_rating(self):
        self.assertEqual(await calcs.score("penguingim1", 500, "Bullet", calcs.model_params), 
        ("Congrats! penguingim1 has already achieved the target rating 500 Bullet.", None, None))

    async def test_target_less_than_1000_plus_current_rating(self):
        self.assertEqual(await calcs.score("KrnAmericanChessNoob", 3100, "Rapid", calcs.model_params), 
        ("Error: please submit a target rating gain of less than +1000 points.", None, None))

    async def test_user_doesnt_exist(self):
        self.assertEqual(await calcs.score("rwafrsdsgga", 3000, "Rapid", calcs.model_params), 
        ("Error: can't retrieve lichess data for user rwafrsdsgga.", None, None))


if __name__ == '__main__':
    unittest.main()