# 6.00.2x Problem Set 2: Simulating robots
"""
Simulation Overview
iRobot is a company (started by MIT alumni and faculty) that sells the 
Roomba vacuuming robot (watch one of the product videos to see these robots
 in action). Roomba robots move around the floor, cleaning the area they pass 
over.

In this problem set, you will code a simulation to compare how much 
time a group of Roomba-like robots will take to clean the floor of a 
room using two different strategies.

The following simplified model of a single robot moving in a square 5x5 
room should give you some intuition about the system we are simulating.

The robot starts out at some random position in the room, and with a random
 direction of motion. The illustrations below show the robot's position 
 (indicated by a black dot) as well as its direction (indicated by the
 direction of the red arrowhead).

  
Time t = 0
The robot starts at the position (2.1, 2.2) with an angle of 205 degrees 
(measured clockwise from "north"). The tile that it is on is now clean.

  
t = 1
The robot has moved 1 unit in the direction it was facing, 
to the position (1.7, 1.3), cleaning another tile.

  
t = 2
The robot has moved 1 unit in the same direction
 (205 degrees from north), to the position (1.2, 0.4), 
 cleaning another tile.

  
t = 3
The robot could not have moved another unit in the 
same direction without hitting the wall, so instead it
 turns to face in a new, random direction, 287 degrees.

  
t = 4
The robot moves along its new direction to the
 position (0.3, 0.7), cleaning another tile.

Simulation Details
Here are additional details about the simulation model. 
Read these carefully.

Multiple robots
In general, there are N > 0 robots in the room, 
where N is given. For simplicity, assume that robots 
are points and can pass through each other or occupy 
the same point without interfering.

The room
The room is rectangular with some integer width w and height h, 
which are given. Initially the entire floor is dirty. A robot cannot
 pass through the walls of the room. A robot may not move to a point 
 outside the room.

Tiles
You will need to keep track of which parts of the floor have been
 cleaned by the robot(s). We will divide the area of the room into 
 1x1 tiles (there will be w * h such tiles). When a robot's location
 is anywhere in a tile, we will consider the entire tile to be cleaned
 (as in the pictures above). By convention, we will refer to the tiles
 using ordered pairs of integers: (0, 0), (0, 1), ..., (0, h-1), (1, 0), (1, 1), 
 ..., (w-1, h-1).

Robot motion rules
Each robot has a position inside the room. We'll represent
 the position using coordinates (x, y) which are floats satisfying
 0 ≤ x < w and 0 ≤ y < h. In our program we'll use instances of the 
 Position class to store these coordinates.

A robot has a direction of motion. We'll represent the direction using an 
integer d satisfying 0 ≤ d < 360, which gives an angle in degrees.

All robots move at the same speed s, a float, which is given and is 
constant throughout the simulation. Every time-step, a robot moves in 
its direction of motion by s units.

If a robot detects that it will hit the wall within the time-step,
 that time step is instead spent picking a new direction at random.
 The robot will attempt to move in that direction on the next time step,
 until it reaches another wall.

Termination
The simulation ends when a specified fraction of the tiles in the room
 have been cleaned.



Introduction
In this problem set you will practice designing a simulation 
and implementing a program that uses classes.

As with previous problem sets, please don't be discouraged by the 
apparent length of this assignment. There is quite a bit to read and 
understand, but most of the problems do not involve writing much code.



pset2.zip: A zip file of all the files you need, including:

ps2.py, a skeleton of the solution.

ps2_visualize.py, code to help you visualize the robot's movement 
(an optional - but cool! - part of this problem set).

ps2_verify_movement35.pyc, precompiled module for Python 3.5 that 
assists with the visualization code. In ps2.py you will uncomment 
this out if you have Python 3.5.

ps2_verify_movement36.pyc, precompiled module for Python 3.6 that
 assists with the visualization code. In ps2.py you will uncomment 
 this out if you have Python 3.6.
"""
import math
import random

import ps2_visualize
import pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
#from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 

