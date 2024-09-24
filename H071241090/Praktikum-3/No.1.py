m = int(input("Masukkan Jumlah Baris: "))
n = m//2 

if m%2 == 0 :
    for i in range (n):
        for j in range (n,i,-1):
            print (" ", end=" ")
        for j in range (2*i+1):
            print ("*", end=" ")
        print ()
    for i in range (n-1,-1,-1):
        for j in range (n,i,-1):
            print (" ", end=" ")
        for j in range (2*i+1):
            print ("*", end=" ")
        print ()
else:
    for i in range (n):
        for j in range (n,i,-1):
            print (" ", end=" ")
        for j in range (2*i+1):
            print ("*", end=" ")
        print ()
    for i in range (n,-1,-1):
        for j in range (n,i,-1):
            print (" ", end=" ")
        for j in range (2*i+1):
            print ("*", end=" ")
        print ()   