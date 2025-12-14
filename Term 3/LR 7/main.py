import pickle

class playerData:
    def __init__(self, player_name, score, level):
        self.player_name = player_name
        self.score = score
        self.level = level
    
    def display(self):
        print(f"Player: {self.player_name}, score: {self.score}, level: {self.level}")

def save_game():
    with open("LR 7/player.pkl", "wb") as f:
        pickle.dump(player, f)

def load_game():
    with open("LR 7/player.pkl", "rb") as f:
        return pickle.load(f)

player = playerData("player", 0, 1)
save_game()
player = load_game()

player.display()
