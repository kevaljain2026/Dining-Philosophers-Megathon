class user:
    # Class for the users of the car
    def __init__(self, name: str, window_distance: int,\
            seat_distance: int, seat_angle: int, music_history):
        self.name = name
        self.window_distance = window_distance
        self.seat_distance = seat_distance;
        self.seat_angle = seat_angle
        self.music_history = music_history
    
    def print_user_settings(self):
        print(f'lowering window by {self.window_distance} cm for {self.name}')
        print(f'adjusting seat distance to {self.seat_distance} for {self.name}')
        print(f'adjusting seat angle to {self.seat_angle} for {self.name}')
