def add_space_before_uppercases(phrase):
  iter = 1
  while (iter < len(phrase)):
    if (65 <= ord(phrase[iter])) and (ord(phrase[iter]) <= 90):
      phrase = phrase[:iter] + ' ' + phrase[iter:]
      iter += 1
    iter += 1
  return phrase

def delete_spaces_and_make_upper(input):
  phrase = ""
  words = input.split(' ')
  for word in words:
    if not (word == words[0]):
      word = word.capitalize()
    phrase += word
  return phrase