import re
user = input("Masukkan Username : ")
email = input("Masukkan Email : ")
password = input("Password Email : ")

def validasiusername(user):
    pattern = r'^[A-z0-9]{5,20}$'
    if re.fullmatch(pattern, user):
        return "Username Valid"
    else:
        return "Username Tidak Valid"

def validasiemail(email):
    pattern = r'^[a-z0-9]+[0-9]*@[a-z]+\.[a-z]{2,3}(\.[a-z]{2,3})?$'

    if re.fullmatch(pattern, email):
        return "Email valid"
    else:
        return "Email yang kamu input tidak valid. Registrasi gagal!"

def validasipassword(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'

    if re.fullmatch(pattern, password):
        return "Password valid"
    else:
        return "Password tidak valid"

print(validasiusername(user))
print(validasipassword(password))
print(validasiemail(email))



