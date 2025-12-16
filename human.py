from workable import Workable
from eatable import Eatable

class Human(Workable, Eatable):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")
