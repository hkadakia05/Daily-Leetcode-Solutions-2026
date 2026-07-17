class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))
        #The solution is simple return the set of s because a set is only continiing the unique characters whoich is all you need for the function and then len just returns the unique characters amount whch is what the function and solution is asking for.