def createUniqueList(list):
  unique_list = []

  for x in list:
    if x not in unique_list:
      unique_list.append(x)
      
  return unique_list

my_list = [1,7,3,7,1,4,5]
print(createUniqueList(my_list))