def best_sum(target_sum, numbers, memo = {}):
  ''' Returns the shortest array of elements that add upto the target sum '''
  
  def best_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}
  
    if target == 0:
        return []
  
    if target in memo:
        return memo[target]
    
    best_combination = None
    
    for num in numbers:
        if num <= target:
            remainder = target - num
            remainder_combination = best_sum(remainder, numbers, memo)
        
            if remainder_combination is not None:
                combination = remainder_combination + [num]
                
              
                if best_combination is None or len(combination) < len(best_combination):
                    best_combination = combination
    memo[target] = best_combination
    return best_combination