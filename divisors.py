#Sarah Forde
#17/02/2025
#divisors.py

def divisors(n):
    divisors_list = []
    for i in range (1,n):
        if n% i == 0:
            divisors_list.append(i)
    return divisors_list

print(divisors(30))
