import re

def validasi_ipv4(ip):
    pola = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if pola.match(ip):
        oktet = list(map(int, ip.split('.')))
        return all(0 <= oktet[i] <= 255 for i in range(4))
    return False

def validasi_ipv6(ip):
    pola = re.compile(r'^[0-9a-fA-F:]{1,39}$')
    if pola.match(ip):
        segmen = ip.split(':')
        if len(segmen) > 8:
            return False
        return True
    return False

def klasifikasi_alamat_ip(N, alamat_ip):
    hasil = []
    for ip in alamat_ip:
        if validasi_ipv4(ip):
            hasil.append("IPv4")
        elif validasi_ipv6(ip):
            hasil.append("IPv6")
        else:
            hasil.append("Bukan IP Address")
    return hasil


N = int(input("Masukkan jumlah baris: "))
alamat_ip = [input("Masukkan alamat IP: ") for _ in range(N)]


hasil = klasifikasi_alamat_ip(N, alamat_ip)
for result in hasil:
    print(result)

