def langkah_aman(jarak):
    if jarak > 20:
        print("Langkah ini berbahaya! Jaraknya lebih dari 20 meter.")
        return False  # bahaya
    return True  # aman

def input_valid(jarak):
    if jarak >= 0:
        return True
    print("Masukkan tidak valid. Harap masukkan angka positif atau 0 untuk berhenti.")
    return False

def main():
    total_jarak = 0
    bahaya = False  # untuk mengecek apakah ada bahaya
    
    print("Selamat datang di petualangan mencari harta karun!")
    
    while True:
        try:
            langkah = float(input("Masukkan jarak langkah (meter) atau 0 untuk berhenti: "))
        except ValueError:
                print("Input tidak valid. Masukkan angka.")
                continue
        
        # Jika langkah yg dimasukkan adalah 0 atau minus maka loop berhenti
        if langkah < 0:
                print("angka minus tidak diperbolehkan.")
                break
            
        if langkah == 0:
            break
  
        if not langkah_aman(langkah):
            bahaya = True
        
        #tambahkan jarak langkah ke total jika aman
        total_jarak += langkah
        
        if total_jarak == 50:
            print("Anda telah mencapai 50 meter!")
            if bahaya:
                print("Namun, Anda telah melakukan langkah yang berbahaya.")
                print("Tidak disarankan untuk menggali harta karun.")
            else:
                print("Tidak ada bahaya terdeteksi. Anda dapat menggali untuk menemukan harta karun!")
            break
        
    # jika pemain berhenti sebelum 50 meter
    if total_jarak < 50:
        print(f"Anda berhenti setelah menempuh {total_jarak} meter.")
        if bahaya:
            print("Langkah Anda berbahaya. Tidak disarankan untuk menggali.")
        else:
            print("Anda aman, tetapi belum mencapai 50 meter. Tidak ada harta karun di sini.")
            
        
    print("Petualangan selesai. Terima kasih telah bermain!")

main()

# def langkah_aman():
#     total_jarak = 0
    
#     while True:
#         try:
#             langkah = float(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
            
#             if langkah < 0: #jika input nya minus
#                 print("Input tidak valid. Program berhenti.")
#                 break

#             if langkah == 0:
#                 print("permainan dihentikan.")
#                 break
#             elif total_jarak == 50:
#                 print("Aman. Kamu tepat menggali harta karun.")
#             elif total_jarak < 50:
#                 print("Tidak menemukan harta karun. Coba lagi")
#             else:
#                 print("Tidak aman untuk menggali harta karun, Coba lagi!")
#                 break
            
#             total_jarak += langkah
            
#             if langkah > 20:
#                 print("Langkah berbahaya. Tidak aman untuk menggali harta karun, coba lagi")
        
#         except ValueError:
#             print("Input tidak valid. Silahkan masukkan angka.")

#     print(f"Total jarak yang telah ditempuh: {total_jarak} meter")

# langkah_aman()
