print("menghitung nilai akhir mahasiswa")
print("=" * 40)

nama = input("masukan nama anda:")
nim = input("masukan nim anda:")

bobotUts = float(input("masukan bobot uts (dalam persentase):"))
bobotUas = float(input("masukan bobot uas (dalam persentase):"))
bobotTugas = float(input("masukan bobot tugas (dalam persentase):"))
bobotProyek = float(input("masukan bobot proyek (dalam persentase):"))

nilaiUts = float(input("masukan nilai uts:"))
nilaiUas = float(input("masukan nilai uas:"))
nilaitugas = float(input("masukan nilai tugas:"))
nilaiproyek = float(input("masukan nilai proyek:"))

hasilUts = nilaiUts * bobotUts / 100
hasilUas = nilaiUas * bobotUas / 100
hasilTugas = nilaitugas * bobotTugas / 100
hasilProyek = nilaiproyek * bobotProyek / 100

print("mahasiswa yang bernama " + nama + " " + "(NIM: " + nim + ")")
print("dengan nilai presentasi yang di hasilkan")

print("Nilai UTS: " + str(hasilUts))
print("Nilai UAS: " + str(hasilUas))
print("Nilai Tugas: " + str(hasilTugas))
print("Nilai Proyek: " + str(hasilProyek))

print("nilai akhir yang diperoleh oleh mahasiswa " + nama + " " + "(NIM: " + nim +")"
+ ": " + str(hasilUts + hasilUas + hasilTugas + hasilProyek))