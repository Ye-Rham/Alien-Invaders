class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 5, 60)
        self.start_color = (0, 0, 0)

        self.button_color = (0, 200, 0)
        self.button_hover_color = (50, 50, 50)
        self.text_color = (200, 200, 200)
        self.text_hover_color = (0, 200, 0)

        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 150, 60
        self.alienbullet_color = 150, 60, 60
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.alien1_points = None
        self.alien2_points = None
        self.alien3_points = None
        self.ship_speed_factor = None
        self.bullet_speed_factor = None
        self.alienbullet_speed_factor = None
        self.alien_speed_factor = None
        self.fleet_direction = None

        self.initialize_dynamic_settings()

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien1_points = int(self.alien1_points * self.score_scale)
        self.alien2_points = int(self.alien2_points * self.score_scale)
        self.alien3_points = int(self.alien3_points * self.score_scale)
        print(self.alien1_points + self.alien2_points + self.alien3_points)

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 6
        self.alienbullet_speed_factor = 2
        self.alien_speed_factor = 1

        self.fleet_direction = 1

        self.alien1_points, self.alien2_points, self.alien3_points = 10, 20, 40
