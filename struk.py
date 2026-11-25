# Tantangan Opsional: Struk Dua Barang
# Menghitung subtotal dua barang dalam satu transaksi

print("=== STRUK BELANJA DUA BARANG ===")

# Input
barang1 = input("Barang 1: ")
harga1 = int(input("Harga 1: "))
jumlah1 = int(input("Jumlah 1: "))

barang2 = input("Barang 2: ")
harga2 = int(input("Harga 2: "))
jumlah2 = int(input("Jumlah 2: "))

# Proses
subtotal1 = harga1 * jumlah1
subtotal2 = harga2 * jumlah2
total = subtotal1 + subtotal2

# Output
print("\n========== STRUK ==========")
print(f"{barang1} x{jumlah1} = Rp{subtotal1:,.0f}")
print(f"{barang2} x{jumlah2} = Rp{subtotal2:,.0f}")
print("---------------------------")
print(f"TOTAL = Rp{total:,.0f}")
print("===========================")
print("Terima kasih!")
