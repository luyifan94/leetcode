#1. Two Sum
class Solution:
    def twoSum(self, nums, target):
        num_hash = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in num_hash:
                return [num_hash[diff],i]
            num_hash[nums[i]] = i

#2. Add Two Numbers
class Solution:
    def addTwoNumbers(self, l1, l2):
        res = ListNode(-1)
        node = res
        carry = 0
        while l1 or l2 or carry:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            node.next = ListNode(val)
            node = node.next
        return res.next

#3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s):
        s_hash = {}
        res = 0
        head = 0
        for i in range(len(s)):
            if s[i] in s_hash and s_hash[s[i]] >= head:
                head = s_hash[s[i]] + 1
            else:
                res = max(res, i - head + 1)
            s_hash[s[i]] = i
        return res

#4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        k = (m+n-1)//2
        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi)//2
            if a[mid] > b[k-mid-1]:
                hi = mid
            else:
                lo = mid + 1
        i = lo
        rest = sorted(a[i:i+2] + b[k-i:k-i+2])
        return (rest[0]+rest[1-(m+n)%2])/2.0

#5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s):

        s = '#' + '#'.join(s) + '#'
        lens = len(s)
        p = []
        idx = 0
        mx = 0
        for i in range(lens):
            if mx > i:
                r = min(p[2 * idx - i], mx - i)  # 当i处在mx的范围内，有两个下限值，一个是关于idx对称的值和超过边界的值
            else:
                r = 1
            while i - r >= 0 and i + r < lens and s[i - r] == s[i + r]:
                r += 1
            p.append(r - 1)
            if (i + p[i]) > mx:
                mx, idx = i + p[i], i

        maxr = max(p)
        maxi = p.index(maxr)
        res = s[maxi - maxr:maxi + maxr + 1].split('#')
        res = res[1:-1]
        return ''.join(res)

#6. ZigZag Conversion
class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        res = ['']*numRows

        index,step = 0,1
        for x in s:
            res[index] += x
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step
        return ''.join(res)

