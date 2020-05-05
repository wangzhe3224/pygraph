from unittest import TestCase
import datetime
import time

from pygraph.common.timing import StopWatch


class TestTiming(TestCase):
    """"""

    def setUp(self) -> None:
        """"""
        self.stopwatch = StopWatch()

    def test_report(self):

        # self.stopwatch.click('1')
        time.sleep(0.5)
        self.stopwatch.click('2')

        print(self.stopwatch.report())

    def test_calc_ms(self):

        start = datetime.datetime(2020, 5, 5, 18, 35, 13, 825411)
        end = datetime.datetime(2020, 5, 5, 18, 35, 13, 925411)

        diff = self.stopwatch.calc_time_ms(start, end)
        self.assertEqual(100, diff)
