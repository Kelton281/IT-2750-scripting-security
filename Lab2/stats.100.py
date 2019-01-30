def first100evensum(even,total):
    total = 0
    even = 2
    for i in range(1, 100, 1):
        if(i % even == 0):
            total += i
        return total
print(first100evensum)

def firstodd50(total1,odd):
    total1 = 0
    odd = 1
    for a in range(1, 50, 1):
        if (a % odd == 0):
            total1 += a
        return total1
print(firstodd50)

def first100avg(total2,avg):
    total2 = 0 
    for c in range(1, 100, 2):
        if (c %2!=0):
            total3 += c
        return total2
print(first100avg)

    
    
    



    




   
        

