# Buatlah program untuk menampilkan bilangan bulat 1 s/d 100 yang merupakan kelipatan 3.

for i in range (1, 100, 3):
    i = i + 2
    print(i)

# Bisa juga seperti ini
for i in range (100):
    bil = i + 1
    # Dengan metode modulo
    if bil % 3 == 0:
        print(bil)

        