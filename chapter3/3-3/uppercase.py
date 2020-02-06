s = '''
One Little, two little, three little Indians
Four little, five LITTLE, six LiTTle Indians
Seven LittlE, eight little, nine LittLe Indians
Ten Little Indians.
'''

f = "little"
r = "BIG"
s2 = s.lower()
n = 0

while (s2.find(f, n) != -1):
  i = s2.find(f, n)
  s = s[:i] + r + s[(i + len(f)):]
  s2 = s2[:i] + r + s2[(i + len(f)):]
  n = i + len(r)

print(s)