# Soal 2
def treasure_hunt():
    total_distance = 0
    bahaya = False

    print("Selamat datang di permainan berburu harta karun!")
    
    while True:
        try:
            step = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
            
            if step < 0:
                print("Input tidak valid! Masukkan bilangan bulat.")
                continue
            
            if step == 0:
                break
            
            total_distance += step
            
            if step > 20:
                bahaya = True

            print(f"Total jarak: {total_distance} meter")

        except ValueError:
            print("Input tidak valid! Masukkan bilangan bulat.")
    
    print(f"Total jarak: {total_distance} meter")
    
    # Output keputusan dan keterangan bahaya setelah permainan selesai
    print("Ada bahaya:", "ya" if bahaya else "tidak")
    
    if total_distance == 50:
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    elif total_distance > 50:
        print("Keputusan: Tidak menemukan harta karun. Coba lagi!")
    else:
        print("Keputusan: Tidak menemukan harta karun. Coba lagi!")

# Jalankan program
if __name__ == "__main__":
    treasure_hunt()

