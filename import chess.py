import chess
import chess.engine

# Chemin vers l'exécutable de Stockfish (téléchargez-le sur stockfishchess.org)
STOCKFISH_PATH = "stockfish-windows-x86-64-avx2.exe"  # À adapter selon votre OS

def get_best_move(fen):
    """ Renvoie le meilleur coup selon Stockfish pour une position donnée en FEN. """
    board = chess.Board(fen)
    
    with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:
        result = engine.play(board, chess.engine.Limit(time=0.5))  # 0.5s d'analyse
        return result.move.uci()

# Exemple d'utilisation
fen_position = chess.STARTING_FEN  # Position de départ
best_move = get_best_move(fen_position)
print(f"Meilleur coup : {best_move}")

