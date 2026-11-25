# Program Konversi Suhu
# Mengubah Celsius ke tiga satuan suhu lainnya

print("=== KONVERSI SUHU ===")

# Input
celsius = float(input("Suhu (Celsius): "))

# Proses
fahrenheit = celsius * 9 / 5 + 32
reamur = celsius * 4 / 5
kelvin = celsius + 273.15

# Output
print("\n--- HASIL KONVERSI ---")
print(f"Fahrenheit : {fahrenheit}")
print(f"Reamur     : {reamur}")
print(f"Kelvin     : {kelvin}")
