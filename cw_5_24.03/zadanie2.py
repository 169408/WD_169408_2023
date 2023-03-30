import numpy as np

a = np.random.randint(10, high=50, size=(3,3))
b = np.random.randint(10, high=50, size=(4,4))

print(a)
for i in range(3):
    print("Dla wiersza nr ", i+1, "najnizsza wartosc - ", np.amin(a, axis=1)[i])
    print("Dla kolumny nr ", i+1, "najnizsza wartosc - ", np.amin(a, axis=0)[i])
print(b)
for j in range(4):
    print("Dla wiersza nr ", j+1, "najnizsza wartosc - ", np.amin(b, axis=1)[j])
    print("Dla kolumny nr ", j+1, "najnizsza wartosc - ", np.amin(b, axis=0)[j])

