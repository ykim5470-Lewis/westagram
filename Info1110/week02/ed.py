import sys
if len(sys.argv) !=6:
    print("please enter five numbers.")
    else:
        num=(float(sys.argv[1])) +float(sys.argv[2])+ float(sys.argv[3])+ float(sys.argv[4])+ float(sys.argv[5]))/5

        print("Average of {{ {}, {}, {}, {}, {} }} is {:0.2f}"). format(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],num))
