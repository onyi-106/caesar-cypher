row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]

map = [row1, row2, row3]
#       0     1     2

# column1 = [1, 4, 7]
# column2 = [2, 5, 8]
# column3 = [3, 6, 9]

position = input("Number: ")
number_of_choice = int(position) - 1

# map[0][0]

if int(position) >= 11 and int(position) <= 13:
  position_of_choice = int(position) - 11
  map[position_of_choice][0] = "x"

elif int(position) >= 21 and int(position) <= 23:
  position_of_choice = int(position) - 21
  map[position_of_choice][1] = "x"

elif int(position) >= 31 and int(position) <= 33:
  position_of_choice = int(position) - 31
  map[position_of_choice][2] = "x"


print(f"{row1}\n{row2}\n{row3}\n")