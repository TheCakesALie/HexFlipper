import binascii ##Imported for conversion: hex <--> binary
import sys ##Used to take arguments from the command line sys.argv[index of argument]
import argparse ##https://docs.python.org/3/library/argparse.html - User-friendly CLI stuff


def main():
    #file2hex() # Just convert file to hex and writes it out
    flip_bits() # Converts file to hex and flips bits   

def file2hex(): # Works
    index = [] # Creation of index
    o = open(sys.argv[2],'w+') # Opens file for writing
    with open(sys.argv[1], 'rb') as n: # Open file for reading in binary mode
        while True: # While file is open
            data = n.read(1) # Read in one chunk at a time
            if not data: # ?
                break
            index.append(binascii.b2a_hex(data)) # Convert binary chunk to hex and append to list

    for i in index: # Print out contents of list to file
        o.write(i)
    
    o.close() # close file for writing

###################################################################################################################
################################### FLIP BITS #####################################################################
###################################################################################################################

def flip_bits(): # ex. ab ac 4e 2d 5c -> ac ab 2d 4e 5c
    index = [] # Creation of index
    o = open(sys.argv[2] + "_flip",'w+') # Opens file for writing
    with open(sys.argv[1], 'rb') as n: # Open file for reading in binary mode
        while True: # While file is open
            data = n.read(1) # Read in one chunk at a time
            if not data: # ?
                break
            index.append(binascii.b2a_hex(data)) # Convert binary chunk to hex and append to list

    indexOut = [None] * len(index)

    a = 0

    if len(index)%2 == 0: # If number of hex bytes are even
        while a < len(index):
            indexOut[a] = index[a+1]
            indexOut[a+1] = index[a]
            a +=2
    else: # If number of hex bytes are odd
        while a < len(index): 
            if a+1 == len(index): 
                indexOut[a] = index[a]
                break
            indexOut[a] = index[a+1]
            indexOut[a+1] = index[a]
            a +=2
    
    #hex2ascii = ''

    for i in indexOut: # Print out contents of list to file
        o.write(i)
        #hex2ascii += i

    #print(hex2ascii.decode('utf-8'))
    #bytes.fromhex(hex2ascii)

    #print(newFile)
    o.close() # close file for writing
    # Need to convert back to ascii



# parser = argparse.ArgumentParser(description="For all your hex flipping needs!")

# # parser.add_argument('integers', metavar='N', type=int, nargs='+',
# #                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print(args.accumulate(args.integers))

if __name__ == "__main__":
    main()