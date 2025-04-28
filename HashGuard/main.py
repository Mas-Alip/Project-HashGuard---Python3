import tkinter as tk
from tkinter import filedialog, messagebox
import os
from hash_util import hash_file, save_hash_to_file, read_hash_from_file, list_saved_hashes
from PIL import Image, ImageTk




def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    if selected_file:
        lbl_file.config(text=os.path.basename(selected_file))

def generate_checksum():
    if not selected_file:
        messagebox.showerror("Error", "Pilih dokumen terlebih dahulu!")
        return
    file_hash = hash_file(selected_file)
    save_hash_to_file(selected_file, file_hash)
    output.delete("1.0", tk.END)
    output.insert(tk.END, f"Hash berhasil disimpan untuk {os.path.basename(selected_file)}.\n")
    output.insert(tk.END, f"SHA-256:\n{file_hash}")

def select_hash_file():
    global selected_hash_file
    selected_hash_file = filedialog.askopenfilename()
    if selected_hash_file:
        lbl_hash.config(text=os.path.basename(selected_hash_file))

def verify_document():
    if not selected_file or not selected_hash_file:
        messagebox.showerror("Error", "Pilih dokumen dan file hash terlebih dahulu!")
        return
    file_hash = hash_file(selected_file)
    saved_hash = read_hash_from_file(selected_hash_file)
    output.delete("1.0", tk.END)
    if file_hash == saved_hash:
        output.insert(tk.END, "✅ Dokumen ASLI\n")
    else:
        output.insert(tk.END, "❌ Dokumen SUDAH BERUBAH\n")

def show_hash_history():
    hashes = list_saved_hashes('data/saved_hashes')
    output.delete("1.0", tk.END)
    if hashes:
        output.insert(tk.END, "=== Riwayat Hash ===\n\n")
        for idx, content in enumerate(hashes, start=1):
            output.insert(tk.END, f"{idx}. {content}\n\n")
    else:
        output.insert(tk.END, "Belum ada hash yang disimpan.")

# Fungsi untuk menambahkan gambar sebagai background
def set_background():
    # Cek apakah file gambar ada
    image_path = "img/bg2.png"
    if not os.path.exists(image_path):
        print(f"File gambar tidak ditemukan: {image_path}")
        return

    # Jika gambar ada, lanjutkan
    background_image = Image.open(image_path)
    background_image = background_image.resize((2000,1100))  # Sesuaikan dengan ukuran jendela
    background_photo = ImageTk.PhotoImage(background_image)
    
    # Membuat label dengan gambar background
    background_label = tk.Label(app, image=background_photo)
    background_label.place(relwidth=1, relheight=1)  # Menempatkan gambar pada seluruh jendela
    
    # Menyimpan foto untuk menghindari garbage collection
    background_label.image = background_photo


# GUI Setup
app = tk.Tk()

# Mengubah warna latar belakang aplikasi menjadi biru muda
app.title("HashGuard - Verifikasi Dokumen")
app.geometry("1000x700")

# Menambahkan background di canvas
set_background()

# Judul besar
title = tk.Label(app, text="HashGuard", font=("Arial", 24, "bold"))
title.pack(pady=10)

subtitle = tk.Label(app, text="Aplikasi Verifikasi Keaslian Dokumen", font=("Arial", 12))
subtitle.pack()

frame = tk.Frame(app)
frame.pack(pady=20)

selected_file = None
selected_hash_file = None

# Tombol-tombol
btn_select = tk.Button(frame, text="Pilih Dokumen", width=20, command=select_file)
btn_select.grid(row=0, column=0, padx=10, pady=5)

lbl_file = tk.Label(frame, text="Belum ada dokumen")
lbl_file.grid(row=0, column=1, padx=10)

btn_generate = tk.Button(frame, text="Generate Checksum", width=20, command=generate_checksum)
btn_generate.grid(row=1, column=0, padx=10, pady=5)

btn_select_hash = tk.Button(frame, text="Pilih File Hash", width=20, command=select_hash_file)
btn_select_hash.grid(row=2, column=0, padx=10, pady=5)

lbl_hash = tk.Label(frame, text="Belum ada file hash")
lbl_hash.grid(row=2, column=1, padx=10)

btn_verify = tk.Button(frame, text="Verifikasi Dokumen", width=20, command=verify_document)
btn_verify.grid(row=3, column=0, padx=10, pady=5)

btn_history = tk.Button(frame, text="Lihat Riwayat Hash", width=20, command=show_hash_history)
btn_history.grid(row=4, column=0, padx=10, pady=5)

# Output teks
output = tk.Text(app, height=15, width=80)
output.pack(pady=10)

# Footer
footer = tk.Label(app, text="© 2025 HashGuard Project", font=("Arial", 8))
footer.pack(pady=5)

app.mainloop()
