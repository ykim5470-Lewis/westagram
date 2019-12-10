#Argument .format
print("average of {} {} is {}".format("1","2","3"))
#import sys.argv
import sys
print("average of {} {} is {}".format(sys.argv[1],sys.argv[2],sys.argv[3]))
#show {} 
import sys
print("average of {{{},{},{}}} is {}".format(sys.argv[1],sys.argv[2],sys.argv[3])
,sys.argv[4])
#Why {{}} is {}?