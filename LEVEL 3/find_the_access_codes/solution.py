def answer(l):
  # Counter of triples
  c = 0

  # Count of numbers
  n = len(l)

  # The dictionary of indexes.
  pairs = {}

  # Loop down of each number expect last one
  for i in xrange(n - 2, -1, -1):
    # Loop down of each number until the index is greater than the current
    for j in xrange(n - 1, i, -1):
      # Is lucky?
      if l[j] % l[i] == 0:
        # If the number is divided by any previous one, then its index increases the weight by 1.
        pairs[i] = pairs.get(i, 0) + 1
        # The current left side there; check counts of the right sides
        if j in pairs:
          c += pairs.get(j, 0)
  
  return c
