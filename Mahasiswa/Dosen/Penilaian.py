class Penilaian2:
    def __init__(self, nama_mahasiswa):
        self.nama_mahasiswa = nama_mahasiswa
        self.nilai_tugas = 0
        self.nilai_quiz = 0
        self.nilai_ujian = 0

    def input_nilai(self):
        self.nilai_tugas = float(input("masukan nilai tugas:"))
        self.nilai_quiz = float(input("Masukan Nilai Quiz: "))
        self.nilai_ujian = float(input("Masukan nilai ujian: "))


    def hitung_nilai_akhir(self):
        nilai_akhir = (self.nilai_tugas * 0.3) + (self.nilai_quiz * 0.2) + (self.nilai_ujian * 0.5)
        return nilai_akhir
    

nama_mahasiswa = input("OLIVIA: ")
penilaian_mahasiswa = Penilaian2(nama_mahasiswa)
penilaian_mahasiswa.input_nilai()
nilai_akhir = penilaian_mahasiswa.hitung_nilai_akhir()

print("Nilai akhir untuk mahasiswa", nama_mahasiswa, "adalah", nilai_akhir)

