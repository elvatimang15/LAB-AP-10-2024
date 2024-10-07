#Nomor 1
def kata_terpanjang(kalimat):
     kata_list = kalimat.split()
     kata_terpanjang = max(kata_list, key=len)
     return kata_terpanjang

kalimat = input("Kalimat: ")
print("Kata terpanjang: ",kata_terpanjang(kalimat))

#Nomor 2
def tukar_huruf(string):
    return string.swapcase()

string = input("string: ")
print("hasil: ", tukar_huruf(string))
               



