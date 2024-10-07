def enkripsi(text, shift):
    hasil = []
    
    for char in text:
        if 'a' <= char <= 'z':
            geser = (ord(char) - ord('a') + shift) % 26 + ord('a')
            hasil.append(chr(geser))
        elif 'A' <= char <= 'Z':
            geser = (ord(char) - ord('A') + shift) % 26 + ord('A')
            hasil.append(chr(geser))
        else:
            hasil.append(char)
    
    return ''.join(hasil)


text = input("Masukkan String: ")
shift = int(input("Masukkan jumlah pergeseran: "))

cipher = enkripsi(text, shift)

print(f"Text    : {text}")
print(f"Shift   : {shift}")
print(f"Cipher  : {cipher}")