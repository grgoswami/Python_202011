
# Factorial by definition is the product of all the integers between
# 1 and num
def factorial(num):
    prod = 1
    for it in range(2, num + 1):
        prod = prod * it
    return prod

factorial(5)
factorial(3)

def letter_counts(sentence):
    """

    Parameters
    ----------
    sentence : str
        User provides any sentence (or paragraph).

    Returns
    -------
    A dictionary of letters in English with their counts.

    """
    ret = {}
    for word in sentence.split():
        for letter in word:
            if letter not in ret:
                ret[letter] = 1
            else:
                ret[letter] = ret[letter] + 1
    return ret

freq0 = letter_counts('Hello World')
print(freq0)

freq1 = letter_counts('All the world’s a stage, and all the men and women merely players. They have their exits and their entrances; And one man in his time plays many parts.')
print(freq1)

        
    
