import math

# Part 1
with open("input.txt") as file:
    # in ms
    times = file.readline()[10:].split()
    # in mm
    distances = file.readline()[10:].split()

print(times, distances)

for time, distance in zip(times, distances):
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
    So:
        Find the x-intercept points
        If peak distance < 0
    '''

    # hold time
    h = 1
    # distance required to beat record
    j = distance + 1
    r = time
    # get the distance based on hold time
    d = -(h^2) + r * h - j
    # left x-intersect
    lx = ( math.sqrt(pow(r, 2) - 4 * j) - r)/(-2)
    rx = (-math.sqrt(pow(r, 2) - 4 * j) - r)/(-2)

    print(time, distance)