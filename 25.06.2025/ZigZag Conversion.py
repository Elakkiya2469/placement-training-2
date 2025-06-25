class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        group = 2 * numRows - 2
        ans = []
        for i in range(1, numRows + 1):
            interval = group if i == numRows else 2 * numRows - 2 * i
            idx = i - 1
            while idx < len(s):
                ans.append(s[idx])
                idx += interval
                interval = group - interval
                if interval == 0:
                    interval = group
        return ''.join(ans)
      

class Solution(object):
  def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows <= 1:
      return s
    n = len(s)
    ans = []
    step = 2 * numRows - 2
    for i in range(numRows):
      one = i
      two = -i
      while one < n or two < n:
        if 0 <= two < n and one != two and i != numRows - 1:
          ans.append(s[two])
        if one < n:
          ans.append(s[one])
        one += step
        two += step
    return "".join(ans)
