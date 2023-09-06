import math
import random
def intToDotted(ip):
    # input: ip

    # determins dotted decimal format for given ip as int

    # returns list: octets
    octets = []
    while ip != 0:
        octets.append(ip % 256)
        ip = math.floor(ip / 256)
    octets.reverse()
    return octets


def printDotted(octets):
    # input: list containing octets

    # prints out the dotted decimal format
    # hint: use '.'.join()
    #returns nothing
    dottedIP = [str(octets[0]), str(octets[1]), str(octets[2]), str(octets[3])]
    x = ".".join(dottedIP)

    return x    

def generateNetwork():
    # input: none
    # generates a random ip and prefix
    # the generated prefix should be in the range [8, 30]
    # to avoid getting too large and too small networks    
    # returns dict: {ip:int, prefix:int}
    ip = random.randint(0, 2**32-1)
    prefix = random.randint(8, 30)
    ipandprefix = {"ip":ip, "prefix":prefix}
    return ipandprefix

    
def getnetid(ip, prefix):
    snm=(2**prefix-1)<<(32-prefix)
    netid = ip&snm
    return netid

def analyseSubnet(ip, prefix):
    # input: ip as int, prefix as int
    

    # prints out net id, broadcast address, 
    
    # and amount of addresses and amount of
    # usable adresses for a given subnet 

    
    wmask = 0xffffffff >> prefix
    bid = ip|wmask
    
    hostbits = 32 - prefix
    hosts = 2**hostbits-2
    print("Useable Hosts: {}".format(hosts))
    ids = {"bid":bid}
    return ids
    # returns dict: {netid:int, bc:int}

def newSubnetExercises(ip, prefix):
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
    print("Generating new Subnet exercise...")
    aufgabentyp = random.randint(0,1)
    bonusaufgabe = random.randint(0,10)
    newprefix = random.randint(prefix, 31)


    
    print(printDotted(intToDotted(ip)))
    print("Prefix: ", prefix)
    if aufgabentyp == 0:
        print("You will have to split the subnet into {} subnets".format(random.randint(2,10)))
    else:
        print("Split subnet into subnet with {} Hosts".format(random.randint(8,254)))
    
    if bonusaufgabe > 5:
        print("What is the Net ID of the given subnet?")
        print("What is the start and end of the Subnet")
    if bonusaufgabe > 8:
        print("What is the Adress of the next subnet?")

    subnetdic = {"ip":ip, "prefix":prefix, "newprefix":newprefix}
    return subnetdic

def listSubnets(ip, prefix, newprefix):
    # input: a network range and a subnet prefix to split into DONE

    # note: sanity check with: assert newprefix > prefix DONE
    # this function prints out every possible network ???
    # within the given range, showing net id and bc DONE        
    # as well as amount of adresses and usable hosts per network DONE
    # returns: nothing, this just prints all possible subnets DONE
    nid = getnetid(ip, prefix)
    print(newprefix)
    hostbits = 32 - newprefix
    newnetbits = newprefix - prefix
    newnetbits = 2**newnetbits
    for i in range(0,newnetbits):
        print(printDotted(intToDotted(nid +i*2**hostbits)))
        if i > 25:
            break


if __name__ == '__main__':
    ipdic = generateNetwork()
    ip = ipdic.get("ip")
    prefix = ipdic.get("prefix")
    newprefixdic = newSubnetExercises(ip=ip, prefix=prefix)
    if input("Press Space and enter to continue") != "":
        listSubnets(ip, prefix, newprefixdic.get("newprefix"))
    # 1. Generate new exercise
    # 2. wait for user input, noting that the solution
    # will be shown after after pressing any key
    # 3. print the solution
    # 4. exit
