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
    We find a parabolic function in which d peaks at h = 1/2r
    This means holding the button for 1/2 of the race is optimal in every scenario
    We can add another variable, j, which is the record distance to beat like so:
        d = -h^2 + rh - j
    By plugging in 0 to d, and finding the min/max non-negative values, we can assert the following:
    (Given that the peak is at least 1 more than the record):
        If ceil(min) > floor(max), there is no way to win
        If ceil(min) == floor(max), there is one way to win
        if ceil(min) < floor(max), there are floor(max) - ceil(min) + 1 ways to win
    '''
    
    print()