import unittest
import commands

class TestCommands(unittest.TestCase):

  def test_combine_command(self):
    result = commands.combine_command('C')
    self.assertTrue(result)
    result = commands.combine_command('c')
    self.assertTrue(result)
    result = commands.combine_command('S')
    self.assertFalse(result)

  def test_split_command(self):
    result = commands.split_command('S')
    self.assertTrue(result)
    result = commands.split_command('s')
    self.assertTrue(result)
    result = commands.split_command('C')
    self.assertFalse(result)
  
  def test_combine_phrase(self):
    result = commands.combine_phrase("combine method", 'm')
    self.assertEqual(result, "combineMethod()")
    result = commands.combine_phrase("combine variable", 'v')
    self.assertEqual(result, "combineVariable")
    result = commands.combine_phrase("combine class", 'c')
    self.assertEqual(result, "CombineClass")
  
  def test_split_phrase(self):
    result = commands.split_phrase("thisIsSamplePhrase")
    self.assertEqual(result, "this is sample phrase")
    result = commands.split_phrase("  thisIsSamplePhrase")
    self.assertEqual(result, "this is sample phrase")
    result = commands.split_phrase("  thisIsSamplePhrase   ")
    self.assertEqual(result, "this is sample phrase")
    result = commands.split_phrase("ThisIsSamplePhrase")
    self.assertEqual(result, "this is sample phrase")
    result = commands.split_phrase("  thisIsSamplePhrase()  ")
    self.assertEqual(result, "this is sample phrase")

if __name__ == '__main__':
  unittest.main()