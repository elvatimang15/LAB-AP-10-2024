import re

def is_vip(name):
    return name[0].lower() in "aeiou" 

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' 
    return re.match(email_pattern, email) is not None

def main():
    pengunjung = [] 
    email_set = set()  
    total_pengunjung = 0  
    
    while True: 
        name = input("Masukkan nama tamu (ketik selesai untuk berhenti): ")
        if name.lower() == "selesai":
            break
        
        email = input(f"Masukkan email untuk {name}: ")
        while not is_valid_email(email):
            print("Email tidak valid, coba lagi.")
            email = input(f"Masukkan email untuk {name}: ")

        pengunjung.append((name, email))
        email_set.add(email)  

        if is_vip(name):
            print(f"{name} adalah peserta VIP!")
        else:
            print(f"{name} bukan peserta VIP.")
        
        total_pengunjung += 1 

    print(f"\nTotal pengunjung yang mendaftar: {total_pengunjung}")
    
    print("\nDaftar pengunjung (diurutkan berdasarkan nama):")
    for name, email in sorted(pengunjung, key=lambda x: x[0]):
        print(f"{name} - {email}")
    
    print("\nEmail unik yang terdaftar:")
    for email in email_set:
        print(email)

if __name__ == "__main__":
    main()
