import hashmap

#create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon','OR')
hashmap.set(states, 'Florida','FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

#create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities,'CA','San Francisco')
hashmap.set(cities,'MI','Detroit')
hashmap.set(cities,'FL','Jacksonville')

#add some more cities
hashmap.set(cities,'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

#print out some cities
print '--' * 10
print "NY state has some cities ", hashmap.get(cities,'NY')
print "OR state has some cities ", hashmap.get(cities,'OR')

#print some states
print '--' * 10
print "Michigan's abbreviation is   ", hashmap.get(states,'Michigan')
print "Florida's abbreviation is  ", hashmap.get(states,'Florida')

#do it by using the state than cities dict
print '--'* 10
print "Michigan has: ", hashmap.get(cities, hashmap.get(states,'Michigan'))
print "Florida has: ", hashmap.get(cities, hashmap.get(states, 'Florida'))

#print every state abbreviation
print '--'* 10
hashmap.list(states)

#print every city in state
print '--'* 10
hashmap.list(cities)


print '--' * 10
#Safely get a abbreviation by state that might not be there
state = hashmap.get(states, 'Texas')
if not state:
    print "Sorry, NO Texas"
#default values using ||= with the nil result
#can u do this on one line
city = hashmap.get(cities, 'TX','Does not exist')
print "The city for the state 'TX' is: %s " % city
