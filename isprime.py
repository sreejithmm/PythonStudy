def is_prime(x):
    prime = True
  
    if (x == 0 or x == 1):
        return False
    if(x < 0):
        x= x*-1
   
    for num in range(2,x-1):
        if x%num== 0:
            return False
    return prime

print is_prime(-7)
