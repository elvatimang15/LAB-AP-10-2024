def substring(s):
    n = len(s)

    for panjang in range(1, n + 1):
        for i in range(n - panjang + 1):
            print(s[i:i + panjang])

string = input("Masukkan sebuah string: ")

substring(string)