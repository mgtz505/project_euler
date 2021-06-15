# PROBLEM 1 - Correctly Solved
# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def problem1(N):
    solution = []
    for i in range(1,N):
        if i % 3 == 0 or i % 5 ==0:
            solution.append(i)
    return sum(solution)

# print(problem1(1000))

#PROBLEM 2
# https://projecteuler.net/problem=2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
#  By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#  find the sum of the even-valued terms.

def problem2(N):
    results = []
    if N == 0:
        return 0
    elif N == 1 or N == 2:
        return 1
    else:
        value = problem2(N - 1) + problem2(N - 2)
        print(value)
        if value % 2 == 0:
            results.append(value)
    return results
# print(problem2(10))


# PROBLEM 4 - Correctly Solved
# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def problem4(bound):
    results = []
    for i in range(1,bound):
        for j in range(1,bound):
            value = i * j
            if str(value) == str(value)[::-1]:
                results.append(value)
    return max(results)

# print(problem4(999)) 


#PROBLEM 5 - Correctly Solved... but algorithm is VERY slow... needs to be reworked
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def problem5(ceiling):
    check_list = [11, 13, 14, 16, 17, 18, 19, 20]
    for i in range(2521,ceiling):
        if all(i % num == 0 for num in check_list):
            return i
    return None
            
# print(problem5(999_999_999))


#PROBLEM 6 - Solved Correctly
# https://projecteuler.net/problem=6
# The sum of the squares of the first ten natural numbers is,
# The square of the sum of the first ten natural numbers is,
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def problem6(N):
    sumOfSquares, sumNum = 0, 0
    for i in range(1,N + 1):
        sumOfSquares += (i * i)
        sumNum += i
    # print(sumOfSquares)
    # print(sumNum)
    # print(sumNum ** 2)

    return (sumNum ** 2) - sumOfSquares
# print(problem6(100))


#PROBLEM 7 - Solved Correctly
# https://projecteuler.net/problem=7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def problem7(N):
    #Will use Sieve of Eratosthenes to yield my primes:
    primeArray = []

    prime = [True for i in range(N + 1)]
    p = 2
    while (p * p <= N):

        if (prime[p] == True):
            for i in range(p * p, N + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, N + 1):
        if len(primeArray) == 10001:
            return primeArray[-1]
        else:
            if prime[p]:
                primeArray.append(p)

print(problem7(5_000_000))


#PROBLEM 8 - Incorrect Approach; Need to revisit
# https://projecteuler.net/problem=8
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. 
# What is the value of this product?
# import math
# def problem8(num):
#     products_final = []
#     groups = [str(num)[i:i+13] for i in range(0,len(str(num)),13)]
#     # print(groups)
#     for i in range(len(groups)):
#         # print(groups[i])
#         group_numerical = [int(i) for i in groups[i]]
#         # print(group_numerical)
#         products_final.append(math.prod(group_numerical))
#         print(products_final)
#     return max(products_final)


# longNum = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
# print(problem8(longNum))

def problem8(num):  
    num_str = str(num)
    holder,results = 1, []
    for i in range(0,len(num_str),1):
        selection = num_str[i:i+12]
        # print(selection)
        if "0" in str(selection):
            pass
        else:
            maximum = math.prod([int(i) for i in selection])
            if maximum > holder:
                holder = maximum
            else:
                pass
    return maximum

longNum = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
# print(problem8(longNum))

#Problem 9 - Correctly Solved, albeit bad code
# https://projecteuler.net/problem=9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def problem9():
    for a in range(1,1000):
        for b in range(1,1000):
            for c in range(1,1000):
                if (a + b + c == 1000) and (a**2 + b**2 == c**2):
                    return a * b * c
# print(problem9())

#PROBLEM 10 - Solved Correctly
# https://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def problem10(N):
    #For this problem, I'll utilize the Sieve of Eratosthenes to yield my primes
    primeArray = []
    prime = [True for i in range(N + 1)]
    p = 2
    while (p * p <= N):

        #if prime[p] is not changed, then it's prime
        if (prime[p] == True):
            #Update for all multiples of P
            for i in range(p * p, N + 1, p):
                prime[i] = False
        p += 1
    #Append Primes:
    for p in range(2, N + 1):
        if prime[p]:
            primeArray.append(p)
    
    return sum(primeArray)

# print(problem10(2_000_000))


#Problem 14
# https://projecteuler.net/problem=14
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

def problem14(target):
    counter, results,values = 0, [],[]
    for i in range(target,1,-1):
        n = i
        while n > 1:
            if n % 2 == 0:
                n = n / 2
                counter += 1
            else:
                n = (3 * n) + 1
                counter += 1
        results.append(counter)
        if counter > results[len(results) - 2]:
            values.append(i)
        counter = 0
    return max(values)

# print(problem14(999999))

#PROBLEM 20 - Correctly Solved
# https://projecteuler.net/problem=20
# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
import math
def problem20(target):
    values = sum([int(i) for i in str(math.factorial(100))])
    return values

# print(problem20(100))


#Problem 36 - Correctly Solved
# https://projecteuler.net/problem=36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def problem36(target):
    results = []
    for i in range(1,target):
        if (str(i) == str(i)[::-1]) and (str(bin(i)[2:]) == str(bin(i)[:1:-1])):
            results.append(i)
    return sum(results)
    

# print(problem36(1_000_000))


#PROBLEM 49
# https://projecteuler.net/problem=49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
# is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
# but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?

def problem49(floor):
    four_d_primes = []
    for i in range(1000,9999,1):
        for j in range(2,int(i / 2) + 1):
            if i % j == 0:
                break
        else:
            four_d_primes.append(i)
    sorted_nums = [sorted(str(i)) for i in four_d_primes]
    

    return
# print(problem49(1000))


#PROBLEM 97 

# value = (28433 * 2**7830457) + 1
# value2 = 100100100100100100

def problem97(N):
    num = "".join([i for i in str(N)])
    return len(num) / 1_000_000

# print(problem97(value))