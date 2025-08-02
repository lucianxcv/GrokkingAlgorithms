states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)

"""
XPLANATION (Line by Line):
states_needed = set([...])
– This is the list of all the states we need to cover.

stations = { ... }
– This dictionary maps each station to the states it covers.

final_stations = set()
– This will hold the minimum set of stations we select in the end.

while states_needed:
– Keep looping until all the states are covered.

best_station = None
– We’ll store the station that covers the most uncovered states in this round.

states_covered = set()
– Stores the states that this round’s best station will cover.

for station, states in stations.items():
– Loop through all stations.

covered = states_needed & states
– Find the intersection between uncovered states and the current station's coverage.

if len(covered) > len(states_covered):
– If this station covers more states than the previous best, we update the best.

After the loop:
– The best station is added to our final result.

states_needed -= states_covered
– We remove the states now covered from the set of states we still need.

final_stations.add(best_station)
– Save the selected station.

Finally, print the selected stations.

"""