import unittest
import library

class TestLibrary(unittest.TestCase):

  def test_add_space_before_uppercases(self):
    result = library.add_space_before_uppercases("addSpaceBeforeUppercase")
    self.assertEqual(result, "add Space Before Uppercase")
    result = library.add_space_before_uppercases("S")
    self.assertEqual(result, "S")

  def test_delete_spaces_and_make_upper(self):
    result = library.delete_spaces_and_make_upper("delete space and make upper")
    self.assertEqual(result, "deleteSpaceAndMakeUpper")
    result = library.delete_spaces_and_make_upper("example")
    self.assertEqual(result, "example")

if __name__ == '__main__':
  unittest.main()