class  student:
    def __init__(self,name,rno):
        self.name = name
        self.rno = rno
        self.lap = self.laptop()

    def show(self):
        print(self.name,self.rno)
        self.lap.show()k

    class laptop:
        def __init__(self):
            self.brand = "Asus"
            self.cpu = "Intel i5"
            self.ram = "8gb"
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = student("Kritik", 1)
s2 = student("Koshal", 2)

s1.show()
s2.show()