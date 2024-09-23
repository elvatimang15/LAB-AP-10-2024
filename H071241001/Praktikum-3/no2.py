import random

print("Selamat datang di permainan menebak angka!")  
print("Saya telah memilih angka antara 1 hingga 100.")  
print("Anda memiliki maksimal 5 percobaan untuk menebak angka tersebut.")  

angka_rahasia = random.randint(1,100)
percobaan = 0

maxpercobaan = 5    
        
while percobaan <= 5:
    answeruser = int(input("Masukkan tebakan anda: "))
    if answeruser == 0:
        break
    elif answeruser != angka_rahasia:
        if answeruser > angka_rahasia:
            print("Angka terlalu besar")
        elif answeruser < angka_rahasia:
            print("Angka terlalu kecil")
    else:
        print("Selamat anda menebak angka dengan benar")
        break
    
    percobaan += 1
    if percobaan == maxpercobaan:
        print("Masa percobaan anda telah habis")
        break
    