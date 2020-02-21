import csv

try:
  with open('data2.csv', mode='w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',', lineterminator='\r', skipinitialspace=True)
    while True:
      instr = input('data:')
      if instr == '':
        break
      inlist = instr.split(' ')
      writer.writerow(inlist)
except Exception as error:
  print(str(error))
print('***end.***')
