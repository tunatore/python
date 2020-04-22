# merge intervals


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


# Time complexity O(N * logN) and space complexity O(N)
def merge2(intervals):
    if intervals is None:
        return None

    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda interval: interval.start)
    merged = []
    start, end = intervals[0].start, intervals[0].end

    for index in range(1, len(intervals)):
        interval = intervals[index]
        if interval.start < end:  # overlap
            end = max(interval.end, end)
        else:  # not overlapping
            merged.append(Interval(start, end))
            start = interval.start
            end = interval.end
    # last interval
    merged.append(Interval(start, end))
    return merged


# Time complexity O(N * logN) and space complexity O(N)
def merge(intervals):
    if intervals is None:
        return None

    if len(intervals) < 2:
        return intervals

    merged = []
    interval_sorted = sorted(intervals, key=lambda interval: interval.start)

    for interval in interval_sorted:
        if len(merged) == 0:
            merged.append(interval)
        else:
            last_interval = merged.pop()
            if last_interval.start < interval.start \
                    and last_interval.start < interval.start < last_interval.end \
                    and last_interval.end < interval.end:
                merged_interval = Interval(last_interval.start, interval.end)
                merged.append(merged_interval)
            elif last_interval.start < interval.start and \
                    last_interval.end > interval.end:
                merged_interval = Interval(last_interval.start, last_interval.end)
                merged.append(merged_interval)
            elif last_interval.start == interval.start and \
                    last_interval.end < interval.end:
                merged_interval = Interval(last_interval.start, interval.end)
                merged.append(merged_interval)
            else:
                merged.append(last_interval)
                merged.append(interval)
    return merged


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9), Interval(1, 10)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
