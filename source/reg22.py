
# Here **kwargs is a variable number of keyword arguments
def menu(**kwargs):
    print(kwargs)
    for key in kwargs:
        print(key, '->', kwargs[key])
        
menu(Pasta=10, Pizza=3, Canolli=2)

menu(Pasta=10, Pizza=3, Canolli=2, Lemonade=2)
