import math

# Used in both solutions
def waysToWin(time, distance):
    '''
    Using the following:
        d - distance travelled
        r - race time
        h - time holding button (in ms)
        t - time spent traveling
        i - initial speed (in mm/ms)
        h = i
        t = r - h
        d = t * i
        d = (r - h) * h
        d = -h^2 + rh
    We find a parabolic function at which d peaks at h = 1/2r
    This means holding the button for 1/2 of the race is optimal in every scenario
    We can add another variable, j, which is the record distance to beat (record + 1 i think) like so:
        d = -h^2 + rh - j
    This results in d being the distance greater than the minimum new record (0 = min new record)
    By plugging in 0 to d, and finding the min/max non-negative values, we can assert the following:
    (Given that the peak is at least 1 more than the record):
        If ceil(min) > floor(max), there is no way to win
        If ceil(min) == floor(max), there is one way to win
        if ceil(min) < floor(max), there are floor(max) - ceil(min) + 1 ways to win
    '''
    j, r = int(distance) + 1, int(time)
    vX = r / 2
    vY = -pow(vX, 2) + r * vX - j
    if vY < 0: return 0
    lx = math.ceil(( math.sqrt(pow(r, 2) - 4 * j) - r)/(-2))
    rx = math.floor((-math.sqrt(pow(r, 2) - 4 * j) - r)/(-2))
    if lx > rx: return 0
    if lx < rx: return rx - lx + 1

# Part 1
with open("input.txt") as file:
    times = file.readline()[10:].split()
    distances = file.readline()[10:].split()
result = 1
for time, distance in zip(times, distances):
    num = waysToWin(time, distance)
    result *= num if num > 0 else 1
print(f"Part 1: {result}")

# Part 2
with open("input.txt") as file:
    time = "".join(file.readline()[10:].split())
    distance = "".join(file.readline()[10:].split())
result = waysToWin(time, distance)
print(f"Part 2: {result}")