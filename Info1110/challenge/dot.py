import sys
V= [sys.argv[1], sys.argv[2], sys.argv[3]]
U= [sys.argv[4], sys.argv[5], sys.argv[6]]
dot= int(V[0])*int(U[0])+int(V[1])*int(U[1])+int(V[2])*int(U[2])
print("V = {{ {}, {}, {} }}".format(sys.argv[1], sys.argv[2], sys.argv[3])) 
print("U = {{ {}, {}, {} }}".format(sys.argv[4], sys.argv[5], sys.argv[6]))
print("V . U = "+str(dot))
