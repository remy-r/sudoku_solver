"""This module solves Sudokus

Sudoku_solver can solve easy sudokus

  Typical usage example:

  s = Solver('600837001089004700102000400000450020030609005040000860908006070700098010005100930')
  print(s.get_solution())

  # 654837291389214756172965483896451327237689145541723869918346572723598614465172938

"""


class Solver:
    """This class is use to solve Sudokus

    """
    def __init__(self, sudoku: str) -> None:
        self._check_input(sudoku)
        self.sudoku = sudoku
        self._organize_sudoku()
        self._solving()

    def _check_input(self, sudoku: str) -> None:
        """Check if the inputed sudoku is in the good format

        Arguments:
            sudoku: The sudoku to solve in one line string where '0' are the case do find

        Raises:
            ValueError: If the sudoku is not well formatted
        """
        if type(sudoku) is not str:
            raise ValueError("The sudoku must be in a string format")

        if len(sudoku) != 81:
            raise ValueError("The sudoku length must be 9x9 = 81")

        for n in sudoku:
            try:
                string_int = int(n)
            except ValueError:
                raise ValueError("Sudoku must contains only numbers [0-9]")

    def solve(self, sudoku: str) -> str:
        """Function that solve the sudoku

        Arguments:
            sudoku: The sudoku to solve in one line string where '0' are the case do find

        Returns: The sudoku solved
        """
        self.__init__(sudoku)
        return self.get_solution()

    def get_solution(self) -> str:
        """Getter for the solution

        """
        return "".join(sum(self.solved_sudoku, []))

    def _organize_sudoku(self) -> None:
        sudoku_matrice = []
        for i in range(9):
            sudoku_matrice.append(list(self.sudoku[i * 9:(i + 1) * 9]))

        for i in range(9):
            for j in range(9):
                if sudoku_matrice[i][j] == '0':
                    sudoku_matrice[i][j] = '123456789'

        self.sudoku_matrice = sudoku_matrice

    def _solving(self) -> None:
        sudoku_matrice = self.sudoku_matrice
        len_s = len("".join(sum(sudoku_matrice, [])))
        while len("".join(sum(sudoku_matrice, []))) > 81:
            for i in range(9):
                for j in range(9):
                    if len(sudoku_matrice[i][j]) == 1:
                        # lignes
                        for x_j in range(9):
                            if j != x_j and len(sudoku_matrice[i][x_j]) > 1:
                                sudoku_matrice[i][x_j] = sudoku_matrice[i][x_j].\
                                    replace(sudoku_matrice[i][j], '')

                        # colonnes
                        for x_i in range(9):
                            if i != x_i and len(sudoku_matrice[x_i][j]) > 1:
                                sudoku_matrice[x_i][j] = sudoku_matrice[x_i][j].\
                                    replace(sudoku_matrice[i][j], '')

                        # carres
                        for x_i in range(3):
                            for x_j in range(3):
                                xii = (i // 3) * 3 + x_i
                                xjj = (j // 3) * 3 + x_j
                                if i != xii and j != xjj and len(sudoku_matrice[xii][xjj]) > 1:
                                    sudoku_matrice[xii][xjj] = sudoku_matrice[xii][xjj].\
                                        replace(sudoku_matrice[i][j],'')
            if len_s == len("".join(sum(sudoku_matrice, []))):
                raise Exception("Can't find a solution")
        self.solved_sudoku = sudoku_matrice

s = Solver('600837001089004700102000400000450020030609005040000860908006070700098010005100930')
print(s.get_solution())
