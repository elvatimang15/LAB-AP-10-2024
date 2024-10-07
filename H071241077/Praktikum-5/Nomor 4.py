# Soal 4
kata = input("Masukkan kata: ").upper()
substring = len(kata)
for i in range(substring):
    for j in range(i + 1, substring + 1):
        print(kata[i:j])