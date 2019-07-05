
def netWeight():
    netweight1 = float(input("enter net weight"))
    return netweight1


def making():
    making1 = float(input("enter making"))
    return making1


def processing():
    processing1 = float(input("enter processing fee"))
    return processing1


def rate():
    rate1 = float(input("enter rate per gm"))
    return rate1


def discount():
    discount1 = float(input("enter discount"))
    return discount1


def bill():
    bill1 = ((netWeight()+processing())*rate())+making()-discount()
    print(bill1)
    return bill1



