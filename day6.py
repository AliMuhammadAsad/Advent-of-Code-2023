INP = """Time:        49     78     79     80
Distance:   298   1185   1066   1181"""

races = [
    {'time': 49, 'distance': 298},
    {'time': 78, 'distance': 1185},
    {'time': 79, 'distance': 1066},
    {'time': 80, 'distance': 1181}
]

def wayWin(time, dist):
    ways = 0
    for hold_time in range(time):
        mt = time - hold_time
        total_distance = mt * hold_time
        if total_distance > dist:
            ways += 1
    return ways

ways_p_race = [wayWin(race["time"], race["distance"]) for race in races]

total = 1
for ways in ways_p_race: total *= ways

print("Part  1:", total)
single_time = 49787980
single_dist = 298118510661181
print("Part  2:", wayWin(single_time, single_dist))