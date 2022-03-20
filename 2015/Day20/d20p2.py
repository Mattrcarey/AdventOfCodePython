import math


# The puzzle input is hardcoded in this one
def main():
    input = 29000000
    primes = []
    primeSet = set()

    for x in range(2, input):
        value = getFactorSum(x, primes, primeSet) * 11
        if value >= input:
            print(x)
            return


def getFactorSum(num, primes, primeSet):
    total = 0
    factors = getFactorsUsingPrimes(num, primes, primeSet, {1})

    if factors == {1}:  # This conditions checks if num is prime
        primes.append(num)
        primeSet.add(num)
        if num <= 50:
            return 1 + num
        return num

    for x in factors:
        if (num / x) <= 50:
            total += x

    return total


def getFactorsUsingPrimes(num, primes, primeSet, factors):
    if num == 1:
        return factors

    if num in primeSet:
        factors = addAll(factors, num)
        return factors

    squareRoot = int(math.sqrt(num))
    for value in primes:
        if value > squareRoot:
            return factors
        (div, mod) = divmod(num, value)
        if mod == 0:
            factors = addAll(factors, value)
            return getFactorsUsingPrimes(div, primes, primeSet, factors)

    return factors


def addAll(factors, num):
    newFactors = factors.copy()
    for x in factors:
        newFactors.add(num * x)
    return newFactors


if __name__ == "__main__":
    main()
