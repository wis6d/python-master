x = int(input('Confirm season. Enter 1~12: '))

if x // 3 == 0:
  print('winter')
elif x // 3 == 1:
  print('spring')
elif x // 3 == 2:
  print('summer')
elif x // 3 == 3:
  print('autumn')
elif x // 3 == 4:
  print('winter')
else:
  print('not found')