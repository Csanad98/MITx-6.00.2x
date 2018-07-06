"""
Intro:
Space Cows Introduction
A colony of Aucks (super-intelligent alien bioengineers) has landed on Earth and has created new species of farm animals! The Aucks are performing their experiments on Earth, and plan on transporting the mutant animals back to their home planet of Aurock. In this problem set, you will implement algorithms to figure out how the aliens should shuttle their experimental animals back across space.

Getting started!

Download pset1.zip from the website.

Please do not rename the files we provide you with, change any of the provided helper functions, change function/method names, or delete provided docstrings. You will need to keep ps1_partition.py and ps1_cow_data.txt in the same folder as ps1.py.


Transporting Cows Across Space!

The aliens have succeeded in breeding cows that jump over the moon! Now they want to take home their mutant cows. The aliens want to take all chosen cows back, but their spaceship has a weight limit and they want to minimize the number of trips they have to take across the universe. Somehow, the aliens have developed breeding technology to make cows with only integer weights.

The data for the cows to be transported is stored in ps1_cow_data.txt. All of your code for Part A should go into ps1.py.

First we need to load the cow data from the data file ps1_cow_data.txt, this has already been done for you and should let you begin working on the rest of this problem. If you are having issues getting the ps1_cow_data.txt to load, be sure that you have it in the same folder as the ps1.py that you are running.

You can expect the data to be formatted in pairs of x,y on each line, where x is the name of the cow and y is a number indicating how much the cow weighs in tons, and that all of the cows have unique names. Here are the first few lines of ps1_cow_data.txt:

Maggie,3
Herman,7
Betsy,9
...
"""



"""
Problem 1

One way of transporting cows is to always pick the heaviest cow that will fit onto the spaceship first. This is an example of a greedy algorithm. So if there are only 2 tons of free space on your spaceship, with one cow that's 3 tons and another that's 1 ton, the 1 ton cow will get put onto the spaceship.

Implement a greedy algorithm for transporting the cows back across space in the function greedy_cow_transport. The function returns a list of lists, where each inner list represents a trip and contains the names of cows taken on that trip.

Note: Make sure not to mutate the dictionary of cows that is passed in!

Assumptions:

The order of the list of trips does not matter. That is, [[1,2],[3,4]] and [[3,4],[1,2]] are considered equivalent lists of trips.
All the cows are between 0 and 100 tons in weight.
All the cows have unique names.
If multiple cows weigh the same amount, break ties arbitrarily.
The spaceship has a cargo weight limit (in tons), which is passed into the function as a parameter.
Example:

Suppose the spaceship has a weight limit of 10 tons and the set of cows to transport is {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}.

The greedy algorithm will first pick Jesse as the heaviest cow for the first trip. There is still space for 4 tons on the trip. Since Maggie will not fit on this trip, the greedy algorithm picks Maybel, the heaviest cow that will still fit. Now there is only 1 ton of space left, and none of the cows can fit in that space, so the first trip is [Jesse, Maybel].

For the second trip, the greedy algorithm first picks Maggie as the heaviest remaining cow, and then picks Callie as the last cow. Since they will both fit, this makes the second trip [[Maggie], [Callie]].

The final result then is [["Jesse", "Maybel"], ["Maggie", "Callie"]].

"""

###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


cows = load_cows("ps1_cow_data.txt")
limit=10

# Problem 1
def greedy_cow_transport(cows, limit):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cowsleft=len(cows)
    alltrips =[]
    def findBiggestCow(cowsdict, limit):
        lowest = limit
        copiedcows = cowsdict.copy()    
        maxname = ''
        maxscore = 0
        for cow in copiedcows.items():
            name = cow[0]  
            weight = cow[1]
            if weight > maxscore:
                maxscore = weight
                maxname = name
            if weight < lowest:
                lowest = weight        
        ans = (maxname, maxscore)        
        return ans      
    
    copiedcows = cows.copy()
    
    
    
    while cowsleft != 0:
        
        trip = []
        spaceleft = limit
        checkedcows = copiedcows.copy()
        while checkedcows != {}:
            if checkedcows == {}:
                break
            cow = findBiggestCow(checkedcows, limit)
            weight = cow[1]
            if spaceleft >= weight:
                name = cow[0]
                trip.append(name)
                trip.append(weight)
                del checkedcows[name]
                cowsleft -=1
                spaceleft -= cow[1]
                del copiedcows[name]
                
            else:
                name = cow[0]
                del checkedcows[name]
            
                
        
          
        alltrips.append(trip)
    
    
    return(alltrips)
    
            
