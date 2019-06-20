from bikes import Bikes
import math

class RdBikes(Bikes):

    def __init__(self, type, color, weight, wheel_size, brake_type, price, max_speed, frame_material, safety_score):
        Bikes.__init__(self, type, color, weight, wheel_size, brake_type, price)
        self.max_speed = max_speed
        self.frame_material = frame_material
        self.safety_score = safety_score


    def danger_score(self):
        danger_algo = ((.1 * self.weight) + (.4 * self.price) + (.5 * self.max_speed))
        final_danger_score = danger_algo * self.safety_score
        print(final_danger_score)


new_bike = RdBikes('road', 'blue', 25, 26, 'disc', 2001, 42, 'fiberglass', 98)

new_bike.danger_score()
