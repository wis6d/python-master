x = int(input('Enter 1~12:'))

if x // 3 == 0:
  print('冬です')
elif x // 3 == 1:
  print('春です')
elif x // 3 == 2:
  print('夏です')
elif x // 3 == 3:
  print('秋です')
elif x == 12:
  print('冬です')
else:
  print('わかりません')