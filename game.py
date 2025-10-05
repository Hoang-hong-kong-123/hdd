import chess
board = chess.Board()

while not board.is_game_over():
    print(board)
    if board.turn == chess.WHITE:
        move = input("Nước đi của Trắng (ví dụ: e2e4): ")
    else:
        move = input("Nước đi của Đen (ví dụ: e7e5): ")

    try:
        board.push_san(move)
    except:
        try:
            board.push_uci(move)
        except:
            print("❌ Nước đi không hợp lệ, thử lại.")
            continue

    print("\n")

print("Kết thúc ván cờ:", board.result())
