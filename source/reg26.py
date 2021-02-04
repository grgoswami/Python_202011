
def Fibonacci_gen():
    store = []
    def Fibonacci(num):
        if len(store) > num:
            print('Returning from store')
            return store[:(num + 1)]
        else:
            print('Computing new numbers')
            for it in range(len(store), num):
                if it == 0 or it == 1:
                    store.append(1)
                else:
                    store.append(store[it - 2] + store[it - 1])
        return store[:(num + 1)]
    return Fibonacci

fib = Fibonacci_gen()
print(fib(2))
print(fib(4))
print(fib(10))
print(fib(5))
                    
                
        