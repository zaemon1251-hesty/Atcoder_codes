from bisect import bisect

x = int(input())
prime = get_prime(2 * pow(10, 5))
while not prime[x]:
    x += 1
print(x)
