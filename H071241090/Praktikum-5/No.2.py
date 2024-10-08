def acronym (kalimat) :
    kalimatPisah = kalimat.split()
    
    acronym = ''.join(kata[0].upper() for kata in kalimatPisah)
    
    return acronym

print(acronym("universitas indonesia")) 
print(acronym("bank nasional indonesia"))
