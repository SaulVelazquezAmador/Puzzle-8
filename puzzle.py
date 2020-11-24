print("Ingrese el estado inicial: ")

m = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        m[i][j] = input("-->")

for i in range(0,3):
    for j in range(0,3):
        print(m[i][j])