def Is_A_Perfect_Number(n):
    total = 0
    for x in range(1,n):
        if n%x==0:
            total += x
    return total == n 
number = int(input('Enter number: '))

if Is_A_Perfect_Number (number):
    print('%d is Perfect' % (number))
else:
    print('%d is NOT Perfect' %(number))


def Is_An_Abundant_Number(n):
    total = 0
    is_abundant = 0
    for x in range(1,n):
        if n%x==0:
        total = total + x
        if(total > n):
            is_abundant=1
number = int(input('Enter number: '))
if(total > n) or (is_abundant ==1))
    print('%d is Abundant' % (number))
else:
    print('%d is NOT Abundant' %(number))
