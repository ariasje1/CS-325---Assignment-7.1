#Author: Jesus Arias
#GitHub username: ariasje1
#Date: 07/31/2025
#Description: Generate the powerset of a given list
def powerset(input_set):
    """
    Generate the powerset of a given list.

    Parameters:
        input_set (List[Any]): The input list of elements.

    Returns:
        List[List[Any]]: A list containing all subsets of the input list.
    """
    result = []   # This will store all subsets
    subset = []   # Temporary list to build current subset

    def dfs(index):
        # Base case: if we've considered all elements
        if index >= len(input_set):
            result.append(subset[:])  # Add a copy of the current subset
            return

        # Choice 1: Include input_set[index] in the subset
        subset.append(input_set[index])
        dfs(index + 1)

        # Backtrack: remove last element before exploring exclusion path
        subset.pop()

        # Choice 2: Exclude input_set[index] and move forward
        dfs(index + 1)

    dfs(0)  # Start recursion from the first index
    return result

