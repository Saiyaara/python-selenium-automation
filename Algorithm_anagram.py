def anagram_text(t1, t2):

  if len(t1)!= 0:
    return False

  count = {}
  for letter in t1:
    if letter in count:
     count[letter] += 1

    else:
     count[letter] = 1

    for letter in t2:
      if letter in count:
        count[letter] -=1
      else:
        count[letter] =1

    for i in count:

     if count[i]!= 0:

        return False

    return True

t1 = "abcdde"
t2 = "abcdee"

print(anagram_text(t1, t2))





