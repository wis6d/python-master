try:
  with open('data.txt', mode='r') as f:
    count = 0
    for p in f:
      count += 1
      print( str(count) + ':' + p)
except Exception as error:
  print(str(error))