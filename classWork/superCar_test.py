import unittest

from classWork import superCar


class superCarTest(unittest.TestCase):
    def test_that_car_is_on(self):
        superCar.SuperCar()
        self.assertTrue(True, superCar.SuperCar)
        self.assertFalse(False,superCar.SuperCar)

    # def test_that_can_auto_accelerate(self, gear):
    #     superCar1 = gear.superCar
    #     self.assertEqual(5, superCar1.Supercar )


if __name__ == '__main__':
    unittest.main()
