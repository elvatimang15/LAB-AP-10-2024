# NOMOR 1
def kata_terpanjang(kalimat):
    kata_terpanjang = kalimat.split()
    return max(kata_terpanjang, key = len)
    
kalimat = input("masukkan kalimat: ")
print(f"kata terpanjang: {kata_terpanjang(kalimat)}")