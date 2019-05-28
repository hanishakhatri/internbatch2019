from common import prime

if __name__=="__main__":
    num=int(input("enter a number :"))
    if prime(num):
        print(f"{num} is prime :")
    else:
        print(f"{num} is  not prime")
