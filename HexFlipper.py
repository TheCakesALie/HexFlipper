import binascii ##Imported for conversion: hex <--> binary
import sys ##Used to take arguments from the command line sys.argv[index of argument]
import argparse ##https://docs.python.org/3/library/argparse.html - User-friendly CLI stuff

print ("This is the name of the file: ", sys.argv[1])

if open(sys.argv[1], "rb"): # File opens just fine
    print("Opened!")
    print(sys.argv[1])



with open(sys.argv[1], 'rb') as f: # Getting a b'[our hex data]' between each chunk. That messes up the decode string
    while True:
        data = f.read(1024)
        if not data:
            break
        hexa = binascii.b2a_hex(data)
        #print (hexa)
        hexa_string = hexa.decode('utf-8')
        print (hexa_string)




""" print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))

print ("\n") """

""" parser = argparse.ArgumentParser(description="For all your hex flipping needs!")

# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers)) """