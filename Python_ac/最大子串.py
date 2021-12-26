s = 'jdsljfsfjsjffj'
# 最大子串jfsfj，fjsjf

def getLongestPalindrome(A, n):
        maxLen=1
        if A==A[::-1]:return n
        for i in range(n):
            if i-maxLen>=1 and A[i-maxLen-1:i+1]==A[i-maxLen-1:i+1][::-1]:
                maxLen+=2
                continue
            if i-maxLen>=0 and A[i-maxLen:i+1]==A[i-maxLen:i+1][::-1]:
                maxLen+=1
        return maxLen

print(getLongestPalindrome(s, len(s)))