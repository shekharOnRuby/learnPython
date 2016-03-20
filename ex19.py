def cheese_and_crackers (cheese_count, boxes_of_crackers):
    print "you have %d cheese" %cheese_count
    print "you have %d crackers" %boxes_of_crackers
    print "Man thats a lot of cheese and crackers"
    print "Get a blanket \n"

print "We can just give the function numbers directly"
cheese_and_crackers(12,45)

print "Or we can use variables from our script"
amount_of_crackers = 10
amount_of_cheese = 30

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print " We can even do Maths inside"
cheese_and_crackers(20+5,35+6)

print "And we can combine the two variables and do the maths"
cheese_and_crackers(amount_of_cheese +45, amount_of_crackers +5)
