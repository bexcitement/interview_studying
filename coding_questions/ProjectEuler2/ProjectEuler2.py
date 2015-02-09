def sumEvenFib(n):
    fib_list = [1,2]
    total = 2
    i = 2
    
    while True:
        current_value = fib_list[i-1] + fib_list[i-2]
        if n < 2:
            total = 0
            break 
        elif current_value < n:
            fib_list.append(current_value)

            if current_value % 2 == 0: 
                total += current_value
        else:
            break
        
        i+=1
    
    return total 

print sumEvenFib(4000000)
