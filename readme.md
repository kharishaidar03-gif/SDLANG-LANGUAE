# 🌀 SDLANG (Sekolah Dasar Language)

**SDLANG** adalah bahasa pemrograman edukatif yang dirancang khusus untuk dijalankan di lingkungan **Termux**. Bahasa ini memiliki sintaksis unik yang mengadaptasi suasana sekolah dasar di Indonesia, bertujuan untuk mempermudah pembuatan **Game Edukasi** dan **Simulasi Ujian Digital**.

---

## 🚀 Fitur Utama
* **Sintaksis Lokal:** Menggunakan istilah yang akrab di telinga siswa (BEL MASUK, TULIS, SOAL, dll).
* **Sistem Pelajaran Dinamis:** Mendukung penggantian konteks ujian menggunakan perintah `IMPORT [NAMA_PELAJARAN]`.
* **Skor Otomatis:** Menghitung nilai jawaban benar secara real-time.
* **Ringan:** Dibuat dengan Python, sangat cepat dijalankan di Termux.

---

## 🛠️ Kamus Sintaksis

| Perintah | Deskripsi |
| :--- | :--- |
| `BEL MASUK` | Membuka program (Wajib di awal). |
| `IMPORT [NAMA]` | Menentukan mata pelajaran yang sedang diuji (Contoh: IMPORT IPA). |
| `TULIS "[teks]"` | Menampilkan pesan dari Guru ke layar. |
| `SOAL "[tanya]" KUNCI "[jawaban]"` | Membuat soal interaktif dan menentukan jawaban benar. |
| `UMUMKAN` | Menampilkan Rapor (Skor Akhir) di layar. |
| `ISTIRAHAT` | Menutup program. |

---

## 💻 Cara Instalasi (Termux)

1. **Siapkan Folder:**
   Pastikan file `sdlang.py` dan file script `.sd` kamu berada dalam satu folder.

2. **Jalankan Script:**
   Pastikan Python sudah terinstal di Termux (`pkg install python`), lalu jalankan:
   ```bash
   python sdlang.py belajar.sd
