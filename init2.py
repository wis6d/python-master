class Person:
  def __init__(self, name='no name', mail='no address', age=0):
    self.name = name
    self.mail = mail
    self.age = age
  
  def say(self):
    print('name:' + self.name + ' mail:' + self.mail + ' age:' + str(self.age))
  
me = Person('taro', 'taro@yamada', 39)
you = Person('hanako')
he = Person()

me.say()
you.say()
he.say()