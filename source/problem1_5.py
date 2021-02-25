import random

def coin_flips(num_flips, num_people):
    """
    Parameters
    ----------
    num_flips : int
        The number of flips of one coin by one person.
    num_people : int
        The number of people flipping coins.

    Returns
    -------
    A list of number of heads that each person got divided by num_flips.
    """
    ret = []
    for it in range(num_people):
        num_heads = 0
        for flip in range(num_flips):
            face_of_coin = random.choice([0, 1])
            if face_of_coin == 1:
                num_heads += 1
        ret.append(num_heads / num_flips)
    return ret

print(coin_flips(5, 10))
print(coin_flips(10, 10))
print(coin_flips(100, 10))
print(coin_flips(1000, 10))
print(coin_flips(10000, 10))
print(coin_flips(100000, 10))
print(coin_flips(10000, 100))
