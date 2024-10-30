import re

ipv4_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"  
ipv6_pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"  

N = int(input("Masukkan jumlah baris: "))

for _ in range(N):
    line = input().strip()  # input() untuk ambil input per baris, .strip() untuk hilangkan spasi di awal/akhir
    if re.match(ipv4_pattern, line):
        parts = line.split('.') 
        #line.split() untuk memisahkan string line menjadi beberapa bagian (substrings) berdasarkan titik (.) sebagai pemisah
        if all(0 <= int(part) <= 255 for part in parts):
            print("IPv4")
        else:
            print("Bukan IP Address")
    elif re.match(ipv6_pattern, line):
        print("IPv6")
    else:
        print("Bukan IP Address")
