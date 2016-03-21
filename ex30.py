people = 30
cars = 40
trucks =12

if cars > people:
    print "We should take the cars"
elif cars < people:
    print "We should not take the cars"
else:
    print "We can't decide"

if trucks > cars:
    print "Maybe we should take the trucks"
elif trucks < cars:
    print "Thats too many cars"
else:
    print "We still can't decide"

if trucks > people:
    print "Thats too many trucks"
else:
    print "Fine lets stay home then"
