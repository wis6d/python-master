class Person:
  def __init__(self, name='no name', mail='no address', age=0):
    self.name = name
    self.mail = mail
    self.age = age
  
  def say(self):
    print('name:' + self.name + ' mail:' + self.mail + ' age:' + str(self.age))

class Member(Person):
  def say(self):
    print('My name is ' + self.name + 'I am ' + str(self.age) + "year's old. ")
    print('    please send mail to "' + self.mail + '".')

me = Person('taro', 'taro@yamada', 39)
me.say()
you = Member('hanako', 'hanako@flower', 45)
you.say()