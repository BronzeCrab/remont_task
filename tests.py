import unittest
from remont_task import (calc_distance, get_all_planes,
                         main, PARIS_LONG, PARIS_LAT)


class TestRemontTask(unittest.TestCase):

    def setUp(self):
        self.DISTANCE_FROM_PARIS_TO_MOSCOW_KM = 2487.12
        self.MOSCOW_LONG = 37.617634
        self.MOSCOW_LAT = 55.755787

        self.DISTANCE_FROM_PARIS_TO_BERLIN_KM = 878.36
        self.BERLIN_LONG = 13.4114
        self.BERLIN_LAT = 52.523403

        self.DISTANCE_FROM_PARIS_TO_LONDON_KM = 343.64
        self.LONDON_LONG = -0.12574
        self.LONDON_LAT = 51.50853

        self.ERROR_KM = 1

    def test_calc_distance_between_paris_and_moscow(self):
        distance = calc_distance(
                PARIS_LAT, PARIS_LONG, self.MOSCOW_LAT, self.MOSCOW_LONG)
        self.assertLess(
            abs(distance - self.DISTANCE_FROM_PARIS_TO_MOSCOW_KM),
            self.ERROR_KM)

    def test_calc_distance_between_paris_and_berlin(self):
        distance = calc_distance(
                PARIS_LAT, PARIS_LONG, self.BERLIN_LAT, self.BERLIN_LONG)
        self.assertLess(
            abs(distance - self.DISTANCE_FROM_PARIS_TO_BERLIN_KM),
            self.ERROR_KM)

    def test_calc_distance_between_paris_and_london(self):
        distance = calc_distance(
                PARIS_LAT, PARIS_LONG, self.LONDON_LAT, self.LONDON_LONG)
        self.assertLess(
            abs(distance - self.DISTANCE_FROM_PARIS_TO_LONDON_KM),
            self.ERROR_KM)

    def test_get_all_planes(self):
        all_planes = get_all_planes()
        self.assertIsInstance(all_planes, list)
        self.assertTrue(all_planes)
        return all_planes

    def test_main(self):
        all_planes = self.test_get_all_planes()
        planes_in_radius = main()
        self.assertIsInstance(planes_in_radius, list)
        self.assertLessEqual(len(planes_in_radius), len(all_planes))


if __name__ == '__main__':
    unittest.main()
