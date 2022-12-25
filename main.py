import commands

if __name__ == '__main__':
  input = input("Enter input: ")
  tuple = input.split(';')
  command = tuple[0]
  operation = tuple[1]
  phrase = tuple[2]

  if (commands.split_command(command)):
    output = commands.split_phrase(phrase)
  elif (commands.combine_command(command)):
    output = commands.combine_phrase(phrase, operation)
  else:
    output = "error: invalid command"

  print(output)