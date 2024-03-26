#Q. 2) Write a Python program to find all possible solution for 8 queens problem using Breadth First Search algorithm.import random
import random
def gen_board(size=8):
    x = [i for i in range(size)]                                                                  
    random.shuffle(x)
    return x


def calc_attacks(board):
    attacks = 0
    size = len(board)
    for i in range(size):
        for j in range(i + 1, size):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks

def gen_neigh(board):
    size = len(board)
    neigh = []
    for i in range(size):
        for j in range(size):
            if j != board[i]:
                neigh_board = board.copy()
                neigh_board[i] = j
                neigh.append(neigh_board)
    return neigh

def hill_climbing():
    curr_board = gen_board()
    print("\n&&&&&&&Starting&&&&&&&&&")
    print_board(curr_board)
    print("\n&&&&&&&Solution&&&&&&&&&")
    queue=[curr_board]
    while len(queue)!=0:
        curr = queue[0]
        queue.pop(0)
        if calc_attacks(curr)==0:
            return curr
        neigh_boards = gen_neigh(curr)
        for d in neigh_boards:
            queue.append(d)

    return None

def print_board(solution):
    for i in range(len(solution)):
        for j in range(len(solution)):
            if i==solution[j]:
                print(" # ",end="")
            else:
                print(" _ ",end="")
        print()


solution = hill_climbing()
if solution!=None:
    print_board(solution)
print(solution)
