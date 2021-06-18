# from typing import int


def lengthOfLongestSubstring(s: str) -> int:
    counter = 0
    st_index = 0
    ch_last_index = {}
    for index in range(0, len(s)):
        ch = s[index]

        if ch in ch_last_index:
            st_index = max(st_index, ch_last_index[ch]+1)


        counter = max(counter, index-st_index + 1)
        ch_last_index[ch] = index
    return counter


if __name__ == "__main__":
    print(lengthOfLongestSubstring("pwwkew"))
