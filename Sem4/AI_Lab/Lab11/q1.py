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
                neigh.append((neigh_board, calc_attacks(neigh_board)))
    return neigh

def hill_climbing():
    curr_board = gen_board()
    curr_att = calc_attacks(curr_board)
    print("\n&&&&&&&Starting&&&&&&&&&")
    print_board(curr_board)
    print("\n&&&&&&&Solution&&&&&&&&&")


    while curr_att > 0:
        neigh_boards = gen_neigh(curr_board)
        neigh_boards.sort(key=lambda x: x[1])
        best_neigh, best_att = neigh_boards[0]

        if best_att < curr_att:
            curr_board = best_neigh
            curr_att = best_att
        else:
            curr_board = gen_board()
            curr_att = calc_attacks(curr_board)

    return curr_board

def print_board(solution):
    for i in range(8):
        for j in range(8):
            if i==solution[j]:
                print(" # ",end="")
            else:
                print(" _ ",end="")
        print()


solution = hill_climbing()
print_board(solution)
print(solution)