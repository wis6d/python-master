x = int(input('Enter number:'))
total = 0
count = 1

while count <= x:
  total += count
  count += 1
print('合計は、' + str(total) + 'です')