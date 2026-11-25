# Program Menghitung Indeks Massa Tubuh (BMI)
# Tinggi badan dimasukkan dalam sentimeter

print("=== HITUNG BMI ===")

# Input
berat = float(input("Berat (kg): "))
tinggi_cm = float(input("Tinggi (cm): "))

# Proses
tinggi_meter = tinggi_cm / 100
bmi = berat / (tinggi_meter ** 2)

# Output
print("\n--- HASIL BMI ---")
print(f"BMI kamu: {bmi:.2f}")
