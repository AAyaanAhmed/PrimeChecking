def check_prime(x):
    if x <= 1:
        return False

    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1

    return True


n = int(input("number "))

if check_prime(n):
    print("prime")
else:
    print("not prime")

a = int(input("start "))
b = int(input("end "))

print("primes in range")
for x in range(a, b + 1):
    if check_prime(x):
        print(x, end=" ")
