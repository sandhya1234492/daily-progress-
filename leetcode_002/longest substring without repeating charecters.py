class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Remember the most recent index of each character we've seen.
        char_index = {}

        # The current substring (window) starts at left.
        left = 0

        # Keep the largest window length found so far.
        longest = 0

        # Move the right edge of the window through the string.
        for right in range(len(s)):
            char = s[right]

            # If this character repeats inside the current window,
            # move the left edge just past its previous occurrence.
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            # Record this character's latest position.
            char_index[char] = right

            # Both ends are included, so the current window length is
            # right - left + 1.
            longest = max(longest, right - left + 1)

        # Return the longest length; this is 0 for an empty string.
        return longest