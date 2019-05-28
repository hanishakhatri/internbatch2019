def prime(num):
    for  check in range(2,num//2+1):
             if num % check ==0:
                return False
             else :
                return True



def armstrong(num):
    p=len(str(num))
    s=0
    temp=num

