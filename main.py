from human import Human
from robot import Robot

workers = [Human(), Robot()]

for worker in workers:
    worker.work()
