def acronym(kalimat):
    return ''.join(x[0].upper() for x in kalimat.split())

hasil = acronym("negara kesatuan")
print(hasil)  


