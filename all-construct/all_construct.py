def all_construct(target_word, word_bank):
  '''
    Returns an array containing all the ways that the `target` can be constructed
    by concatenating elements of the `word_bank` array
  '''
  if target_word == "":
    return [[]]
  all_ways = []

  for word in word_bank:
    if target_word.startswith(word):
      suffix = target_word[len(word):]
      suffix_ways = all_construct(suffix, word_bank)
      target_ways = [[word] + way for way in suffix_ways]
      all_ways.extend(target_ways)

  return all_ways
