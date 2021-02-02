
# The following is called closure
def shifter(shift_by=5):
    def shift(x):
        return x + shift_by
    
    return shift

s0 = shifter(5)
print(s0(10))
print(s0(100))

s1 = shifter(-5)
print(s1(10))
print(s1(100))

# One more example of closure
# The three variables size, place and weather are contained
# in the closure of serve.
def mega_taco(size=100):
    place = 'Short Hills'
    weather = 31
    def serve(person):
        print(f'Hi {person}! Here is your taco. You are at {place}. It is {weather} degrees now.')
        return size
    return serve
    
mt0 = mega_taco(10)
print(mt0('Rishaan'))
print(mt0('Gia'))
