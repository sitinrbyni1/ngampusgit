# print('Numbers from 1 to 100:')
# for n in range(1, 101):
#     print(n, end=' ')


# #soal ketiga function untuk mengecek sebuah bilangan genap atau ganjil. 

# def cek_ganjil_genap(angka):

    # untuk mengecek apakah bilangan tersebut genap/ganjil, jika ganjil  maka skip menggunakan if else

for n in range(1, 101):
    if n % 2 == 0:
        continue
    else:
        print(n)