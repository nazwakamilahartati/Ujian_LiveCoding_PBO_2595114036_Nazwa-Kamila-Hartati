class PenilaianMahasiswa:
    def __init__(self, nim, nama, tugas, uts,uas):
        self.nim = nim
        self.nama = nama
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        
    def hitung_nilai_akhir(self):
        return (
            self.tugas * 0.3
            + self.uts * 0.3
            + self.uas * 0.4
        )
        
    def tentukan_grade(self):
        nilai = self.hitung_nilai_akhir()
        
        if nilai >= 85:
            return "A"
        elif nilai >= 75:
            return "B"
        elif nilai >= 65:
            return "C"
        elif nilai >= 50:
            return "D"
        else:
            return "E"
        
    def cek_status(self):
        if self.hitung_nilai_akhir() >= 65:
            return "LULUS"
        else:
            return "TIDAK LULUS"
        
    def tampilkan_hasil(self):
        print("\nHASIL AKADEMIK")
        print("NIM: ", self.nim)
        print("Nama: ", self.nama)
        print("Nilai Akhir: ", format(self.hitung_nilai_akhir()), ".2f")
        print("Grade: ", self.tentukan_grade())
        print("status: ", self.cek_status())
        
try:
    print("SISTEM PENILAIAN")
    
    nim = input("NIM: ")
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    
    if (tugas < 0 or tugas > 100 or
        uts < 0 or uts > 100 or
        uas < 0 or uas > 100):
        print("Nilai harus antara 0 sampai 100")
    else:
        mahasiswa = PenilaianMahasiswa(nim, nama, tugas, uts, uas)
        mahasiswa.tampilkan_hasil()
        
except ValueError:
    print("Nilai harus berupa angka")