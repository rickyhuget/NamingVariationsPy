import operations
from library import add_space_before_uppercases

def split_command(command):
  if (command == 'S') or (command == 's'):
    return True
  return False

def combine_command(command):
  if (command == 'C') or (command == 'c'):
    return True
  return False

def combine_phrase(phrase, operation):
  if (operations.method_operation(operation)):
    phrase = operations.make_method_name(phrase)
  elif (operations.variable_operation(operation)):
    phrase = operations.make_variable_name(phrase)
  elif (operations.class_operation(operation)):
    phrase = operations.make_class_name(phrase)
  else:
    phrase = "error in combine_phrase(phrase, type)"
  return phrase

def split_phrase(phrase):
  phrase = phrase.strip()
  phrase = phrase.strip('()')
  phrase = add_space_before_uppercases(phrase)
  phrase = phrase.lower()
  return phrase