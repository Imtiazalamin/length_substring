class Solution(object): # object class nilam
    def lengthOfLongestSubstring(self, s): # class er modde function toiri korlsm
        char_set = set() # faka set ja nitei hobe
        max_len = 0 # window start korlam jekhane unique r none unique process hobe er por ja baki thakbe ta end thakbe
        result = 0 # akhane start window theke slice ho a asha value thakbe

        for i in range(len(s)): # ai line a s er value gulor index ber kora holo
            while s[i] in char_set: # index value gulo char_set a ache ki na jotokhon thakbe totkhon colbe
                char_set.remove(s[max_len]) # char_set theke max_len a jabe r none unique remove hobe
                max_len += 1 # akhane remove hoar por max_len tehe result window te diya dibe
            char_set.add(s[i]) # akhane jokhon value r index na thake tokhon ai line a joge korbo ja result er modde ache
            result = max(result, i - max_len + 1)
        return result

soul = Solution()
s = "abcabcbb"
print(soul.lengthOfLongestSubstring(s))

# Example 2

class Solution(object): # object class nilam
    def lengthOfLongestSubstring(self, s): # class er modde function toiri korlsm
        blank_set = set() # faka set ja nitei hobe
        for_processing = 0 # window start korlam jekhane unique r none unique process hobe er por ja baki thakbe ta end thakbe
        end_processing = 0 # akhane start window theke slice ho a asha value thakbe

        for v_index in range(len(s)): # ai line a s er value gulor index ber kora holo
            while s[v_index] in blank_set: # index value gulo char_set a ache ki na jotokhon thakbe totkhon colte thakbe
                blank_set.remove(s[for_processing])
                for_processing += 1 # for_processing theke 1 r 1 kore end_p dukbe
            blank_set.add(s[v_index])

            end_processing = max(end_processing, v_index - for_processing + 1)

        return end_processing






soul = Solution()
s = "bbbbb"
print(soul.lengthOfLongestSubstring(s))

# 3
class Solution(object): # object class nilam
    def lengthOfLongestSubstring(self, s): # class er modde function toiri korlsm
        blank_set = set() # faka set ja nitei hobe
        for_processing = 0 # window start korlam jekhane unique r none unique process hobe er por ja baki thakbe ta end thakbe
        end_processing = 0 # akhane start window theke slice ho a asha value thakbe

        for v_index in range(len(s)): # ai line a s er value gulor index ber kora holo
            while s[v_index] in blank_set: # index value gulo char_set a ache ki na jotokhon thakbe totkhon colte thakbe
                blank_set.remove(s[for_processing])
                for_processing += 1 # for_processing theke 1 r 1 kore end_p dukbe
            blank_set.add(s[v_index])

            end_processing = max(end_processing, v_index - for_processing + 1)

        return end_processing






soul = Solution()
s = "pwwkew"
print(soul.lengthOfLongestSubstring(s))

