def urut_kata(s):
    panjang = len(s)
    huruf = []

    for i in range(panjang):
        for j in range(i + 1, panjang + 1):
            huruf.append(s[i:j])
    
    return huruf

kata = input("Input your string: ")
print("========================")

huruf = urut_kata(kata)
huruf.sort(key=len)  

for z in huruf:
    print(z)                            
