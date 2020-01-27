class Person:
  name = 'no name'
  mail = 'no address'
  age = 0
  nationality = 'no nationality'

  def say(self):
    print('name:' + self.name + ' mail:' + self.mail + ' age:' + str(self.age) + ' nationality:' + self.nationality)

me = Person()
print(me.name, me.mail, me.age, me.nationality)
me.say()

me.name = 'taro'
me.mail = 'taro@yamada'
me.age = 39
me.nationality = 'Japan'

me.say()