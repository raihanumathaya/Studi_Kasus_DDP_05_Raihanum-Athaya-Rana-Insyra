
def hitung_biaya_parkir(jenis_kendaraan, durasi):
    if jenis_kendaraan == "mobil":
        tarif = 5000
    elif jenis_kendaraan == "motor":
        tarif = 3000
    
    total_biaya = tarif * durasi 
    return total_biaya 

jenis_kendaraan= (input("mobil/motor? : "))
jam_masuk = int(input("Masukkan jam masuk :"))
jam_keluar = int(input("Masukkan jam keluar :"))

durasi = jam_keluar - jam_masuk

total_biaya = hitung_biaya_parkir(jenis_kendaraan, durasi)

print("durasi parkir: ", durasi, "jam")
print("total biaya parkir: ", total_biaya)