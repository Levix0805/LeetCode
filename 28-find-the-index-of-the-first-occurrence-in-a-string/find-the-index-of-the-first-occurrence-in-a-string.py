class Solution(object):
    def strStr(self, haystack, needle):
        self.haystack = haystack
        self.needle = needle

        if needle in haystack:
            return haystack.index(needle)
        return -1
