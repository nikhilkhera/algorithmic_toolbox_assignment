# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def myfunc(n):
    return n.end

def optimal_points(segments,n):
    points=[]
    i=0
    while i <n:
        points.append(segments[i].end)
        i=i+1
        if i>=n:
            break
        while segments[i].start<=points[-1] :
            i=i+1
            if i>=n:
                break
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    segments.sort(key= myfunc)
    points = optimal_points(segments,n)
    print(len(points))
    print(*points)