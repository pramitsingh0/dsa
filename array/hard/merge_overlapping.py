def mergeIntervals(intervals):
    n = len(intervals)
    intervals.sort()
    result = []
    for i in range(n):
        end = intervals[i][1]
        start = intervals[i][0]
        if len(result) and end <= result[-1][1]:
            continue

        for j in range(i + 1, n):
            if intervals[j][0] <= end:
                end = max(end, intervals[j][1])
            else:
                break
        result.append([start, end])
    return result


def mergeIntervelsOptimal(intervals):
    n = len(intervals)
    intervals.sort()
    result = []
    for i in range(n):
        if len(result) == 0 or intervals[i][0] > result[-1][1]:
            result.append(intervals[i])
        else:
            result[-1][1] = intervals[i][1]
    return result



arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
mergedArr = mergeIntervelsOptimal(arr)
print(mergedArr)
