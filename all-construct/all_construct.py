def all_construct(target_word, word_bank):
  if target_word == "":
        return [[]] 
    
  result = []
    
  for word in word_bank:
    if target_word.startswith(word):
      suffix = target_word[len(word):]  
      suffix_ways = all_construct(suffix, word_bank)  
      
      target_ways = [[word] + way for way in suffix_ways]
      result.extend(target_ways)

    return result



  return target_word
