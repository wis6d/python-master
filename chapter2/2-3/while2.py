x = int(input('Enter your favorite number:'))
total = 0
count = 1

while count <= x:
  total += count
  count += 1
print('Amount: ' + str(total))