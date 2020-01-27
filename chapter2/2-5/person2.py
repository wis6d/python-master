class Person:
  name = 'no name'
  mail = 'no address'
  age = 0

  def say(self):
    print('name:' + self.name + ' mail:' + self.mail + ' age:' + str(self.age))

me = Person()
print(me.name, me.mail, me.age)
me.say()

me.name = 'taro'
me.mail = 'taro@yamada'
me.age = 39

me.say()