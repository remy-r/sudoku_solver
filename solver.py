sudoku = "600837001089004700102000400000450020030609005040000860908006070700098010005100930"
sudoku_matrice = []
for i in range(9):
    sudoku_matrice.append(list(sudoku[i*9:(i+1)*9]))

for i in range(9):
    for j in range(9):
        if sudoku_matrice[i][j] == '0':
            sudoku_matrice[i][j] = '123456789'

while len("".join(sum(sudoku_matrice, []))) > 81:
    for i in range(9):
        for j in range(9):
            if len(sudoku_matrice[i][j]) == 1:
                # lignes
                for xj in range(9):
                    if j != xj and len(sudoku_matrice[i][xj]) > 1:
                        sudoku_matrice[i][xj] = sudoku_matrice[i][xj].replace(sudoku_matrice[i][j], '')

                # colonnes
                for xi in range(9):
                    if i != xi and len(sudoku_matrice[xi][j]) > 1:
                        sudoku_matrice[xi][j] = sudoku_matrice[xi][j].replace(sudoku_matrice[i][j], '')

                #carres
                for xi in range(3):
                    for xj in range(3):
                        xii = (i // 3) * 3 + xi
                        xjj = (j // 3) * 3 + xj
                        if i != xii and j != xjj and len(sudoku_matrice[xii][xjj]) > 1:
                            sudoku_matrice[xii][xjj] = sudoku_matrice[xii][xjj].replace(sudoku_matrice[i][j], '')
print("".join(sum(sudoku_matrice, [])) == '654837291389214756172965483896451327237689145541723869918346572723598614465172938')
print("".join(sum(sudoku_matrice, [])))