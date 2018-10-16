class MyClass:

    # a = None
    # b = None
    # def __init__(self):
    #     print("Object init")
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display(self):
        print('a: {}\nb: {}'.format(self.a, self.b))

    def add(self):
        return self.a + self.b        

myObj = MyClass(10, 20)
myObj.display()
print(myObj.add())





