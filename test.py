import implementation as Life

# first test: check that rule works
# alive_rule(current, neighbors)
# returns True iff a cell that is currently <current> and with
# <neighbors> neighbors will be alive in the next generation

assert Life.alive_rule(1, 2) 
assert Life.alive_rule(1, 3) 
assert Life.alive_rule(0, 3) 
assert not Life.alive_rule(0, 2) 
