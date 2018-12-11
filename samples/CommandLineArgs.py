import sys

usage = "\nUsage: jython CommandLineArgs.py -conf myconf.txt\n\n" 
if len(sys.argv) != 3:  # the program name and the two arguments
  # stop the program and print an error message
  sys.exit(usage)
  
print "---- All the args(including name of the script)"
for arg in sys.argv: 
  print arg

print "\n---- The first arg: "
print sys.argv[1]
  
