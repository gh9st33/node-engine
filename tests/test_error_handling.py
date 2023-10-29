```python
import unittest
from src.execution_engine.error_handling import ErrorHandler

class TestErrorHandling(unittest.TestCase):

    def setUp(self):
        self.error_handler = ErrorHandler()

    def test_log_error(self):
        try:
            raise Exception("Test Exception")
        except Exception as e:
            self.error_handler.log_error(e)
            self.assertEqual(len(self.error_handler.error_log), 1)
            self.assertEqual(self.error_handler.error_log[0].message, "Test Exception")

    def test_clear_errors(self):
        try:
            raise Exception("Test Exception")
        except Exception as e:
            self.error_handler.log_error(e)
        self.error_handler.clear_errors()
        self.assertEqual(len(self.error_handler.error_log), 0)

    def test_get_errors(self):
        try:
            raise Exception("Test Exception")
        except Exception as e:
            self.error_handler.log_error(e)
        errors = self.error_handler.get_errors()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0].message, "Test Exception")

if __name__ == '__main__':
    unittest.main()
```