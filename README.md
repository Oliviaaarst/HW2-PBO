# HW2-PBO

1. REQUIREMENT ANALYSIS

    A. Requirement Analysis untuk Ukrida Sisfo
    
    1. Otentikasi dan Otorisasi Pengguna:

        • Sistem harus dapat menyediakan fungsional login yang aman untuk mahasiswa, dosen, dan staf, untuk memastikan bahwa hanya pengguna yang berwenang yang dapat mengakses fitur tertentu berdasarkan peran mereka.

       • Prosesnya termasuk manajemen kata sandi, dan kontrol akses berbasis peran. 
    2. Pendaftaran:

       • Sistem harus dapat memfasilitasi proses pendaftaran bagi mahasiswa baru, untuk memungkinkan mereka memilih mata kuliah, melihat bagian yang tersedia, dan mendaftar di kelas.

       • Sistem juga harus menangani prasyarat, daftar tunggu, dan tenggat waktu pendaftaran.
    3. Manajemen Keuangan:

       • Sistem harus mendukung proses penagihan dan pembayaran untuk biaya kuliah, dan pengeluaran lainnya. Ini harus menghasilkan faktur, menyediakan opsi pembayaran, dan memelihara catatan transaksi keuangan.

       • Sitem harus terintegrasi dengan sistem akun virtual untuk pengumpulan pembayaran yang efisien. 
    4. Alat Komunikasi dan Kolaborasi:

       • Sistem harus menawarkan saluran komunikasi bagi mahasiswa, dosen, dan staf untuk berinteraksi, seperti pesan, forum, dan pengumuman.

       • Sistem juga harus mendukung pemberitahuan untuk pembaruan dan acara penting. 
    5. Akses Sumber Daya Akademik:

       • Sistem harus memberikan akses ke sumber daya akademik, seperti materi perkuliahan, buku teks, dan perpustakaan online.

       • Perpustakaan harus dapat berintegrasi dengan sistem perpustakaan universitas untuk menyediakan akses tanpa hambatan terhadap sumber daya digital dan fisik, termasuk fungsi pencarian dan hak peminjaman.
    6. Penilaian:

       • Sistem harus dapat mendukung proses penilaian dengan memungkinkan instruktur membuat dan mengelola tugas, kuis, ujian, dan bentuk evaluasi lainnya.

       • Sistem harus memfasilitasi penyerahan tugas, penilaian pekerjaan mahasiswa, dan pencatatan nilai.
    7. Layanan Dukungan Mahasiswa:

       • Sistem harus menyediakan akses ke layanan dukungan mahasiswa, termasuk bimbingan akademik, konseling, dan bimbingan karir.


B. Usecase stories

      Judul: Manajemen Data Mahasiswa dalam Sistem Informasi Akademik UKRIDA
      
      Deskripsi Singkat:
      Aplikasi Manajemen Data Mahasiswa dalam Sistem Informasi Akademik UKRIDA memungkinkan pengguna untuk melakukan operasi dasar terkait data mahasiswa, termasuk pendaftaran mahasiswa baru, pembaruan profil mahasiswa, penjadwalan bimbingan akademik, dan pencatatan absensi mahasiswa.

      Use Case Story:

      1. Pendaftaran Mahasiswa Baru:
          • Aktor: Calon Mahasiswa
          • Deskripsi: Calon mahasiswa ingin mendaftar sebagai mahasiswa baru di UKRIDA.
          • Langkah-langkah:
            1. Calon mahasiswa mengakses formulir pendaftaran melalui situs web atau aplikasi UKRIDA Sisfo.
            2. Calon mahasiswa mengisi formulir pendaftaran dengan informasi pribadi, riwayat pendidikan, dan pilihan program studi.
            3. Setelah mengisi formulir, calon mahasiswa mengirimkan permohonan pendaftaran.
            4. Tim pendaftaran universitas memproses permohonan dan memberikan status pendaftaran kepada calon mahasiswa.
      2. Pembaruan Profil Mahasiswa:
         • Aktor: Mahasiswa
         • Deskripsi: Mahasiswa ingin memperbarui informasi pribadi dan akademik mereka di sistem.
         • Langkah-langkah:
           1. Mahasiswa masuk ke portal Sisfo UKRIDA menggunakan kredensial mereka.
           2. Mahasiswa mengakses halaman profil mereka dan memilih opsi untuk memperbarui informasi.
           3. Mahasiswa memperbarui informasi yang diperlukan, seperti alamat, nomor kontak, atau program studi.
           4. Setelah pembaruan selesai, mahasiswa menyimpan perubahan dan sistem menyimpan data baru.
      3. Pencatatan Absensi Mahasiswa:
         • Aktor: Dosen
         • Deskripsi: Dosen ingin mencatat absensi mahasiswa dalam suatu kelas.
         • Langkah-langkah:
           1. Dosen membuka daftar absensi untuk kelas yang mereka ajarkan melalui sistem.
           2. Dosen memeriksa kehadiran mahasiswa dan mencatat absensi mereka.
           3. Sistem secara otomatis menyimpan catatan absensi dan memberikan laporan kepada dosen dan mahasiswa.
           4. Jika diperlukan, dosen dapat mengirimkan pemberitahuan kepada mahasiswa yang absen.
      4. Keluar dari Aplikasi:
         • Aktor: Pengguna (Mahasiswa, Dosen, atau Staff Administrasi)
         • Deskripsi: Pengguna ingin keluar dari aplikasi setelah selesai menggunakan fiturfiturnya.
         • Langkah-langkah:
           1. Pengguna menavigasi ke opsi "Keluar" yang tersedia di aplikasi atau situs web.
           2. Sistem mengonfirmasi keinginan pengguna untuk keluar dan melakukan proses logout.
           3. Pengguna dikeluarkan dari sesi mereka dan diarahkan ke halaman login jika ingin mengakses kembali aplikasi

2. USE CASE DIAGRAM
     ![Gambar tak berjudul (4)](https://github.com/Oliviaaarst/HW2-PBO/assets/151018674/e6ff1adc-dc47-4b36-a7ea-7debcfe12335)

3. DIAGRAM CLASS
    ![Gambar tak berjudul (3)](https://github.com/Oliviaaarst/HW2-PBO/assets/151018674/ec563ccb-a218-4a28-af0e-90323715c946)






