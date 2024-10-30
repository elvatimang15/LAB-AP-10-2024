import re

def cek_ip_address(n, alamat_list):
    hasil = []
    
    ipv4_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    ipv6_pattern = re.compile(r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$")
    
    for alamat in alamat_list:
        ipv4_match = ipv4_pattern.match(alamat)
        if ipv4_match:
            hasil.append("IPv4")
            continue
        
        ipv6_match = ipv6_pattern.match(alamat)
        if ipv6_match:
            hasil.append("IPv6")
            continue
    
        hasil.append("Bukan IP Address")
    
    return hasil

n = int(input("Masukkan nilai n : "))
alamat_list = []
for i in range (n) :
    alamat = input("Masukkan alamat IP : ")
    alamat_list.append(alamat)

hasil = cek_ip_address(n, alamat_list)
for hasil_deteksi in hasil:
    print(hasil_deteksi)
