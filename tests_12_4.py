import unittest
import logging
from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)

class RunnerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print()
        for result in cls.all_results.values():
            ans = {}
            for i in result:
                ans[i] = str(result[i])
            print(ans)

    def test_walk_with_negative_speed(self):
        with self.assertRaises(ValueError) as context:
            Runner("Тестовый", -5)
        logging.warning("Неверный тип данных для объекта Runner\n%s", context.exception)

    def test_run_with_non_string_name(self):
        with self.assertRaises(TypeError) as context:
            Runner(12345, 10)
        logging.warning("Неверная скорость для Runner\n%s", context.exception)

if __name__ == '__main__':
    unittest.main()