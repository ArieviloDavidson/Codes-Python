def épar(x):
    return x%2 == 0

print(épar(4))
print(épar(3))

def fatorial(x):
    f = 1
    while x > 0:
        f = f * x
        x = x - 1
    return f

x = int(input("digite o fatorial: "))
print(fatorial(x))

for x in range(5): print(fatorial(x))