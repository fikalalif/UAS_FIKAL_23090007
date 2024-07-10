class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def set_nama(self, nama):
        self.nama = nama

    def set_warna(self, warna):
        self.warna = warna

    def set_rasa(self, rasa):
        self.rasa = rasa

    def informasi(self):
        return f"Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"

class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def set_vitamin(self, vitamin):
        self.vitamin = vitamin

    def informasi(self):
        parent_info = super().informasi()
        return f"{parent_info}, Vitamin: {self.vitamin}"

mangga_objek = Mangga("Mangga", "Hijau", "Manis", "Vitamin C")

print(mangga_objek.informasi())

mangga_objek.set_nama("Mangga Harum Manis")
mangga_objek.set_warna("Kuning")
mangga_objek.set_rasa("Sangat Manis")
mangga_objek.set_vitamin("Vitamin A, Vitamin C")

print(mangga_objek.informasi())
