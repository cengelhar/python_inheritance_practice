from bikes import Bikes
import math

class BmxBikes(Bikes):
    def __init__(self, type, color, weight, wheel_size, brake_type, price, has_pegs, has_gyro):
        Bikes.__init__(self, type, color, weight, wheel_size, brake_type, price)
        self.has_pegs = has_pegs
        self.has_gyro = has_gyro


    def coolness_score(self):
        if self.has_pegs == 'Yes':
            pegs_score = 100
        elif self.has_pegs == 'Kind of':
            pegs_score = 50
        else:
            pegs_score = 0

        if self.has_gyro == 'Yes':
            gyro_score = 100
        elif self.has_gyro == 'Yes, but it doesn\'t work':
            gyro_score = 50
        else:
            gyro_score = 0

        coolness = ((.5 * pegs_score) + (.5 * gyro_score))

        print(coolness)

new_bike = BmxBikes('bxm', 'blue', 25, 26, 'disc', 2001, 'Kind of', 'Yes, but it doesn\'t work')

new_bike.coolness_score()
