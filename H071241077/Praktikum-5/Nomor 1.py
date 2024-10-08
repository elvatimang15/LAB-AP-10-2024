# Soal 1
kata = input("Masukkan kata: ")
kata = kata.replace(" ", "").lower()
palindrome = ''.join(reversed(kata))

if kata == palindrome:
    print("kata ini adalah palindrome")
else:
    print("kata ini bukan palindrome")
