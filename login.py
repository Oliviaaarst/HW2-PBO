class UKRIDA:
    def __init__(self):
        
        self.user_data = {
            'mahasiswa1': 'password1',
            'mahasiswa2': 'password2',
            
        }

    def authenticate(self, username, password):
        
        if username in self.user_data:
            
            if self.user_data[username] == password:
                return True
        return False


def login():
    
    ukrida = UKRIDA()

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    
    if ukrida.authenticate(username, password):
        print("Login berhasil!")
        
    else:
        print("Username atau password salah.")


login()

