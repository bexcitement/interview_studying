# helper function to check if an integer is prime
def isPrime(n):
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if n % 2 == 0:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def sumPrimes():
	num_list = []
	i = 0

	while len(num_list) < 1000:
		if isPrime(i) == True:
			num_list.append(i)
	        i +=1
	return sum(num_list)

print sumPrimes()
