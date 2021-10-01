# python3
import sys


def compute_min_refills(distance, tank,no_stops, stops):
    # write your code here
    numrefils=0
    stops.append(distance)
    stops.insert(0,0)
    current_refill=0
    while current_refill <= no_stops:
        last_Refill = current_refill
        while(current_refill<=no_stops) and stops[current_refill+1]-stops[last_Refill]<=tank:
            current_refill=current_refill+1
        if current_refill==last_Refill:
            return -1
        if current_refill<=no_stops:
            numrefils=numrefils+1
    return numrefils

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m,_, stops))
