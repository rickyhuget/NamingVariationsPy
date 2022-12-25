from library import delete_spaces_and_make_upper

def method_operation(type):
  if (type == 'M') or (type == 'm'):
    return True
  return False

def variable_operation(type):
  if (type == 'V') or (type == 'v'):
    return True
  return False

def class_operation(type):
  if (type == 'C') or (type == 'c'):
    return True
  return False

def make_method_name(phrase):
  phrase = phrase.strip()
  phrase = delete_spaces_and_make_upper(phrase)
  phrase += "()"
  return phrase
  
def make_variable_name(phrase):
  phrase = phrase.strip()
  phrase = delete_spaces_and_make_upper(phrase)
  return phrase

def make_class_name(phrase):
  phrase = phrase.strip()
  phrase = phrase.capitalize()
  phrase = delete_spaces_and_make_upper(phrase)
  return phrase