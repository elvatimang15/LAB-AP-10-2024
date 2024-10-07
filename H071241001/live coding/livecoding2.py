print("Pilih Gender Anda \n1.Pria\n2.Wanita")
gender= input("= ")
TB = int(input("Masukkan tinggi badan (cm): "))
BB = int(input("Masukkan berat badan (kg): "))

BMI = BB / (TB/100)**2

if gender == 1:
    if BMI >= 27:
        print(f"Anda tergolong Obese dengan {BMI:.2f}")
    elif BMI >= 24:
        print(f"Anda tergolong Overweight dengan {BMI:.2f}")
    elif BMI >= 18:
        print(f"Anda tergolong Normal dengan {BMI:.2f}")
    else:
        print(f"Anda tergolong Underweight dengan {BMI:.2f}")
        
else:
    if BMI >= 28:
        print(f"Anda tergolong Obese dengan {BMI:.2f}")
    elif BMI >= 24:
        print(f"Anda tergolong Overweight dengan {BMI:.2f}")
    elif BMI >= 17:
        print(f"Anda tergolong Normal dengan {BMI:.2f}")
    else:
        print(f"Anda tergolong Underweight dengan {BMI:.2f}")
        

        
