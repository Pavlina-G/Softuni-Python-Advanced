def ranges_split(ranges):
    sets_range = []
    for r in ranges:
        start = int(r.split(',')[0])
        end = int(r.split(',')[1])
        range_nums = set(n for n in range(start, end + 1))
        sets_range.append(range_nums)

    return sets_range


def longest_intersection(sets):
    longest_intersec = set()
    for s in sets:
        if len(s) > len(longest_intersec):
            longest_intersec = s

    return longest_intersec


def sets_longest_intersection():
    n = int(input())
    intersections = []
    for i in range(n):
        ranges = input().split('-')
        set1, set2 = ranges_split(ranges)
        sets_intersection = set1.intersection(set2)
        intersections.append(sets_intersection)

    longest_intersection_of_sets = longest_intersection(intersections)
    print(
        f'Longest intersection is {list(longest_intersection_of_sets)} with length {len(longest_intersection_of_sets)}')


sets_longest_intersection()
