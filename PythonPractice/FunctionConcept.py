def test():
    print("Hello World")


test()  # Hello World


def abc(a):
    print(a + 10)


abc(10)  # 20


# optional/Default parameter
def getCountryName(name="India"):
    print(name)


getCountryName()  # India
getCountryName("UK")  # UK
getCountryName(100)  # 100


# pass a list to a function
def getNames(list):
    for x in list:
        print(x)


names = ["Java", "Python", "Dot Net", "Ruby"]
getNames(names)


# output:
# Java
# Python
# Dot Net
# Ruby

# function with return
def sum(a, b):
    c = a + b
    return c


s1 = sum(10, 20)
print(s1)  # 30
print(sum(50, 50))  # 100


def getCapitalName(countryName):
    if countryName == "India":
        return "New Delhi"
    elif countryName == "USA":
        return "Washington DC"


print(getCapitalName("India"))  # New Delhi
print(getCapitalName("USA"))  # Washington DC


def launchBrowser(browserName):
    if browserName == "chrome":
        print("launch google chrome")
    elif browserName == "firefox":
        print("launch mozilla firefox")
    else:
        print("no browser defined!!!")


launchBrowser("chrome")  # launch google chrome
launchBrowser("firefox")  # launch mozilla firefox
launchBrowser("IE")  # no browser defined!!!


# Recursion function
# a function is calling by itself

# WAP to get the factorial of a given number:
# fact(4) = 4*3*2*1 = 24
# fact(5) = 5*4*3*2*1 = 120

def fact(num):
    if (num > 1):
        num = num * fact(num - 1)
    return num


print(fact(4))  # 24
print(fact(5))  # 120


# concatenation in appending on Python
def login(userName, password):
    print("login with %s and %s" % (userName, password))


login("rajeevanand1991@gmail.com", "test@123")  # login with rajeevanand1991@gmail.com and test@123