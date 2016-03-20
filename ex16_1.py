from sys import argv

scriptname, filename = argv

fil = open(filename)
target = file.read(fil)

print "Displaying contents of file %r" %target
