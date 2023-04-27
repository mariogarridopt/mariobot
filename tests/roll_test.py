import unittest

from src.modules.roll import (
    LEAGUE_POSITIONS,
    LEAGUE_CHAMPIONS,
    LEAGUE_BUILDS,
    VAL_CHAR_NAMES,
    role_int,
    role_valorant,
    role_legueoflegends
)


class TestModule(unittest.TestCase):
    def test_role_int(self):
        """Test role_int function"""
        for _ in range(1000):
            result = role_int()
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 10)

    def test_role_valorant(self):
        """Test role_valorant function"""
        for _ in range(1000):
            result = role_valorant()
            self.assertIn(result, VAL_CHAR_NAMES)

    def test_role_legueoflegends(self):
        """Test role_legueoflegends function"""
        for lane in LEAGUE_POSITIONS:
            for _ in range(1000):
                result = role_legueoflegends(lane)
                strList = result.split(' - ')
                lane_name = strList[0]
                champ_name = strList[1]
                build_name = strList[2]

                self.assertIn(lane_name, LEAGUE_POSITIONS)
                self.assertIn(champ_name, LEAGUE_CHAMPIONS[lane_name])
                self.assertIn(build_name, LEAGUE_BUILDS)

if __name__ == '__main__':
    unittest.main()
