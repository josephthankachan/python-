# asking to user pyramid height#
Inp_t= input("Enter the height of the pyramid you wnated")
# converting string value to integer value#
Heig_pyra = int(Inp_t)
# printing the empty space til the middle then print "*" according to the pyramid order #
n=Heig_pyra-1
for i in range(0,Heig_pyra):
    for x in range(0, n):
        print(end=" ")
    n=n-1
    for x in range(0,i+1):
        print("* ", end="")
    print("\r")
