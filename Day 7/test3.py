
divisible_by_3_and_5 = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(divisible_by_3_and_5)

prime_gen = (n for n in range(2, 21) if all(n % i != 0 for i in range(2, int(n**0.5) + 1)))

try:
    while True:
        print(next(prime_gen))
except StopIteration:
    print("done")
