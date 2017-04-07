class myClass():
    name = 'Sam'

    def sayHi(self):
        print('hello tom!')
        print('Hello %s'%self.name)
        mc = myClass()
        print(mc.name)
        mc.name = 'Lily'
        mc.sayHi()
a=myClass()
a.sayHi()