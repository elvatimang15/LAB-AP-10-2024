def clean_string(s):
    return ''.join(c for c in s if c.isalnum())

def minimum_anagram(str1, str2):
    str1 = clean_string(str1)
    str2 = clean_string(str2)

    hitung = [0] * 26  

    for char in str1:
        index = ord(char.lower()) - ord('a')  
        hitung[index] += 1

    for char in str2:
        index = ord(char.lower()) - ord('a')
        hitung[index] -= 1

    
    hapus = sum(abs(c) for c in hitung)

    return hapus


str1 = input("Masukkan string pertama: ")
str2 = input("Masukkan string kedua: ")

result = minimum_anagram(str1, str2)

print(f"Jumlah minimum penghapusan untuk membuat anagram: {result}")
