def get_combined_dict(dict1, dict2):

  combined_dict = {}
  for key1 in dict1:
    for key2 in dict2:
      if key1 == key2:
        combined_dict[key1] = dict1[key1] + dict2[key2]
  return combined_dict

dict1 = {"a": 4, "b": 5, "c": 3}
dict2 = {"b": 6, "c": 20, "d" : 2}

print(get_combined_dict(dict1, dict2))