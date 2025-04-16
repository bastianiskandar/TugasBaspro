matriks1 = []
matriks2 = []

print("\nMasukkan elemen Matriks 1:")
for i in range(5):
    baris = []
    for j in range(5):
        elemen = int(input(f"Matriks 1 [{i+1}][{j+1}] = "))
        baris.append(elemen)
    matriks1.append(baris)

print("\nMasukkan elemen Matriks 2:")
for i in range(5):
    baris = []
    for j in range(5):
        elemen = int(input(f"Matriks 2 [{i+1}][{j+1}] = "))
        baris.append(elemen)
    matriks2.append(baris)

hasil = []
for i in range(5):
    baris_hasil = []
    for j in range(5):
        total = 0
        for k in range(5):
            total += matriks1[i][k] * matriks2[k][j]
        baris_hasil.append(total)
    hasil.append(baris_hasil)

print("\nHasil Perkalian Matriks 5x5:")
for baris in hasil:
    print(baris)