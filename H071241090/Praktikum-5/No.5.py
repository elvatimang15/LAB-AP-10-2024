def kriptografi(text, shift):
    encrypted_text = ""
    
    for huruf in text:
        if 'a' <= huruf <= 'z':
            encrypted_text += chr((ord(huruf) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= huruf <= 'Z':
            encrypted_text += chr((ord(huruf) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += huruf
    
    return encrypted_text

text = input("Masukkan string: ")
shift = input("Masukkan jumlah pergeseran: ")

if shift.isdigit():
    shift = int(shift)  
    print(f"Text: {text}")
    print(f"Shift: {shift}")
    print(f"Cipher: {kriptografi(text, shift)}")
else:
    print("Shift harus berupa bilangan bulat positif.")