"""
Part 2: Brute Force Cow Transport

Another way to transport the cows is to look at every possible combination of trips and pick the best one. This is an example of a brute force algorithm.

Implement a brute force algorithm to find the minimum number of trips needed to take all the cows across the universe in the function brute_force_cow_transport. The function returns a list of lists, where each inner list represents a trip and contains the names of cows taken on that trip.

Notes:

Make sure not to mutate the dictionary of cows!
In order to enumerate all possible combinations of trips, you will want to work with set partitions. We have provided you with a helper function called get_partitions that generates all the set partitions for a set of cows. More details on this function are provided below.
Assumptions:

Assume that order doesn't matter. (1) [[1,2],[3,4]] and [[3,4],[1,2]] are considered equivalent lists of trips. (2) [[1,2],[3,4]] and [[2,1],[3,4]] are considered the same partitions of [1,2,3,4].
You can assume that all the cows are between 0 and 100 tons in weight.
All the cows have unique names.
If multiple cows weigh the same amount, break ties arbitrarily.
The spaceship has a cargo weight limit (in tons), which is passed into the function as a parameter.
Helper function get_partitions in ps1_partitions.py:

To generate all the possibilities for the brute force method, you will want to work with set partitions.

For instance, all the possible 2-partitions of the list [1,2,3,4] are [[1,2],[3,4]], [[1,3],[2,4]], [[2,3],[1,4]], [[1],[2,3,4]], [[2],[1,3,4]], [[3],[1,2,4]], [[4],[1,2,3]].

To help you with creating partitions, we have included a helper function get_partitions(L) that takes as input a list and returns a generator that contains all the possible partitions of this list, from 0-partitions to n-partitions, where n is the length of this list.

You can review more on generators in the Lecture 2 Exercise 1. To use generators, you must iterate over the generator to retrieve the elements; you cannot index into a generator! For instance, the recommended way to call get_partitions on a list [1,2,3] is the following. Try it out in ps1_partitions.py to see what is printed!

for partition in get_partitions([1,2,3]):
    print(partition)
Example:

Suppose the spaceship has a cargo weight limit of 10 tons and the set of cows to transport is {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}.

The brute force algorithm will first try to fit them on only one trip, ["Jesse", "Maybel", "Callie", "Maggie"]. Since this trip contains 16 tons of cows, it is over the weight limit and does not work. Then the algorithm will try fitting them on all combinations of two trips. Suppose it first tries [["Jesse", "Maggie"], ["Maybel", "Callie"]]. This solution will be rejected because Jesse and Maggie together are over the weight limit and cannot be on the same trip. The algorithm will continue trying two trip partitions until it finds one that works, such as [["Jesse", "Callie"], ["Maybel", "Maggie"]].

The final result is then [["Jesse", "Callie"], ["Maybel", "Maggie"]]. Note that depending on which cow it tries first, the algorithm may find a different, optimal solution. Another optimal result could be [["Jesse", "Maybel"],["Callie", "Maggie"]].
"""       

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    optimaltrip = []
    
    allcows = cows
    mintripcount = len(allcows)
    for trips in (get_partitions(allcows)):
        tripcount = len(trips)
        weight = 0
        for trip in trips:
            if weight > limit:   
                break
            weight = 0 
            for cowname in trip:
                weight += allcows[cowname]
                if weight > limit:
                    break
        if mintripcount >= tripcount and weight <= limit:
            mintripcount = tripcount
            optimaltrip = trips
    
    
    return optimaltrip 
        
        
        
        
        
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    print(greedy_cow_transport(cows, limit))
    end = time.time()
    print("Greedy:", end - start)
    start = time.time()
    print(brute_force_cow_transport(cows,limit=10))
    end = time.time()
    print("Greedy:", end - start)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""
print(compare_cow_transport_algorithms())

#print(cows)

#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport({'Daisy': 50, 'Betsy': 65, 'Buttercup': 72}, 75))
#print(cows)
#print(greedy_cow_transport(cows, 10))
