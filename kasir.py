# Program Kasir Sederhana
# Dibuat untuk latihan variabel, tipe data, dan operator

print("=== KASIR MINI ===")

# Input
nama = input("Nama barang: ")
harga = int(input("Harga satuan: "))
jumlah = int(input("Jumlah beli: "))
diskon_persen = float(input("Diskon (%): "))

# Proses
total = harga * jumlah
diskon = total * diskon_persen / 100
bayar = total - diskon

# Output
print("\n--- RINCIAN BELANJA ---")
print(f"{nama} x{jumlah}")
print(f"Total  : Rp{total:,.0f}")
print(f"Diskon : Rp{diskon:,.0f}")
print(f"Bayar  : Rp{bayar:,.0f}")
print("Terima kasih sudah berbelanja!")
