baris = int(input("Masukkan jumlah baris: "))
if baris % 2 == 0:    
    for m in range(1, baris//2+1):
        print(" "*(baris//2-m) + "*"*(2*m-1))
    for m in range(baris//2, 0,-1):
        print(" "*(baris//2-m) + "*"*(2*m-1))
          
if baris%2==1:
    for m in range(1, baris//2+2):
        print(" "*(baris//2-m+1)+"*"*(2*m-1))
    for m in range(baris//2,0,-1):
        print(" "*(baris//2-m+1)+ "*"*(2*m-1))
        
        