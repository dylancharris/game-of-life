from implementation import Life

# first test: check that rule works
# alive_rule(current, neighbors)
# returns True iff a cell that is currently <current> and with
# <neighbors> neighbors will be alive in the next generation

l = new Life()

assert l.alive_rule(1, 2) 
assert l.alive_rule(1, 3) 
assert l.alive_rule(0, 3) 
assert not l.alive_rule(0, 2) 
assert not l.alive_rule(0, 4) 
assert not l.alive_rule(0, 1) 
assert not l.alive_rule(1, 1) 
assert not l.alive_rule(1, 4) 


