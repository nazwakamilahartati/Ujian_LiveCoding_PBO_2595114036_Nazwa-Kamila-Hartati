class TransaksiKasir:
    def __init__(self, pelanggan, barang, harga, jumlah):
        self.pelanggan = pelanggan
        self.barang = barang
        self.harga = harga
        self.jumlah = jumlah
        
    def hitung_subtotal(self):
        return self.harga * self.jumlah
    
    def hitung_diskon(self):
        subtotal = self.hitung_subtotal()
        if subtotal >= 500000:
            return 15
        elif subtotal >= 250000:
            return 10
        elif subtotal >= 100000:
            return 5
        else:
            return 0
        
    def hitung_total(self):
        subtotal = self.hitung_subtotal()
        potongan = subtotal * self.hitung_diskon() / 100
        return subtotal - potongan
    
    def tampilkan_struk(self):
        subtotal = self.hitung_subtotal()
        diskon = self.hitung_diskon()
        potongan = subtotal * diskon / 100
        
        print("\n STRUK PEMBAYARAN")
        print("Pelanggan: ", self.pelanggan)
        print("Barang: ", self.barang)
        print("Subtotal: Rp", format(subtotal, ",.0f"))
        print("Diskon: ", diskon, "%")
        print("Potongan: Rp", format(potongan, ",.0f"))
        print("Total bayar: Rp", format(self.hitung_total(), ",.0f"))
        
try:
    print("KASIR MINIMARKET")
    
    pelanggan = input("Nama pelangan: ")
    barang = input("Nama Barang: ")
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))
    
    if harga <= 0 or jumlah <=0:
        print("Harga dan jumlah harus lebih dari o")
    else:
        transaksi = TransaksiKasir(pelanggan, barang, harga, jumlah)
        transaksi.tampilkan_struk()

except ValueError:
    print("Harga dan jumlah harus berupa angka")