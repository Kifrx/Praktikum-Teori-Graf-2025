BOARD_SIZE = 8

MOVES = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def inside_board(x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

def count_onward_moves(board, x, y):
    count = 0
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if inside_board(nx, ny) and board[ny][nx] == -1:
            count += 1
    return count

def pure_warnsdorff(start_x, start_y):
    board = [[-1 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    curr_x, curr_y = start_x, start_y
    board[curr_y][curr_x] = 1 # Langkah 1

    # Loop sampe langkah 64
    for step in range(2, BOARD_SIZE * BOARD_SIZE + 1):
        min_degree = 9
        next_x, next_y = -1, -1

        # Cari tetangga dengan degree terkecil
        for dx, dy in MOVES:
            nx, ny = curr_x + dx, curr_y + dy
            if inside_board(nx, ny) and board[ny][nx] == -1:
                deg = count_onward_moves(board, nx, ny)
                if deg < min_degree:
                    min_degree = deg
                    next_x, next_y = nx, ny

        if next_x == -1:
            return None # Gagal 

        # Pindah
        curr_x, curr_y = next_x, next_y
        board[curr_y][curr_x] = step

    return board


def check_tour_status(board, start_x, start_y):
    # Cari lokasi langkah terakhir (64)
    end_x, end_y = -1, -1
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if board[y][x] == 64:
                end_x, end_y = x, y
                break
              
    # Cek apakah 64 bertetangga dengan Start (1)
    for dx, dy in MOVES:
        if end_x + dx == start_x and end_y + dy == start_y:
            return "CLOSED TOUR "
    return "OPEN TOUR "

def print_board(board):
    for row in board:
        print(" ".join(f"{x:2}" for x in row))

if __name__ == "__main__":
    print("=== KNIGHT'S TOUR ===")
    
    try:
        sx = int(input("Start X (0-7): "))
        sy = int(input("Start Y (0-7): "))
        
        if inside_board(sx, sy):
            board = pure_warnsdorff(sx, sy)
            
            if board:
                print("\n Papan: ")
                print_board(board)
                
                status = check_tour_status(board, sx, sy)
                print(f"\nSTATUS : {status}")
                
                for r in range(8):
                    for c in range(8):
                        if board[r][c] == 64:
                            ex, ey = c, r
                print(f"Info: Kuda mulai di ({sx},{sy}) dan berakhir di ({ex},{ey}).")

            else:
                print("\nStatus: GAGAL")
    except ValueError:
        print("Error: Angka saja.")
