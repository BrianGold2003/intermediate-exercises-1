int1 = input("please enter a number: ")
while not int1.isdigit():
  int1 = input("not a number, try again: ")
  
int2 = input("please enter a number: ")
while not int2.isdigit():
  int2 = input("not a number, try again: ")
  
int3 = input("please enter a number: ")
while not int3.isdigit():
  int3 = input("not a number, try again: ")

int4 = input("please enter a number: ")
while not int4.isdigit():
  int4 = input("not a number, try again: ")

int5 = input("please enter a number: ")
while not int5.isdigit():
  int5 = input("not a number, try again: ")

print("sum:", end = " ")
print(int(int1) + int(int2) + int(int3) + int(int4) + int(int5))