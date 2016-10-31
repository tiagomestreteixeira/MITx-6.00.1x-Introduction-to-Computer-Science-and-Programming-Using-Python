# If L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] then the longest run of monotonically increasing numbers in L is [3, 4, 5, 7, 7]
# and the longest run of monotonically decreasing numbers in L is [10, 4, 3]. Your function should return the value 26
# because the longest run of monotonically increasing integers is longer than the longest run of monotonically decreasing numbers.

# If L = [5, 4, 10] then the longest run of monotonically increasing numbers in L is [4, 10] and the longest run of
# monotonically decreasing numbers in L is [5, 4]. Your function should return the value 9 because the longest run of
# monotonically decreasing integers occurs before the longest run of monotonically increasing numbers.

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    greater_sequence_number = 1
    start_idx, end_idx, current_idx = 0, 0, 0
    sprint_idx = 0
    lenght_list = len(L)
    while current_idx < (lenght_list - 1):
        current_idx = sprint_idx
        while (current_idx + 1) < lenght_list and L[current_idx + 1] >= L[current_idx]:
            current_idx += 1

        if (current_idx - sprint_idx + 1) > greater_sequence_number:
            start_idx = sprint_idx
            end_idx = current_idx
            greater_sequence_number = end_idx - start_idx + 1

        current_idx = sprint_idx
        while (current_idx + 1) < lenght_list and L[current_idx + 1] <= L[current_idx]:
            current_idx += 1

        if (current_idx - sprint_idx + 1) > greater_sequence_number:
            start_idx = sprint_idx
            end_idx = current_idx
            greater_sequence_number = end_idx - start_idx + 1

        sprint_idx += 1
    return sum(L[start_idx:(end_idx + 1)])


longest_run([5, 4, 10])
longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2])
