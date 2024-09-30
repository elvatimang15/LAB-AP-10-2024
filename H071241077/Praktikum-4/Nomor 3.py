# Soal 3
def hitung_langkah(n):
    langkah = 0
    while n != 1:
        if n % 2 == 0:  # Jika n genap
            n //= 2
            print(f"{n}")  
        else:           # Jika n ganjil
            n = n * 3 + 1
            print(f"{n}")  
        langkah += 1
    return langkah

def main():
    try:
        n = float(input("Masukkan angka: "))

        if n <= 0:
            print("Input tidak Valid")
            return

        langkah = hitung_langkah(n)
        print(f"Jumlah langkah: {langkah}")

    except ValueError:
        print("Input tidak Valid")

if __name__ == "__main__":
    main()