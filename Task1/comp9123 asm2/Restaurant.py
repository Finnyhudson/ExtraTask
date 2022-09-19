from Table import Table

class Restaurant:
    def __init__(self):
        self.table_num = 0
        self.all_diners = 0
        self.all_elves = 0
        self.all_dwarves = 0
        self.all_humans = 0
        self.all_hobbits = 0
        self.tables = []
        self.all_diners = self.all_dwarves + self.all_hobbits + self.all_elves + self.all_humans
