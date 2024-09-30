def hitung_langkah(n):
    langkah = [] 

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        
        langkah.append(float(n))  
    return langkah

def main():
    try:
        n = int(input("Masukan angka: "))
        if n <= 0:
            print("Input tidak Valid")
            return
        
        langkah = hitung_langkah(n) 
        for step in langkah:
            print(step)

        print(f"Jumlah langkah: {len(langkah)}")  

    except ValueError:
        print("Input tidak Valid")

main()
