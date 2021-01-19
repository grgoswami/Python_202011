#print()
#len()


# Empy Function
def Pass():
    pass

Pass()

def Hi():
    print ('hi')

def Greet(name):
    """
    

    Parameters
    ----------
    name : string
        This will be the name of the person who will
        be greeted

    Returns
    -------
    None.

    """
    print("Hi " + name + '! How are you ?')
    input()
    
def Ice_Cream(flavor1, flavor2, topping, bowl, scoops =2,):
    """
    

    Parameters
    ----------
    scoops : int
        DESCRIPTION.
    flavor1 : string
        DESCRIPTION.
    flavor2 : string
        DESCRIPTION.
    topping : string
        DESCRIPTION.
    bowl : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    print("Here's your order : ")
    print(str(scoops) + ' scoops of ' + flavor1 + ' and ' + flavor2)
    print('with ' + topping + ' in a ' + bowl)
    
Ice_Cream('chocolate', 'vanilla', 'sprinkles', 'cone')
Ice_Cream( 'Strawberry',' Vanilla', 'Sprinkles', 'cone', scoops= 1000)
