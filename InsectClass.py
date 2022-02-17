import random
from re import L
from tkinter import W


class Insect:
    def __init__(self, w, l):


        self.legs = W
        self.wings = L
        self.flight = 0

    def flight_length(self):
        self.flight = random.randint(1, 10)

    def get_flight(self):
        return self.flight
