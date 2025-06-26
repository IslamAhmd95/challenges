"""
Problem:
    Given a string s, return a new string that shows how many times each character appears, preserving the order of first appearance.
    This is a simplified version of run-length encoding, often asked in interviews like at Microsoft.
"""

from collections import Counter, OrderedDict



# Solution 1: collections.Counter (Python 3.7+)
"""
Notes:
- Uses Counter to count characters and relies on dict insertion order (Python 3.7+).
- This is very concise and efficient but not explicit.
- One pass internally
- Preserves order only from Python 3.7+
- Not reliable in older versions
"""
def encode_with_counter(s):
    """
    
    """
    counts = Counter(s)  # one-pass counter
    return ''.join(f"{count}{char}" for char, count in counts.items())


# Solution 2: OrderedDict (Any Python version)
"""
Notes:
- Uses OrderedDict to count characters and preserve insertion order.
- Works in all Python versions. Explicit and safe.
- Guarantees order preservation in any Python version
- Slightly slower due to extra overhead
- Very readable and safe for compatibility
"""
def encode_with_ordereddict(s):
    counts = OrderedDict()
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    return ''.join(f"{count}{char}" for char, count in counts.items())


# Manual Dict + List (Optimal for Interviews)
"""
Notes:
- Manually tracks character count and order of appearance using a dict and a list.
- This is the most efficient method for very large strings.
- Only 1 pass through the string
- Full control and always preserves order
- Best performance in interviews and large-scale input
"""
def encode_with_manual_tracking(s):
    
    seen = {}
    order = []

    for char in s:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1
            order.append(char)

    return ''.join(f"{seen[char]}{char}" for char in order)



s = 'AAAAAAAbbCCCCCDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDE'

print(encode_with_counter(s))
print(encode_with_ordereddict(s))
print(encode_with_manual_tracking(s))
