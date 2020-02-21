import csv

try:
  with open('data.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    total = 0
    for r in reader:
      try:
        total += int(r[1])
      except ValueError as v_err:
        print(r)
      print( r[0] + ':' + str(r[1]))
    print('合計:' + str(total))
    print('平均:' + str(total // 5))
except Exception as error:
  print(str(error))
