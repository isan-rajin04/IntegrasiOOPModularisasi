from tracker import RekapKelas, build_markdown_report, save_text
import csv, os

def load_csv(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))

def bootstrap_data(rekap):
    att = load_csv("data/attendance.csv")
    grd = load_csv("data/grades.csv")
    by_nim = {g["student_id"]: g for g in grd}

    for row in att:
        nim, nama = row["student_id"], row["name"]
        rekap.tambah_mahasiswa(nim, nama)
        weeks = [k for k in row if k.startswith("week")]
        hadir = sum(int(row[w]) for w in weeks if row[w].strip())
        rekap.set_hadir(nim, round(hadir / len(weeks) * 100, 2))

        if nim in by_nim:
            g = by_nim[nim]
            rekap.set_penilaian(
                nim,
                quiz=float(g.get("quiz", 0)),
                tugas=float(g.get("assignment", 0)),
                uts=float(g.get("mid", 0)),
                uas=float(g.get("final", 0)),
            )

def tampilkan_rekap(rows):
    print("\nNIM        | Nama   | Hadir% | Akhir | Pred")
    print("--------------------------------------------")
    for r in rows:
        print("{:<10} | {:<6} | {:>6.2f} | {:>5.2f} | {}".format(
            r['nim'], r['nama'], r['hadir'], r['akhir'], r['predikat']
        ))
    print()

def main():
    r = RekapKelas()
    while True:
        print("=== Student Performance Tracker ===")
        print("1) Muat data dari CSV")
        print("2) Tambah Mahasiswa")
        print("3) Ubah Presensi")
        print("4) Ubah nilai")
        print("5) Lihat Rekap")
        print("6) Simpan laporan Markdown")
        print("7) Keluar")
        pilih = input("Pilih: ").strip()

        try:
            if pilih == "1":
                bootstrap_data(r)
                print("✅ Data dimuat.")
            elif pilih == "2":
                nim = input("NIM: ")
                nama = input("Nama: ")
                r.tambah_mahasiswa(nim, nama)
            elif pilih == "3":
                nim = input("NIM: ")
                hadir = float(input("Hadir (%): "))
                r.set_hadir(nim, hadir)
            elif pilih == "4":
                nim = input("NIM: ")
                q = float(input("Quiz: "))
                t = float(input("Tugas: "))
                u = float(input("UTS: "))
                a = float(input("UAS: "))
                r.set_penilaian(nim, quiz=q, tugas=t, uts=u, uas=a)
            elif pilih == "5":
                tampilkan_rekap(r.rekap())
            elif pilih == "6":
                md = build_markdown_report(r.rekap())
                os.makedirs("out", exist_ok=True)
                save_text("out/report.md", md)
                print("📄 Laporan sudah tersimpan di out/report.md")
            elif pilih == "7":
                break
            else:
                print("Pilihan tidak valid.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
 
