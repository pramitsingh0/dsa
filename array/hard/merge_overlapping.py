def mergeIntervals(intervals):
    intervals.sort()
    result = []
    for i in range(len(intervals)):
        if len(result) == 0 or intervals[i][0] > result[-1][1]:
            result.append(intervals[i])
        else:
            result[-1][1] = intervals[i][1]
    return result


print(mergeIntervals([[1, 4], [4, 5]]))
