#untuk mengecek apakah bilangan itu genap atau ganjil
def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "genap"
    else:
        return "ganjil"
#menggunakan looping for  untuk melakukan iterasi dari 1-100
for n in range(1, 101):
    hasil_cek = cek_ganjil_genap(n)
    print(n, "adalah bilangan", hasil_cek)