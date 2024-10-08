# no 1
kalimat = input("Kalimat: ")
def tes(kalimat):
    pemisahan = kalimat.split()
    kata_terpanjang = ""  
    
    for kata in pemisahan:  
        if len(kata) > len(kata_terpanjang):  
            kata_terpanjang = kata  
    return kata_terpanjang  
    
print(f"Kata terpanjang: {tes(kalimat)}")


#  no 2
string = input("Tukar huruf: ")
tukarhuruf = string.swapcase()
print(tukarhuruf)