# For Python 3.6:
from ps2_verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
"""
You will need to design two classes to keep track of which parts of
 the room have been cleaned as well as the position and direction of each robot.

In ps2.py, we've provided skeletons for the following two classes,
 which you will fill in in Problem 1:

RectangularRoom: Represents the space to be cleaned and keeps track of
 which tiles have been cleaned.
Position: We've also provided a complete implementation of this class. 
It stores the x- and y-coordinates of a robot in a room.
Read ps2.py carefully before starting, so that you understand
 the provided code and its capabilities.

Problem 1
In this problem you will implement the RectangularRoom class.
 For this class, decide what fields you will use and decide how 
 the following operations are to be performed:

Initializing the object
Marking an appropriate tile as cleaned when a robot moves to a given position (casting floats to ints - and/or the function math.floor - may be useful to you here)
Determining if a given tile has been cleaned
Determining how many tiles there are in the room
Determining how many cleaned tiles there are in the room
Getting a random position in the room
Determining if a given position is in the room
Complete the RectangularRoom class by implementing its methods in ps2.py.

"""
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.rectRoom = [] #initialize a list for the tile coordinates
        self.width = width 
        self.height = height
        
        clean = False
        #create the coordinate pairs of the tiles and add a 3rd element: if it's clean or not
        for w in range(width):
            for h in range(height):
                tile = [w, h, clean]
                self.rectRoom.append(tile)
            
    def __str__ (self):
        for tile in self.rectRoom:
            print(tile)
    
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        x = int(pos.getX())
        y = int(pos.getY())
        clean = False
        toclean = [x, y, clean]
        
        for tile in self.rectRoom:
            if toclean == tile:
                tile[2] = True
        

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        clean = True
        toCheck = [m, n, clean]
        for tile in self.rectRoom:
            if toCheck in self.rectRoom:
                return True
        return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        count = 0
        for tile in self.rectRoom:
            count +=1
        return count
        

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        cleaned = 0
        for tile in self.rectRoom:
            if tile[2] == True:
                cleaned +=1
        return cleaned

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x = random.randint(0, self.width-1)
        y = random.randint(0, self.height-1)
        return Position(x, y)
        

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        x = pos.getX()
        y = pos.getY()
        if x < 0 or y < 0:
            return False
        if x >= self.width:
            return False
        if y >= self.height:
            return False
        return True


# === Problem 2
"""
In ps2.py we provided you with the Robot class, which stores the position 
and direction of a robot. For this class, decide what fields you will use 
and decide how the following operations are to be performed:

Initializing the object
Accessing the robot's position
Accessing the robot's direction
Setting the robot's position
Setting the robot's direction
Complete the Robot class by implementing its methods in ps2.py.

Note: When a Robot is initialized, it should clean the first tile it is
 initialized on. Generally the model these Robots will follow is that after
 a robot lands on a given tile, we will mark the entire tile as clean. This
 might not make sense if you're thinking about really large tiles, but as we
 make the size of the tiles smaller and smaller, this does actually become a 
 pretty good approximation.

In the final implementation of Robot, not all methods will be implemented.
 Not to worry -- its subclass(es) will implement the method updatePositionAndClean()


"""
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.speed = speed
        self.room = room
        self.pos = room.getRandomPosition()
        self.room.cleanTileAtPosition(self.pos)
        self.direction = random.randint(0, 359)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.pos = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 3
"""
Each robot must also have some code that tells it how to move about a room,
 which will go in a method called updatePositionAndClean.

Ordinarily we would consider putting all the robot's methods in a
 single class. However, later in this problem set we'll consider 
 robots with alternate movement strategies, to be implemented as different
 classes with the same interface. These classes will have a different
 implementation of updatePositionAndClean but are for the most part the
 same as the original robots. Therefore, we'd like to use inheritance to
 reduce the amount of duplicated code.
"""
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        while self.room.isPositionInRoom(self.pos.getNewPosition(self.direction, self.speed)) == False:
             self.direction = random.randint(0, 359)           
            
        self.pos = self.pos.getNewPosition(self.direction, self.speed)
        self.room.cleanTileAtPosition(self.pos)
        
            
            

# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps (meanSteps) needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    meanSteps = 0 
    for num in range (num_trials):
        steps = oneSim(num_robots, speed, width, height, min_coverage, robot_type)
        meanSteps += steps
    meanSteps /= num_trials
    return meanSteps

def oneSim(num_robots, speed, width, height, min_coverage, robot_type):
    steps = 0

    #create the room
    room = RectangularRoom(width, height)
    
    #initialize the robots in the room
    robots = []
    for robot in range(num_robots):
        robots.append(robot_type(room, speed))
        
    #clean until min_coverage is reached, keep track of steps
    cleanRatio = room.getNumCleanedTiles() / room.getNumTiles()
    while min_coverage > cleanRatio:
        for robot in robots:
            robot.updatePositionAndClean()
        steps +=1
        cleanRatio = room.getNumCleanedTiles() / room.getNumTiles()
    
    return steps
    
        
        

# Uncomment this line to see how much your simulation takes on average
#print(runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot))


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.pos = self.pos.getNewPosition(self.direction, self.speed)
        self.room.cleanTileAtPosition(self.pos)
        self.direction = random.randint(0, 359) 
        



