import math
import random

def intToDotted(ip :int):
    # input: ip

    # determins dotted decimal format for given ip as int

    # returns list: octets
    octets = []
    while ip != 0:
        octets.append(ip % 256)
        ip = math.floor(ip / 256)
    octets.reverse()
    return octets


def printDotted(octets: list):
    # input: list containing octets

    # prints out the dotted decimal format
    # hint: use '.'.join()
    #returns nothing
    dottedIP = [str(octets[0]), str(octets[1]), str(octets[2]), str(octets[3])]
    x = ".".join(dottedIP)

    print(x)
    

def generateNetwork():
    # input: none
    # generates a random ip and prefix
    # the generated prefix should be in the range [8, 30]
    # to avoid getting too large and too small networks    
    # returns dict: {ip:int, prefix:int}
    ip = random.randint(0, 2**32-1)
    prefix = random.randint(8, 30)
    ipandprefix = {ip:int, prefix:int}
    return ipandprefix

def GetNetID(ip:int, prefix:int):
    snm=(2**prefix-1)<<(32-prefix)
    ip=ip&snm
    printDotted(intToDotted(ip))
    

def BroadcastID(ip:int, prefix:int):
    wmask = 0xffffffff >> prefix
    ip=ip|wmask
    printDotted(intToDotted(ip))


def analyseSubnet(ip:int, prefix:int):
    # input: ip as int, prefix as int
    

    # prints out net id, broadcast address,
    
    # and amount of addresses and amount of
    # usable adresses for a given subnet
    GetNetID(ip, prefix)
    BroadcastID(ip, prefix)


    # returns dict: {netid:int, bc:int}

def newSubnetExercises(ip:int, prefix:int):
    # input: a subnet, consisting of an ip
    # and a given prefix

    # generates a new subnet exercise
    # 1. determine the type of exercise
    #   types: split into x subnets
    #          split into subnets with x hosts
    # 2. print out the given subnet
    # 3. determine if there is optional exercises
    #    like determining a specific subnet (start, end), etc
    #    think of new types of exercises to add into this
    #    output logic
    # 4. print out the exercise:
    #   "split the given network into...."
    #   depending on the type of exercise

    # returns dict: {ip: int, prefix:int, newprefix:int}
    # newprefx contains the new subnet mask that solves the exercise
    print("no")

def listSubnets(ip: int, prefix:int, newprefix:int):
    # input: a network range and a subnet prefix to split into

    # note: sanity check with: assert newprefix > prefix
    # this function prints out every possible network
    # within the given range, showing net id and bc
    # as well as amount of adresses and usable hosts per network

    # returns: nothing, this just prints all possible subnets
    print("BLUB")
if __name__ == '__main__':
    print("blub")
    # 2. wait for user input, noting that the solution
    # will be shown after after pressing any key
    # 3. print the solution
    # 4. exit
