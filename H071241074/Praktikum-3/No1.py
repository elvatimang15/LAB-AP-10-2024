a = int(input("Masukkan Jumlah Baris: "))

if a % 2 == 0:
        i = 1
        while i <= a:
            j = 1
            print('  ' * ((a - i) // 2), end='')
            while j <= i:   
                print(f"*", end=' ')
                j += 1
            print("")
            i+=2

        i = a - 1
        while i >= 1:
            j = 1
            print('  ' * ((a - i) // 2), end='')
            while j <= i:   
                print(f"*", end=' ')
                j += 1
            print("")
            i -= 2

else:
        
        i = 1
        while i <= a:
            j = 1
            print('  ' * ((a - i) // 2), end='')
            while j <= i:   
                print(f"*", end=' ')
                j += 1
            print("")
            i+=2

        i = a - 2
        while i >= 1:
            j = 1
            print('  ' * ((a - i) // 2), end='')
            while j <= i:   
                print(f"*", end=' ')
                j += 1
            print("")
            i -= 2