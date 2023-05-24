testing = "test.txt\"content\""
comma1 = testing.find('"')
comma2 = testing.find('"', comma1+1)
greet = testing[0:comma1]
fname = testing[comma1+1:comma2]
print(fname)
