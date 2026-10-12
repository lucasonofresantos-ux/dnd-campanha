"""Testes básicos. Execute: python -m unittest discover -s skills/dice-roller -p 'test_*.py'"""
import unittest
from dice_roller import roll

class DiceRollerTests(unittest.TestCase):
    def test_bounds(self):
        for expr, sides in [("1d4", 4), ("8d6", 6), ("2d20kh1", 20), ("2d20kl1", 20), ("4d6dl1", 6), ("1d100+3", 100)]:
            value = roll(expr)
            self.assertTrue(all(1 <= die <= sides for die in value["rolls"]))
            self.assertEqual(value["total"], sum(value["rolls"][i] for i in value["kept_indices"]) + value["modifier"])

    def test_reject_invalid(self):
        for expr in ("0d6", "101d6", "1d3", "1d20kh1", "2d20oops"):
            with self.assertRaises(ValueError):
                roll(expr)

if __name__ == "__main__":
    unittest.main()
