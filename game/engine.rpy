#This file was use to measure how much affection Luna have

init -5 python:
    class Point:
        def __init__(self):
            self.affection = 0

        #add or minus the point
        def add(self, amount=10):
            self.affection = min(100, self.affection + amount)

        #total point after all
        def total(self):
            return self.affection
