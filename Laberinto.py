muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
laberinto = [[]] * 5
print(muro[1][1])
for i in range(5):
    laberinto[i].append("X")
print(laberinto)