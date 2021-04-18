#!/use/bin/env python

def fibonacci(n=0, is_list=False):
    fibonacci_list = [0,1]
    if n-1 > len(fibonacci_list):
        for i in range(2,n):
            fibonacci_list.append( fibonacci_list[i-2]+fibonacci_list[i-1])
    return fibonacci_list[n-1] if not bool(is_list) else fibonacci_list 

def test():
    print(fibonacci(40))

if __name__ == "__main__":
    test()