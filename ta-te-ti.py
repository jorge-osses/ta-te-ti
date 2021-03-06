theBoard = ["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]


def DisplayBoard(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[0][0]+"   |   "+board[0][1]+("   |   ")+board[0][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[1][0]+"   |   "+board[1][1]+("   |   ")+board[1][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[2][0]+"   |   "+board[2][1]+("   |   ")+board[2][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

theBoard[1][1] = "X"

    
#
# la función acepta un parámetro el cual contiene el estado1 actual del tablero
# y lo muestra en la consola
#

def MakeListOfFreeFields(board):
    numFila = 0
    listFree = []
    for fila in board:
        numColum = 0
        for col in fila:
            posicion = (numFila, numColum)
            if col == "X" or col == "O":
                pass
            else:
                listFree.append(posicion)
            numColum += 1
            
        numFila += 1    
    return listFree

#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#


def EnterMove(board):
    entrada = int(input("Ingresa tu movimiento: "))
    coordenadas = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    coordenada = coordenadas[entrada - 1]
    if coordenada in MakeListOfFreeFields(board):
        board[coordenada[0]][coordenada[1]] = "O"
    else:
        print("Lo siento, Posición ocupada.")
        EnterMove(board)

#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#




def VictoryFor(board):        
    if board[0][0] == board[0][1] == board[0][2] == "O":
        print("Tu Ganas.")
        return True
        
    elif board[0][0] == board[0][1] == board[0][2] == "X":
        print("Tu pierdes, gana la maquina")
        return True
        
    elif board[1][0] == board[1][1] == board[1][2] == "O":
        print("Tu Ganas.")
        return True
        
    elif board[1][0] == board[1][1] == board[1][2] == "X":
        print("Tu pierdes, gana la maquina")
        return True
        
    elif board[2][0] == board[2][1] == board[2][2] == "O":
        print("Tu Ganas.")
        return True
        
    elif board[2][0] == board[2][1] == board[2][2] == "X":
        print("Tu pierdes, gana la maquina")
        return True
        
    elif board[0][0] == board[1][1] == board[2][2] == "O":
        print("Tu Ganas.")
        return True
        
    elif board[0][0] == board[1][1] == board[2][2] == "X":
        print("Tu pierdes, gana la maquina")
        return True
        
    elif board[0][2] == board[1][1] == board[2][0] == "O":
        print("Tu Ganas.")
        return True
        
    elif board[0][2] == board[1][1] == board[2][0] == "X":
        print("Tu pierdes, gana la maquina")
        return True
        
    elif board[0][0] == board[1][0] == board[2][0] == "O":
        print("Tu Ganas.")
        return True
        
    elif board[0][0] == board[1][0] == board[2][0] == "X":
        print("Tu pierdes, gana la maquina")
        return True
        
    elif board[0][1] == board[1][1] == board[2][1] == "O":
        print("Tu Ganas.")
        return True
        
    elif board[0][1] == board[1][1] == board[2][1] == "X":
        print("Tu pierdes, gana la maquina")
        return True
        
    elif board[0][2] == board[1][2] == board[2][2] == "O":
        print("Tu Ganas.")
        return True
        
    elif board[0][2] == board[1][2] == board[2][2] == "X":
        print("Tu pierdes, gana la maquina")
        return True
        
    else:
        return False
    
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#
def DrawMove(board):
    lst = len(MakeListOfFreeFields(board))
    lst2 = []
    from random import randrange
    lst2 = MakeListOfFreeFields(board)[randrange(lst)]
    board[lst2[0]][lst2[1]] = "X"


def game(board):
    DisplayBoard(board)
    while len(MakeListOfFreeFields(board)) > 0 and VictoryFor(board) != True:
        EnterMove(board)
        if VictoryFor(board) == True:
            break
        else:
            DrawMove(board)
            DisplayBoard(board)
            
    if VictoryFor(board) == False:
        print("¡EMPATE WEY!")
    else:
        pass
           
game(theBoard)
            
 
