"""
(OA) - Particle Velocity

You are a programmer in a scientific team doing research into particles. As an experiment, you have
measured the position of a single particle in N equally distributed moments of time. The measurement
made in moment K is recorded in an array particles as particles[K].

Now, your job is to count all the periods of time when the movement of the particle was stable. 
Those are the periods during which the particle doesn't change its velocity: i.e. the difference 
between any two consecutive position measurements remains the same. Note that you need at least 
three measurements to be sure that the particle didn't change its velocity.

For Example

    1, 3, 5, 7, 9 is stable (velocity is 2)
    7, 7, 7, 7 is stable (particle stays in place)
    3, -1, -5, -9 is stable (velocity is 4)
    0, 1 is not stable (you need at least three measurements)
    1, 1, 2, 5, 7 is not stable (velocity changes between measurements)

More formally, your task is to find all the periods of time particles[P], particles[P+1], ....
particles[Q] (of length at least 3) during which the movement of the particle is stable. Note that
some periods of time might be contained in others (see below example).


Example:
Input: [-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]
Output: 5
Explanation:

Possible periods of time for which velocity is stable are:

values	        location(from, to)	    Velocity
[-1, 1, 3]	        (0,2)	                2
[3, 3, 3]	        (2,4)	                0
[3, 2, 1, 0]	    (6,9)	                -1
[3, 2, 1]	        (6,8)	                -1
[2, 1, 0]	        (7,9)	                -1

Note: Last two periods are contained by (6,9)

Write a function:

public static int particleVelocity(int[] particles)

that given array particles consisting of N integers representing the results of the measurements, 
returns the number of periods of time when the movement of the particle was stable. The function 
should return -1 if the result exceeds 10^9.

More examples:

Example 1:
Input: [1, 3, 5, 7, 9]
Output: 6
Explanation:

Possible periods of time for which velocity is stable are:

values	    location(from, to)	Velocity
[1, 3, 5]	    (0,2)	            2
[3, 5, 7]	    (1,3)	            2
[5, 7, 9]	    (2,4)	            2
[1, 3, 5, 7, 9]	(0,4)	            2
[1, 3, 5, 7]	(0,3)	            2
[3, 5, 7, 9]	(1,4)	            2

Example 2:
Input: [7, 7, 7, 7]
Output: 3
Explanation:

Possible periods of time for which velocity is stable are:

values	        location(from, to)	Velocity
[7, 7, 7, 7]	    (0,3)	        0
[7, 7, 7]	        (1,3)	        0
[7, 7, 7]	        (0,2)	        0

"""
def particleVelocity(particles):
    numStable = 0
    if len(particles) < 3:
        return 0
    for i in range(len(particles) -2):
        for j in range(i + 1, len(particles) -1):
            if particles[j + 1] - particles[j] == particles[i + 1] - particles[i]:
                numStable += 1
            else:
                break
    return numStable if numStable < 1000000000 else -1

if __name__ =='__main__':
    nlist =[7, 7, 7, 7]
    elevs =[int(x) for x in nlist]
    # elevs =[int(x) for x in input().split()]
    print(particleVelocity(elevs))
