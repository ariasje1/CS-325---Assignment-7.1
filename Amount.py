#Author: Jesus Arias
#GitHub username: ariasje1
#Date: 07/31/2025
#Description:
def powerset(input_set):
    result = []

    def backtrack(start, current):
        # Append a copy of current subset to result
        result.append(current[:])

        for i in range(start, len(input_set)):
            # Include input_set[i]
            current.append(input_set[i])
            # Recurse
            backtrack(i + 1, current)
            # Backtrack
            current.pop()

    backtrack(0, [])
    return result

# Example usage
if __name__ == "__main__":
    print(powerset([1, 2, 3]))  # Output: [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
