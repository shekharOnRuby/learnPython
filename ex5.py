name = 'Zed A. Shaw'
age = 35 # not a lie
height = 75 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
celsius = 32
farhenheit = (celsius * (9/2)) + 32
km = 1
mile = 0.625 * km
print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Atually thats not too heavy"
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the cofee." %teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d" %(age,height,weight, age + weight + height)

print " %d celsius converst to %f farhenheit" %(celsius, farhenheit)
print " And %d km is %f miles" %(km, mile)
