def length_of_last_word(word):
  ''' Returns the length of the last word in a string '''
  # remove any trailing space and split 
  words = word.strip().split()
  # return the length of the last word 
  return len(words[-1] if words else 0)
 
