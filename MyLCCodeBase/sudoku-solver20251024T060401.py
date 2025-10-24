#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import sys

ROW = "ABCDEFGHI"
COL = "123456789"

# 3x3 subgrids
def cross(A, B):
    return [a + b for a in A for b in B]
SQS = [cross(rs, cs) for rs in ("ABC", "DEF", "GHI") for cs in ("123", "456", "789")]
DEBUG = False

def box_index(cell):
    r, c = cell[0], cell[1]
    row_block = ROW.index(r)//3
    col_block = COL.index(c)//3
    return 3 * row_block + col_block

def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = i + ' '
        for j in COL:
            row += (str(board[i + j]) + " ")
            if int(j)%3==0:
                row += " "
        print(row)
        if (ord(i)-ord("A"))%3 == 2:
            print()


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)

def is_valid(board, ignore_zeroes = False):
    def all_unique(values):
        if ignore_zeroes:
            non_zero_vals = [v for v in values if v != 0]
            # if len(non_zero_vals) != len(set(non_zero_vals)) and DEBUG:
            #     print(f"INVALID SEQUENCE {values}")
            #     print(f"bad board:")
            #     print_board(board)
            return len(non_zero_vals) == len(set(non_zero_vals))
        if 0 in values:
            return False
        return 9 == len(set(values))

    # check all rows
    for r in ROW:
        if not all_unique([board[r + c] for c in COL]):
            return False

    # check all columns
    for c in COL:
        if not all_unique([board[r + c] for r in ROW]):
            return False

    # check all 3x3 subgrids
    for sq in SQS:
        if not all_unique([board[cell] for cell in sq]):
            return False
    return True


def has_singleton(u):
    for coord in u:
        if len(u[coord]) == 1:
            return True
    return False

def _backtracking(board, unassigned, times):
    '''
    @params
    board: dict() "A1" -> int
    unassigned: dict() "A1" -> [1,...9]
    @returns solved board
    '''
    if DEBUG:
        if times > 200: return board
    if is_valid(board):
        if DEBUG:
            print_board(board)
            print("valid!")
        return board
    
    # calculate min
    cell_fewest_options = None
    for cell in unassigned:
        if not cell_fewest_options or len(unassigned[cell_fewest_options]) > len(unassigned[cell]):
            cell_fewest_options = cell
    if not cell_fewest_options:
        return None
    # if DEBUG:
    #     print(f"{cell_fewest_options} has fewest options: {unassigned[cell_fewest_options]}")

    # using the minimum remaining value heuristic:
    # Choose the var with the fewest legal values in its domain.
    potential_options = unassigned[cell_fewest_options][:]
    for i,option in enumerate(potential_options):
        options_ok = True
        
        r = cell_fewest_options[0]
        c = cell_fewest_options[1]
        # forward check two things: if board is valid, if unassigned valid
        board[cell_fewest_options] = option
        if not is_valid(board, ignore_zeroes=True):
            options_ok = False

        removed = []
        # check if unassigned valid
        if options_ok:
            for col in COL: # this row
                if c == col: continue
                if r + col in unassigned and option in unassigned[r + col]:
                    if len(unassigned[r + col]) == 1:
                        options_ok = False
                        break # failure, forward checking
                    unassigned[r + col].remove(option)
                    removed.append((r+col, option))

            for row in ROW: # this col
                if r == row: continue
                if row + c in unassigned and option in unassigned[row + c]:
                    if len(unassigned[row + c]) == 1:
                        options_ok = False
                        break # failure, forward checking
                    unassigned[row + c].remove(option)
                    removed.append((row+c, option))

            #within this subgrid
            for sq_cell in SQS[box_index(cell_fewest_options)]:
                if sq_cell == cell_fewest_options: continue
                if sq_cell in unassigned and option in unassigned[sq_cell]:
                    if len(unassigned[sq_cell]) == 1:
                        # unassigned[sq_cell].append(option)
                        options_ok = False
                        break # failure
                    unassigned[sq_cell].remove(option)
                    removed.append((sq_cell, option))
            for cur_options in unassigned[cell_fewest_options]:
                removed.append((cell_fewest_options, cur_options))
            del unassigned[cell_fewest_options]

        if options_ok:
            if DEBUG:
                print(f"{times} state: ")
                print_board(board)
                print(unassigned)
            solution = _backtracking(board, unassigned, times +(i+ 1))
            if solution:
                return solution

        # restore state
        board[cell_fewest_options] = 0
        for cell, val in removed:
            if cell not in unassigned:
                unassigned[cell] = []
            unassigned[cell].append(val)

    return None

def backtracking(board):
    """Takes a board and returns solved board."""
    unassigned = {
        ROW[r] + COL[c]: 
        [board[ROW[r] + COL[c]]] 
            if board[ROW[r] + COL[c]] != 0 else list(range(1,10)) 
        for r in range(9) for c in range(9)
    }

    # Maintain Arc Consistency
    while has_singleton(unassigned):
        for cell in board:
            r = cell[0]
            c = cell[1]
            if cell in unassigned and len(unassigned[cell]) == 1:
                val = unassigned[cell][0]
                board[cell] = val
                for col in COL: # this row
                    # if c == col: continue
                    if r + col in unassigned and val in unassigned[r + col]:
                        unassigned[r + col].remove(val)
                for row in ROW: # this col
                    # if r == row: continue
                    if row + c in unassigned and val in unassigned[row + c]:
                        unassigned[row + c].remove(val)
                #within this subgrid
                for sq_cell in SQS[box_index(cell)]:
                    # if sq_cell == cell: continue
                    if sq_cell in unassigned and val in unassigned[sq_cell]:
                        unassigned[sq_cell].remove(val)
                del unassigned[cell]
        # if DEBUG:
        #     print(unassigned)

    solved_board = _backtracking(board, unassigned, 0)
    return solved_board


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if len(sys.argv[1]) < 9:
            print("Input string too short")
            exit()

        print(sys.argv[1])
        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(sys.argv[1][9*r+c])
                  for r in range(9) for c in range(9)}       
        
        solved_board = backtracking(board)
        
        # Write board to file
        if not DEBUG:
            out_filename = 'output.txt'
            outfile = open(out_filename, "w")
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')
    else:
        print("Usage: python3 sudoku.py <input string>")
    
    print("Finishing all boards in file.")