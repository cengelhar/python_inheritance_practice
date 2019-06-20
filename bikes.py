class Bikes:
    def __init__(self, type, color, weight, wheel_size, brake_type, price):
        self.type = type
        self.color = color
        self.weight = weight
        self.wheel_size = wheel_size
        self.brake_type = brake_type
        self.price = price
        self.msrp = 0

    def adjust_color(self, new_color):
        self.color = new_color

    def calc_msrp(self, current_discount):
        self.msrp = self.price * (1+current_discount)
        return self.msrp


# new_bike = Bikes('mountain', 'blue', 25, 26, 'disc', 2000)
# print(new_bike.price)
