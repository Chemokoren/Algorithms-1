"""

"""
def move(f, t):
    print("Move disc from {} to {}!".format(f,t))

move("A", "C")

def moveVia(f, v, t):
    move(f, v)
    move(v, t)
print(" ################################# move via #################################\n")

moveVia("A", "B", "C")


def hanoi(n, source, via, dest):

    """
    n  - number of disks
    source  - 'from' position
    via  - 'helper' position
    dest  - 'target' position
    """
    if n == 0:
        pass
    else:
        hanoi(n-1, source, dest, via)
        move(source,dest)
        hanoi(n-1, via, source, dest)

print(" ################################# tower of hanoi #################################\n")
hanoi(4, "A", "B", "C")