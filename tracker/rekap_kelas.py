from .mahasiswa import Mahasiswa
from .penilaian import Penilaian

class RekapKelas:
    """Mengelola data banyak mahasiswa dan nilai mereka."""

    def __init__(self):
        self._data = {}  # {nim: {'mhs': Mahasiswa, 'nilai': Penilaian}}

    def tambah_mahasiswa(self, nim, nama):
        if nim in self._data:
            raise KeyError("NIM sudah terdaftar.")
        self._data[nim] = {'mhs': Mahasiswa(nim, nama), 'nilai': Penilaian()}

    def set_hadir(self, nim, persen):
        self._data[nim]['mhs'].hadir_persen = persen

    def set_penilaian(self, nim, quiz=None, tugas=None, uts=None, uas=None):
        p = self._data[nim]['nilai']
        if quiz is not None: p.quiz = quiz
        if tugas is not None: p.tugas = tugas
        if uts is not None: p.uts = uts
        if uas is not None: p.uas = uas

    def predikat(self, skor):
        if skor >= 85: return "A"
        if skor >= 75: return "B"
        if skor >= 65: return "C"
        if skor >= 50: return "D"
        return "E"

    def rekap(self):
        hasil = []
        for nim, d in self._data.items():
            m, n = d['mhs'], d['nilai']
            akhir = n.nilai_akhir()
            hasil.append({
                'nim': nim,
                'nama': m.nama,
                'hadir': m.hadir_persen,
                'akhir': akhir,
                'predikat': self.predikat(akhir)
            })
        return hasil

