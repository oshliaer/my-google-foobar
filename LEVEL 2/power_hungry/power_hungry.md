## Power Hungry
https://spacepenguin.tech/google-foo-bar-challenge-level-2-power-hungry/

<details>
  <summary>solution.py</summary>
  
  ```python
class SetsPanels:
    def isOdd(self, number):
        return number % 2 != 0

    def sorting(self, arr):
        return sorted(arr, key=abs, reverse=True)

    def isSubzero(self):
        return len(self.subsets) == 1 and self.subsets[0] < 0

    def getMaximumProduct(self):
        if self.isSubzero():
            return str(self.subsets[0])

        maxProduct = 1
        valid = 0
        negatives = []
        subsets = self.sorting(self.subsets)

        for sub in subsets:
            if sub < 0:
                negatives.append(sub)
            elif sub > 0:
                valid = 1
                maxProduct *= sub
        if len(negatives) > 1:
            if self.isOdd(len(negatives)):
                negatives = negatives[:-1]
            for sub in negatives:
                maxProduct *= sub
        return str(maxProduct * valid)

    def __init__(self, subsets):
        self.subsets = subsets


def caller(xs):
    return SetsPanels(xs).getMaximumProduct()
```

</details>
