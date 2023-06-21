class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return f'Car(color={self.color}, count_passenger_seats={self.count_passenger_seats}, is_baby_seat={self.is_baby_seat}, is_busy={self.is_busy})'
