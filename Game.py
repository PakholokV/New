fillename = open('book.txt','r', encoding='utf-8')

def opened():
    fillename = open('book.txt')
    return fillename


def rehab():
    with opened() as file:
        for line in file:
            for word in line.split():
                print(word)


def conts():
    text = fillename.read()
    se = "A"
    t = text.count(se)
    print(str(t))
conts()















