'''
Given an array a, your task is to output an array b of the same length by applying the following transformation: 
– For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
– If an element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, use 0 in its place
– For instance, b[0] = 0 + a[0] + a[1]

Example

For a = [4, 0, 1, -2, 3]: 
– b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
– b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
– b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
– b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
– b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1

So, the output should be solution(a) = [4, 5, -1, 2, 1].
Taking a look at this question, you can see that it covers a basic array traversal and manipulation. The candidate simply needs to return the sum of each value in a, plus its right and left neighbors. 

At the same time, the question asks candidates to take into account corner cases with their implementation, which is an important fundamental skill. They need to correctly handle the first and last elements of the array. 
'''

# Resolver con:
# Anterior, actual, siguiente

def solution(input_list):
    '''
    This function returns a list where each element is calculated based on
    the sum of the center and neighbor values of an input list.

    Example:
    If a = [1, 2, 3, 4], the function returns [3, 6, 9, 7].
    '''
    
    output_list = []

    # Iterate through elements of input list:
    for i in range(len(input_list)):
        
        # Case: First element
        # Value will be the sum of actual and next element.
        if i == 0:
            output_list.append(input_list[i] + input_list[i+1])
        
        # Case: Last element
        # Value will be the sum of the previous and actual element.
        elif i == (len(input_list) - 1):
            output_list.append(input_list[i-1] + input_list[i])
        
        # Every other case:
        # Value will be the sum of previous, actual and next element.
        else:
            output_list.append(input_list[i-1] + input_list[i] + input_list[i+1])
    
    return output_list

# Example usage
example_list = [4, 0, 1, -2, 3]
print(solution(example_list))