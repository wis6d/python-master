def total(n):
  if 0 < n < 5:
    total = 0

    for n in range(n + 1):
      total += n
    return total
  elif n > 5 :
    total = 0

    for n in range(n * 2):
      total += n
    return total
  else:
    return 0

s = 1
while s:
  try:
    s = int(input('Enter number:'))
    print('合計:', total(s))
  except:
    s = 0
    print('正しい数字ではありません')