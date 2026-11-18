# Advent of Code 2016, Day 9: Explosives in Cyberspace
from aocd import get_data

# The puzzle says whitespace is ignored, so remove it everywhere.
data = ''.join(get_data(day=9, year=2016).split())

def decompressed_length(s, recursive=False):
    """Length of s after decompression, without building the text."""
    length = 0
    i = 0
    while i < len(s):
        start = s.find('(', i)
        if start == -1:                  # No markers left: the rest is plain text
            return length + len(s) - i
        length += start - i              # Plain text before this marker

        # Marker like (10x2): take the next 10 characters, repeat twice
        end = s.index(')', start)
        take, times = map(int, s[start + 1:end].split('x'))
        chunk = s[end + 1:end + 1 + take]

        # Part 2: markers inside the chunk expand too, so measure it recursively
        inner = decompressed_length(chunk, recursive=True) if recursive else len(chunk)
        length += inner * times

        i = end + 1 + take               # Skip past the marker and its chunk
    return length

print(f"Part 1: {decompressed_length(data)}")
print(f"Part 2: {decompressed_length(data, recursive=True)}")
