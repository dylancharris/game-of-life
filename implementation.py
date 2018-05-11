class Life:

    def __init__(self):
        self.board = []

    def alive_rule(self, cell_num, num_alive_neighbors):
        return num_alive_neighbors in [2,3] or num_alive_neighbors > 4 if cell_num else num_alive_neighbors == 3 or num_alive_neighbors > 4
