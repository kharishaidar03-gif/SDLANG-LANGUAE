import sys
import re

class SDLANG:
    def __init__(self):
        self.nilai_ujian = 0
        self.pelajaran = "Umum"

    def jalankan(self, script):
        baris = script.split('\n')
        
        if not any("BEL MASUK" in b for b in baris):
            print("GURU: Kamu belum mengucapkan 'BEL MASUK'!")
            return

        for l in baris:
            l = l.strip()
            if not l or l.startswith("//"): continue

            # --- DINAMIS IMPORT PELAJARAN ---
            if l.startswith("IMPORT"):
                self.pelajaran = l.replace("IMPORT ", "")
                print(f"[SISTEM]: Membuka Buku Pelajaran {self.pelajaran}...")

            # --- OUTPUT ---
            elif l.startswith("TULIS"):
                teks = re.findall(r'"(.*?)"', l)
                if teks: print(f"GURU: {teks[0]}")

            # --- SISTEM SOAL ---
            elif l.startswith("SOAL"):
                match = re.match(r'SOAL "(.*)" KUNCI "(.*)"', l)
                if match:
                    tanya, kunci = match.groups()
                    print(f"\n[{self.pelajaran}]")
                    user_ans = input(f"Pertanyaan: {tanya}?\nJawab: ")
                    
                    if user_ans.lower() == kunci.lower():
                        print("HASIL: Bagus! Jawaban kamu tepat.")
                        self.nilai_ujian += 25
                    else:
                        print(f"HASIL: Salah! Jawaban yang benar: {kunci}")

            # --- RAPOR ---
            elif l == "UMUMKAN":
                print(f"\n--- HASIL UJIAN {self.pelajaran.upper()} ---")
                print(f"Total Nilai: {self.nilai_ujian}")
                print("-" * 25)

    def run_file(self, filename):
        with open(filename, 'r') as f:
            self.jalankan(f.read())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        SDLANG().run_file(sys.argv[1])
