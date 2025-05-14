def p(n):
    l1=list(n)
    s=1
    for x in l1:
        s=s*x
    return s

n=(12,56,67,55,34)
print("Tuple:",n)
print("Product:",p(n))