x = int(input('Enter Number:'))
if x % 2 == 0:
  print('2の倍数')
elif x % 3 == 0:
  print('3の倍数')
elif x % 5 == 0:
  print('5の倍数')
elif x % 7 == 0:
  print('7の倍数')
elif x % 11 == 0:
  print('11の倍数')
else:
  print("I don't know")