from bikes import Bikes
import math

class MtnBikes(Bikes):

    def __init__(self, type, color, weight, wheel_size, brake_type, price, bike_subtype, has_suspension, gear_count):
        Bikes.__init__(self, type, color, weight, wheel_size, brake_type, price)
        self.bike_subtype = bike_subtype
        self.has_suspension = has_suspension
        self.gear_count = gear_count

    def adrenaline_level(self, intensity):
        bike_qual = self.price * self.gear_count

        foo = bike_qual * intensity
        print(foo)

    def total_worth(self, current_discount, total_use):
        msrp = Bikes.calc_msrp(self, current_discount)
        total_worth = msrp * total_use
        print(total_worth)



new_bike = MtnBikes('mountain', 'blue', 25, 26, 'disc', 2001, 'downhill', 'yes', 22)

# new_bike.adrenaline_level(200)

new_bike.total_worth(0.2, 40)
