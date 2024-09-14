x = float(input('masukkan nilai x: '))
y = float(input('masukkan nilai y: '))
z = (x**2 + y**2)**0.5

luas = x * y / 2
keliling = x + y + z

print(f'Luas permukaan {luas: .2f}')
print(f'Keliling {keliling: .2f}')