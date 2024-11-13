def how_sum(target_sum, numbers, memo=None):
  
    # Recursive case
    for num in numbers:
        remainder = target_sum - num
        result = how_sum(remainder, numbers, memo)  # Recursive call
        
        if result is not None:
            memo[target_sum] = result + [num]  # Store result in memo
            return memo[target_sum]
    
    memo[target_sum] = None  # Store failure in memo
    return None
