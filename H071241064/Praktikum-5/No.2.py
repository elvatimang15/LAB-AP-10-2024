def akronim(kalimat):
    kata_pisah = kalimat.split()

    singkatan = "".join(kata[0].upper() for kata in kata_pisah)
    return singkatan

input_kalimat = input("Masukkan kalimat: ")
hasil_akronim = akronim(input_kalimat)

print(f"{hasil_akronim}")