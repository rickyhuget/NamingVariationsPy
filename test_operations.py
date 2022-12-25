import unittest
import operations

class TestTypes(unittest.TestCase):
  
  def test_make_method_name(self):
    result = operations.make_method_name("make method name")
    self.assertEqual(result, "makeMethodName()")
    result = operations.make_method_name("make method name ")
    self.assertEqual(result, "makeMethodName()")

  def test_make_variable_name(self):
    result = operations.make_variable_name("make variable name")
    self.assertEqual(result, "makeVariableName")
    result = operations.make_variable_name("make 1 variable name")
    self.assertEqual(result, "make1VariableName")

  def test_make_class_name(self):
    result = operations.make_class_name("make class name")
    self.assertEqual(result, "MakeClassName")
    result = operations.make_class_name("make 1 class  name")
    self.assertEqual(result, "Make1ClassName")

if __name__ == '__main__':
  unittest.main()