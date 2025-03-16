import unittest
from main import Calculator

class CalculatorSumTests(unittest.TestCase):

    def logs_to_str(self, log):
        return "\n".join(
            [f'> {i["a"]} + {i["b"]} = {i["result"]}' if i.get("a") != None
             else f'!> {i["type"]}: {i["message"]}'
             for i in log]
        )

    def setUp(self) -> None:
        self.calc = Calculator()

    def test_sum(self):
        a,b = 3.4 ,4
        check = a + b
        result = self.calc.sum(a,b)
        self.assertEqual(result, check)

    def test_log(self):
        a, b = 3, 4
        check = a + b

        res_log = {'a': a, 'b': b, 'result': check}
        res_str = "\n".join([f'> {i["a"]} + {i["b"]} = {i["result"]}' for i in [res_log]])

        result = self.calc.sum(a, b)

        self.assertIn(res_log, self.calc.logs.logs)
        self.assertIn(res_str, str(self.calc.logs).split("\n"))

    def test_non_num(self):
        a,b = "a", 3

        with self.assertRaises(ValueError):
            self.calc.sum(a, b)

    def test_error_logging(self):
        a,b = "a", 2

        with self.assertRaises(ValueError):
            self.calc.sum(a,b)
            err_log = {"type": "error", "message": "value can not be parsed to float"}
            err_str = f'!> {err_log["type"]}: {err_log["message"]}'
            self.assertIn(err_log, self.calc.logs.logs)
            self.assertIn(err_str, str(self.calc.logs))

    def test_sum_bignums(self):
        a, b = 1.0e100, 1.0e100
        check = a + b
        res = self.calc.sum(a,b)
        self.assertEqual(res, check)

    def test_multiaction(self):
        data = [
            [1,2],
            [0.1, 0.2],
            [-1, 3.2]
        ]

        check = [sum(i) for i in data]


        for line, check_num in zip(data, check):
            self.assertEqual(self.calc.sum(*line), check_num)

    def test_multiaction_logs(self):
        data = [
            ["not number", "definetly not number"],
            ["52", 1],
            [1,2]
        ]

        logs = [
            {"type": "error", "message": "value can not be parsed to float"},
            {"type": "error", "message": "value can not be parsed to float"},
            {'a': 1, 'b': 2, 'result': 3}
        ]

        check_str = self.logs_to_str(logs)

        with self.assertRaises(ValueError):
            for line in data:
                self.calc.sum(*line)
            self.assertEqual(str(self.calc.logs), check_str)

if __name__ == '__main__':
    unittest.main()
