# Program Kalkulator Tujuh Operator
# Menggunakan dua bilangan bulat

print("=== KALKULATOR 7 OPERATOR ===")

# Input
angka1 = int(input("Angka 1: "))
angka2 = int(input("Angka 2: "))

# Proses dan Output
print("\n--- HASIL PERHITUNGAN ---")
print(f"{angka1} + {angka2} = {angka1 + angka2}")
print(f"{angka1} - {angka2} = {angka1 - angka2}")
print(f"{angka1} * {angka2} = {angka1 * angka2}")

if angka2 != 0:
    print(f"{angka1} / {angka2} = {angka1 / angka2}")
    print(f"{angka1} // {angka2} = {angka1 // angka2}")
    print(f"{angka1} % {angka2} = {angka1 % angka2}")
else:
    print("Pembagian, pembagian bulat, dan modulus tidak bisa dilakukan dengan 0.")

print(f"{angka1} ** {angka2} = {angka1 ** angka2}")
