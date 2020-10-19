primos =  []

for x in range (1,100):
    cont = 1
    for y in range (x, x+1):
        if x % y == 2:
            cont +=1
    if cont <=2:
        primos.append(x)
print(primos)        
