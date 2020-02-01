#My first code! Im so proud!!!
print "Hello User, give me two numbers and a limiter."
print "I will find the sum of all multiples of that number within the limiter"

var_1 = input("Number 1: ")
var_2 = input("Number 2: ")
limiter = input("Limiting Number: ")
var_1orig = var_1
var_2orig = var_2
var_1_results = []
var_2_results = []

print "-" * 20
print "Number 1 multiples begin."

while var_1 < limiter:
    var_1_results.append(var_1)
    var_1 += var_1orig

print var_1_results
print "Number 1 multiples finished."
print "-" * 20


print "-" * 20
print "Number 2 multiples begin."

while var_2 < limiter:
    var_2_results.append(var_2)
    var_2 += var_2orig

print var_2_results
print "Number 2 multiples finished."
print "-" * 20
print "-" * 20
print "The sum of both lists of variabels is..."
print sum(var_1_results) + sum(var_2_results)
print "Tada!"
