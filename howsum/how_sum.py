def how_sum(target_sum, numbers, memo=None):
    # Initialize the memo dictionary on the first call
    if memo is None:
        memo = {}
        
    # Base cases
    if target_sum in memo:  # Return memoized result if available
        return memo[target_sum]
    if target_sum == 0:  # Successful base case
        return []
    if target_sum < 0:  # Unsuccessful base case
        return None
    
    # Recursive case
    for num in numbers:
        remainder = target_sum - num
        result = how_sum(remainder, numbers, memo)  # Recursive call
        
        if result is not None:
            memo[target_sum] = result + [num]  # Store result in memo
            return memo[target_sum]
    
    memo[target_sum] = None  # Store failure in memo
    return None
