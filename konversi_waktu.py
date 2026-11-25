# Program Konversi Detik
# Mengubah total detik menjadi jam, menit, dan detik

print("=== KONVERSI WAKTU ===")

# Input
total_detik = int(input("Jumlah detik: "))

# Proses
jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

# Output
print("\n--- HASIL KONVERSI ---")
print(f"{jam} jam {menit} menit {detik} detik")
