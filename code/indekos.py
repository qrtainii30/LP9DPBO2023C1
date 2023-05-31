from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, no_kamar, hargaperBulan):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.no_kamar = no_kamar
        self.hargaperBulan = hargaperBulan
        

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_summary(self):
        return "Hunian Indekos."
    
    def get_no_kamar(self):
        return self.no_kamar
    
    def get_hargaperBulan(self):
        return self.hargaperBulan
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nNomor Kamar : " + str(self.no_kamar) + "\nHarga Per Bulan : " + str(self.hargaperBulan) + "\n"