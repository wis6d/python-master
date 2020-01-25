class Person:
  def __init__(self, name, mail, age):
    self.name = name
    self.mail = mail
    self.age = age
  
  def say(self):
    print('name:' + self.name + ' mail:' + self.mail + ' age:' + str(self.age))
  
me = Person('taro', 'taro@yamada', 39)
you = Person('hanako', 'hanako@flower', 45)

me.say()
you.say()