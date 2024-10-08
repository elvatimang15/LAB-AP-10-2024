def acronym(s):
    # Memisahkan kata-kata dalam string
    words = s.split()
    
    # Mengambil huruf pertama dari setiap kata dan menggabungkannya
    akronim = ''.join(word[0].upper() for word in words)
    
    print(akronim)

# Mengambil input dari pengguna
input_string = input("Masukkan kalimat: ")
acronym(input_string)
