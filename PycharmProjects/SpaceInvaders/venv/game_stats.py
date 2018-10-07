class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.high_score_file = open("High_Scores.txt", "r")
        self.high_score_list = []
        for line in self.high_score_file:
            self.high_score_list.append(int(line))
        self.high_score_file.close()
        if self.high_score_list:
            self.high_score = self.high_score_list[0]
        else:
            self.high_score = 0
        self.ships_left = None
        self.score = None
        self.level = None
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
