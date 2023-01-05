
s1 = "Tesco"

for each in s1:
	print (each, end  ="")

print(" Sale transaction", end = "\n===\n")

print ("Sales Amt : %10.2f. \nTotal amount: %8.2f. \nTransaction status: %15s" %(10, 10, "completed"))


def string_formatting(s1,t1,status = "pending"):
	return ("Sales Amt : %10.2f. \nTotal amount: %8.2f. \nTransaction status: %15s" %(s1, t1, status))


print (string_formatting(10, 20))	


print ("store  %20s" %"Transactions", end = "\n===\n")

print ("Sales amt : {0:10.2f}. \nTotal value: {1: 10.2f}. \nTransaction status: {2:10s}".format(234, 2343, "done"))

print ("Sales amt : {0[1]:10.2f}. \nTotal value: {1[1]: 10.2f}. \nTransaction status: {2[2]:10s}".format({0:234, 1:454}, {1: 2343}, {2:"done"}))



print ("a : {0[x]:3.2f}, b: {1[s]:2d}".format({'x':43, 'y':32}, {'s': 32, 't': 43}))

print ("a : {0:3.2f}, b: {1:2d}".format(2,3))

print ("{a:10s} {b:20s} and {c:10s} and {d:5d}".format(a ="python", b= "DS", c ="ML", d = 32))

d = {'a': 1, 'b':2} # dictonary

print (d['a'])

t = (10,20, 30,40, 50, 60)
count = 0;
for each in t:
	print ("t[%d] = %d"%(count, each))
	count = count + 1;

print ("Input values are: {x}, {y} and {z} ".format(x = 10, y = 20, z = 30))

# t[0] = 10
# t[1] = 20
# t[2] = 30
# t[3] = 40
# t[4] = 50
# t[5] = 60

