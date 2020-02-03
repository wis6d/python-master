data = [
  98, 23, 45, 56,
  89, 87, 12, 34,
  49, 30, 51, 94
]

total = sum(data)
ave = total / len(data)

print('合計:' + str(total))
print('平均:' + str(ave))
print('最小:' + str(min(data)))
print('最大:' + str(max(data)))