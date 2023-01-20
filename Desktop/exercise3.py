user_str = input("please enter a string: ")

def create_dict(string):
  newDict = {}
  for element in string:
    if element not in newDict and element != " ":
      count = string.count(element)
      newDict[element] = count
  print(newDict)

create_dict(user_str)