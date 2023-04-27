import unittest
import pytz
from datetime import datetime
from src.modules.timer_cog import timer_cog


class TestTimerCog(unittest.TestCase):
    def setUp(self):
        portugal_timezone = pytz.timezone('Europe/Lisbon')
        current_time = datetime.now(portugal_timezone)
        self.current_time = current_time.strftime("%I:%M %p")

    def test_getCurrentTime(self):
        current_time = timer_cog.getCurretTime()

        self.assertIsInstance(current_time, str)
        self.assertNotEqual(current_time, '')
        self.assertEqual(current_time.split(':')[0], self.current_time.split(':')[0])
        