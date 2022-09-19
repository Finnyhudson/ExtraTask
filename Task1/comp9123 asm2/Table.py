class Table:
    def __init__(self, hobbits: int, elfs: int, dwarfs: int, humans: int, distance: int):
        self.capacity = 7
        self.distance = distance
        self.hobbits = hobbits
        self.elfs = elfs
        self.dwarfs = dwarfs
        self.humans = humans
        self.num_on_table = self.hobbits + self.humans + self.elfs + self.dwarfs

    def is_table_full(self):
        """
        Returns whether the table is full or not.
        :return: True if the table is full, False otherwise.
        """
        if self.num_on_table >= self.capacity:
            return True
        else:
            return False

    def is_elves_only(self):
        """
        Returns whether the table is only elves or not.
        There must be at least one elf at the table to be considered elves-only.
        :return: True if the table is only elves, False otherwise.
        """
        if self.hobbits == 0 and self.humans == 0 and self.dwarfs == 0 and self.elfs > 0:
            return True
        else:
            return False

    def is_dhe_only(self):
        """
        Returns whether the table is made up of only dwarves, only hobbits, or only elves.
        Note that at least one of the creatures must be at the table to be considered
        dwarf-only, hobbit-only, or elf-only.
        :return: True if the table is made up of only dwarves, only hobbits, or only elves.
        """
        if self.hobbits > 0 and self.elfs == 0 and self.humans == 0 and self.dwarfs == 0:
            return True
        elif self.dwarfs > 0 and self.humans == 0 and self.elfs == 0 and self.hobbits == 0:
            return True
        elif self.is_elves_only() is True:
            return True

    def get_total_diners(self):
        """
        Returns the total number of diners at the table.
        :return: The total number of diners at the table.
        """
        return self.num_on_table

    def get_elves(self):
        """
        Returns the number of elves at the table.
        :return: The number of elves at the table.
        """
        return self.elfs

    def get_distance(self):
        """
        Returns the distance of the table from the door.
        :return: The distance of the table from the door.
        """
        return self.distance

    def add_hobbit(self):
        """
        Adds a hobbit to the table.
        If the table is already full, this function should do nothing.
        """
        if self.num_on_table < self.capacity:
            self.hobbits += 1
            self.num_on_table += 1

    def add_dwarf(self):
        """
        Adds a dwarf to the table.
        If the table is already full, this function should do nothing.
        """
        if self.num_on_table < self.capacity:
            self.dwarfs += 1
            self.num_on_table += 1

    def add_elf(self):
        """
        Adds an elf to the table.
        If the table is already full, this function should do nothing.
        """
        if self.num_on_table < self.capacity:
            self.elfs += 1
            self.num_on_table += 1

    def add_human(self):
        """
        Adds a human to the table.
        If the table is already full, this function should do nothing.
        """
        if self.num_on_table < self.capacity:
            self.humans += 1
            self.num_on_table += 1

