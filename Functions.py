param = 10

def functionName():
    print('This is functionName')

functionName()

def functionWithParam(param):
    param = 100
    print(param)
functionWithParam(param)
print(param)


def functionWithDefaultParams(param2 = "Vaibhav"):
    print(param2)

functionWithDefaultParams("Passed")

def functionWith2Params(myStr, myInt = 10, myDouble = 30.89):
    print(myInt,myStr)

functionWith2Params(10,myDouble=60.89)