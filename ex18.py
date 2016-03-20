#this is one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r and arg2 :%r " % (arg1, arg2)

#ok, that *args is just pointless, we can do the following

def print_two_again (arg1, arg2):
    print "arg1: %r, arg2: %r "%(arg1,arg2)

#this just takes one argument
def print_one(arg1):
    print " arg1: %r" %arg1

#this one prints nothing
def print_none():
    print "I got nothing"

print_two("Shekhar", "Karande")
print_two_again("Shekhar", "Karande")
print_one("Shekhar")
print_none()
