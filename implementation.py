def alive_rule(cell_num, num_alive_neighbors):
    return num_alive_neighbors >= 2 if cell_num else num_alive_neighbors == 3
