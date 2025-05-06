# Project-HashGuard---Python3
Projek ini adalah tugas mata kuliah kriptografi.
HashGuard adalah aplikasi desktop untuk menghasilkan dan memverifikasi checksum file menggunakan algoritma
SHA-256. Aplikasi ini berguna untuk memastikan bahwa file tidak dimodifikasi selama pengiriman atau penyimpanan

Sebelum menjalankan aplikasi, anda harus terlebih dahulu menyiapkan alat tempurnya ya gaes
1. Aplikasi Python versi terbaru. Download disini https://www.python.org/
2. Pastikan di komputer kalian mempunyai pip versi terbaru. Gunanya adalah perintah untuk menginstall package python yang dibutuhkan saat menjalankan aplikasi.
   Caranya ada disini https://pip.pypa.io/en/stable/installation/.
3. Jika alat tempurnya sudah, silahkan download source code HashGuard ini di komputer kalian, kemudian jalankan.


Package yang perlu di install
1. Pillow => pip install Pillow
2. Tkinter => pip install tkinter
3. hashlib
Biasanya sih yang nomor 2 sama 3 akan otomatis keinstall ketika sudah memasang python.😁😁


📜 Flow Lengkap HashGuard
1. Generate Checksum
   - Pilih dokumen.
   - Generate hash SHA-256.
   - Simpan hash ke file .txt di folder data/saved_hashes/.

2. Verifikasi Dokumen
   - Pilih dokumen yang ingin dicek.
   - Pilih file hash .txt.
   - Bandingkan hash dokumen dan hash dari file.

3. Tampilkan hasil:
   - ✅ Cocok ➔ Dokumen ASLI.
   - ❌ Tidak cocok ➔ Dokumen SUDAH BERUBAH.

4. Lihat Riwayat Hash
   - Klik "Lihat Riwayat Hash".
   - Tampilkan semua hash yang pernah disimpan ke layar.

🔥 Yang Sudah Selesai:
✅ Coding fitur utama.
✅ Testing awal masing-masing fitur.
✅ Struktur folder rapi (data/saved_hashes/).
✅ Logika aplikasi sudah jalan stabil.


🛡Struktur Aplikasi HashGuard🛡

HashGuard/
│
├── data/               # Folder untuk menyimpan file hash
    └── saved_hashes
├── img/                # Folder untuk menyimpan gambar background dan lainnya
    └── bg2.jpg     
├── hash_util.py        # utilitas yang digunakan untuk meng-generate checksum file
├── main.py             # aplikasi

