import unittest
from. import playground


class PlaygroundTest(unittest.TestCase):
    def setUp(self) -> None:
        print("i run before")

    def tearDown(self) -> None:
        print("i run after")


    def test_something(self):
        print("i am running")





if __name__ == '__main__':
    unittest.main()
