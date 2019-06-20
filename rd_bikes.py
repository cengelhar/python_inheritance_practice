from bikes import Bikes
import math

class RdBikes(Bikes):

    def __init__(self, type, color, weight, wheel_size, brake_type, price, max_speed, frame_material, safey_score):
        Bikes.__init__(self, type, color, weight, wheel_size, brake_type, price)
        self.max_speed = max_speed
        self.frame_material = frame_material
        self.safey_score = safey_score


    def danger_score(self, weight, brake_type, price, max_speed, safety_score):
        danger_algo = ((.1 * weight) + (.1 * brake_type) + (.1 * price) + (.3 * max_speed) (.4 * safety_score))
        print(danger_algo)
