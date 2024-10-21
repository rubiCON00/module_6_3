class Hourse:
    def __init__(self):
        super().__init__()
        self.x_distance = 0
        self.sound = 'Frrr'
    def run(self, dx):
        self.x_distance += dx
        return self.x_distance
class Eagle:
    def __init__(self):
        super().__init__()
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Hourse, Eagle):
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)
    def move(self, dx, dy):
        return self.fly(dy), self.run(dx)
    def get_pos(self):
        return self.x_distance, self.y_distance
    def voice(self):
        print(self.sound)


p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()

