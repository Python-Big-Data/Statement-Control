# Buatlah program untuk menghitung banyaknya bilangan bulat 1 s/d 100 yang merupakan kelipatan 3

sum = 0
for i in range(100):
    if (i + 1) % 3 == 0:
        # Jika ini true maka akan masuk ke dalam variabel sum yang ada di bawah
        sum += 1

print("Banyaknya bilangan : " + str(sum))