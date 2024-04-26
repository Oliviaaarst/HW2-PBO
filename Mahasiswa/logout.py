class Mahasiswa:
    def __init__(self, nim, password): 
        self.nim = nim
        self.password = password
        self.logged_in = False

    def login(self, username, password):
        if self.nim == username and self.password == password:
            self.logged_in = True
            print("Login berhasil untuk mahasiswa dengan Nim:", self.nim)
        else:
            print("Login gagal. Nim atau kata sandi salah.")

    def logout(self):
        if self.logged_in:
            self.logged_in = False
            print("Logout Berhasil")
        else:
            print("Tidak ada yang login saat ini")

mahasiswa1 = Mahasiswa("422023025", "password1310")
mahasiswa1.login("422023025", "password1310")
mahasiswa1.logout()