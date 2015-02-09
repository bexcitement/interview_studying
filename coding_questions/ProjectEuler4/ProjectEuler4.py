# find the palidrome largest palidrome that is less then 1 million

def highestPali():
    # 998001 is 999 * 999 
    for num in reversed(xrange(998001)):
        num_str =str(num)
        reversed_num = str(num)[::-1]

        if num_str == reversed_num and int(num_str) % 999 == 0:
            return int(num_str)

print highestPali()
