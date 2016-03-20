print "Let's practice everything."
print "You\'d need to know \' bout escapes with \\ that do \nnewline and \t tabs "

poem = """
    \tThe Lovely World
    with logic so firmly planted
    cannot discern\n the needs of Love
    nor comprehend passion from intution
    and requires an explanation
    \n\twhere there is none
    """
print "-"*20
print poem
print "-"*20

five = 10 - 2 + 3 - 6

print "This should be five: %s" %five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000

beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %s " %start_point
print "We have %d beans, %d jars and %d crates" %(beans, jars, crates)

start_point = start_point / 10
print "We can also do it this way: "
print "We'd have %d beans, %d jars and %d crates" % secret_formula(start_point)
