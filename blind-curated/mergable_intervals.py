


def merge(intervals):
    ans = []
    
    intervals = sorted(intervals, key=lambda x: x[0])
    print(intervals)
    merged_intervals = [intervals[0]]

    for interval in intervals[1:]:
        print(interval, merged_intervals[-1])
        if interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        else:
            merged_intervals.append(interval)
    return merged_intervals



if __name__ == "__main__":
    a = [[1,3],[2,6],[8,10],[15,18]] # [[1, 6], [8, 10], [15, 18]]
    b = [[1,4],[0,1]] # [[0, 4]]
    c = [[1,4],[0,4]] # [[0, 4]]
    d = [[1,4],[0,0]] # [[0, 0], [1, 4]]
    e = [[1,4],[0,2],[3,5]] # [[0, 5]]
    print(merge(e))