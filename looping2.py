# untuk mengecek apakah bilangan tersebut genap/ganjil, jika ganjil  maka skip menggunakan if else
for n in range(1, 101):
    if n % 2 == 0:
        continue
    else:
        print(n)