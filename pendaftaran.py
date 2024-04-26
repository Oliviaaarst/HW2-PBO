class Mahasiswa1:
    def __init__(self, nama_lengkap, alamat, tanggal_lahir, email, password):
        self.nama_lengkap = nama_lengkap
        self.alamat = alamat
        self.tanggal_lahir = tanggal_lahir
        self.email = email
        self.password = password

    def daftar(self):

        print("Pendaftaran berhasil untuk mahasiswa dengan nama:", self.nama_lengkap)

# Contoh penggunaan
# Input data pendaftaran
nama_lengkap = input("Masukan nama lengkap:")
alamat = input("Masukan alamat:")
tanggal_lahir = input("Masukan tanggal lahir (DD-MM-YYYY)")
email = input("Masukan email anda:")
pasword = input("Masukan password:")

mahasiswa_baru = Mahasiswa1(nama_lengkap, alamat, tanggal_lahir, email, pasword )
mahasiswa_baru.daftar()