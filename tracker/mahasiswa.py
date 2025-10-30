class Mahasiswa:
    """Representasi data mahasiswa dengan enkapsulasi atribut kehadiran."""

    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self._hadir_persen = 0.0

    @property
    def hadir_persen(self):
        return self._hadir_persen

    @hadir_persen.setter
    def hadir_persen(self, value):
        if value < 0 or value > 100:
            raise ValueError("Persentase Hadir harus 0–100.")
        self._hadir_persen = float(value)

    def info(self):
        """Kembalikan informasi singkat mahasiswa."""
        return f"{self.nim} - {self.nama} ({self.hadir_persen:.2f}%)"

