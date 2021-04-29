class persegiPanjang:

    #Constructor
    def __init__(self,p,l):
        self.panjang = p
        self.lebar = l

#Enkapsulasi
    #Setter
    def ubahPanjang (self,p):
        self.panjang = p

    def ubahLebar (self,l):
        self.lebar = l
# End Enkapsulasi

    def hitungLuas(self):
        return self.panjang * self.lebar

    def hitungKeliling(self):
        return 2 * (self.panjang + self.lebar)

    def cetakLuas(self):
        print(f'Luas Persegi Panjang\t\t: {self.hitungLuas()}')

    def cetakKeliling(self):
        print(f'Keliling Persegi Panjang\t: {self.hitungKeliling()}')

objekPP = persegiPanjang(10, 8)

objekPP.cetakKeliling()

objekPP.cetakLuas()