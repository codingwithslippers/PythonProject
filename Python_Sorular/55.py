# Bir satranç tahtasında verilen bir başlangıç pozisyonunda, her adımda atın tüm geçerli hareketlerini hesaplayan ve sonunda tüm şahların mat olduğu bir programı Python kullanarak nasıl yazabilirsiniz?


def is_valid_move(x, y):
    # Kontrol edilen hareketlerin tahtada kalmasını sağlayın
    if x >= 0 and x < 8 and y >= 0 and y < 8:
        return True
    return False

def is_checkmate(board):
    # Tüm şahların mat olup olmadığını kontrol eder
    for row in board:
        for piece in row:
            if piece == '♔':
                return False
    return True

def get_valid_moves(x, y):
    # Atın geçerli hareketlerini döndürür
    moves = []
    offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
               (1, -2), (1, 2), (2, -1), (2, 1)]

    for offset in offsets:
        new_x = x + offset[0]
        new_y = y + offset[1]
        if is_valid_move(new_x, new_y):
            moves.append((new_x, new_y))
    return moves

def play_game():
    board = [[' ' for _ in range(8)] for _ in range(8)]
    board[0][0] = '♔'  # Beyaz şah
    board[3][3] = '♚'  # Siyah şah
    at_pos = (0, 0)

    while not is_checkmate(board):
        print("Şu anki tahta durumu:")
        for row in board:
            print(' | '.join(row))
        print("")

        x, y = at_pos
        valid_moves = get_valid_moves(x, y)

        print("Atın geçerli hareketleri:")
        for move in valid_moves:
            print(move)
        print("")

        move = input("Hangi hamleyi yapmak istersiniz? (x y): ")
        new_x, new_y = map(int, move.split())

        if (new_x, new_y) in valid_moves:
            # Eski pozisyonu temizleyin
            board[x][y] = ' '

            # Yeni pozisyona atı taşıyın
            board[new_x][new_y] = '♔'

            # At pozisyonunu güncelleyin
            at_pos = (new_x, new_y)
        else:
            print("Geçersiz hamle!")

    print("Tüm şahlar mat! Oyun bitti.")

play_game()
