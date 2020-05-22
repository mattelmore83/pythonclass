
# just messing with classes
class Robot:

    def __init__(self,x=0,y=0):
        self.my_x = x
        self.my_y = y

    def _move_left_leg(self):
        print('moving left leg')

    def _move_right_leg(self):
        print('moving right leg')

    def say_hi(self):
        print(self,'says Beep boop from',self.my_x,self.my_y)

    def move_to(self,x,y):
        self._move_left_leg()
        self._move_right_leg()

        self.my_x = x
        self.my_y = y

    def fire_laser(self,power):
        print('firing laser on',power)

def cleanse_covid(r,x,y):
    r.say_hi()
    r.move_to(x,y)
    r.say_hi()
    r.fire_laser('high')
    r.move_to(x,y)
    r.say_hi()

# creates a robot named rob
#rob = Robot(30,30)

#rob.say_hi()
#rob.move_to(10,20)
#rob.fire_laser('high')
#rob.say_hi()

#bob = Robot()
#bob.say_hi()

# cleanse the covid from 22,50
rob = Robot() # create the robot
cleanse_covid(rob,22,40)