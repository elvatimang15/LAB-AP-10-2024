def tampilkan_substring(s):

    panjang = len(s)
    
    for panjang_substring in range(1, panjang + 1):
        for i in range(panjang - panjang_substring + 1):
            substring = s[i:i + panjang_substring]
            print(substring)

input_string = input("Masukkan sebuah string: ")
print("=============================")
tampilkan_substring(input_string)