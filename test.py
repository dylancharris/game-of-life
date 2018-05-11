from implementation import Life

# first test: check that rule works
# alive_rule(current, neighbors)
# returns True iff a cell that is currently <current> and with
# <neighbors> neighbors will be alive in the next generation

l = Life()

print("Alive rule")
assert l.alive_rule(1, 2)
assert l.alive_rule(1, 3)
assert l.alive_rule(0, 3)
assert not l.alive_rule(0, 2)
assert not l.alive_rule(0, 4)
assert not l.alive_rule(0, 1)
assert not l.alive_rule(1, 1)
assert not l.alive_rule(1, 4)

# second test: Set and get cells from the board
# Life object includes board getters/setters
# board initially all dead
# dead = False, alive = True

print("get/set/clear")
assert not l.get(0,0)
assert not l.get(1,4)
assert not l.get(3,3)
assert not l.get(2,2)

l.set(0,0)
l.set(1,1)

assert l.get(0,0)
assert l.get(1,1)
assert not l.get(3,3)

l.set(3,3)
assert l.get(3,3)

l.clear(1,1)
assert not l.get(1,1)
l.set(1,1)
assert l.get(1,1)

# count neighbors
# Live.count(x,y) = the number of live neighbors
print("count neighbors")
assert l.count(0,0) == 1
assert l.count(1,1) == 1
assert l.count(0,1) == 2
assert l.count(2,2) == 2

# output formatting:
# return a list of lines where a dead cell is formatted as " " and 
# a living cell is formatted as "#"
assert l.format() == [
 "#   ",
 " #  ",
 "    ",
 "   #"]
l.clear(0,0)
assert l.format() == [
 "    ",
 " #  ",
 "    ",
 "   #"]
l.set(2,0)
assert l.format() == [
 "  # ",
 " #  ",
 "    ",
 "   #"]

# read input
with open("f1.gol") as infile:
	l.read(infile)
with open("f1.gol") as infile:
	# format shouldn't include the trailing newlines
	assert [line.rstrip("\n") for line in infile.readlines()] == l.format()
    

