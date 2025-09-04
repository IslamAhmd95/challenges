"""
Problem:
    A Python program to find the common elements (intersection) between two lists.
"""

list1 = [5, 1, 2, 3, 4, 5, 5]
list2 = [4, 5, 6, 7, 8, 4, 5]

# first solution
common_items = list(set(list1) & set(list2))
print(common_items)


# second solution
common_items = []
set_list2 = set(list2)
seen = set()

for item in list1:
    if item in set_list2 and item not in seen:
        common_items.append(item)
        seen.add(item)

print(common_items)



"""
Notes:
    Membership check means: testing if an element exists in a collection, e.g., item in collection.

        1. List membership check (item in list)
            - Lists store elements in a sequential order.
            - Python checks membership by scanning each element one by one until it finds the target or reaches the end.
            - Time complexity: O(n), where n = length of the list.
            - This means the time to check membership grows linearly with the size of the list.
            - Example: In a list of 1,000 items, worst case 1,000 comparisons are needed.

        2. Set membership check (item in set)
            - Sets use a hash table data structure internally.
            - When checking membership, Python:
            - Computes the hash of the item.
            - Uses this hash to directly find the position in memory where the item would be stored.
            - Time complexity: O(1) — constant time.
            - This means the time to check membership does not increase with the size of the set.
            - Example: In a set of 1,000,000 items, the lookup still takes roughly the same time as in a set of 10 items.

        3. Practical recommendation
            - When performing many membership checks or handling large collections, prefer sets over lists.
            - Using sets will improve performance and efficiency significantly.
            - If order matters and you want to preserve it while having fast membership checks, consider using OrderedDict keys (Python 3.6+) or collections.OrderedDict (before 3.6), or a custom solution.
"""

print('-------------------------------------------------------------------------')

"""
If you want both:
    Fast membership checks like set (O(1) time),
    Order preservation like list (elements stay in original order),
➡️ Use: collections.OrderedDict.fromkeys(iterable)
Why?
    - set removes duplicates and gives fast membership checks, but doesn’t reliably preserve order (especially in older Python versions).
    - list preserves order, but checking membership (x in list) is O(n) and duplicates aren’t automatically removed.
    - OrderedDict (or regular dict in Python 3.7+) preserves order and gives O(1) membership checks on keys.
"""

from collections import OrderedDict

data = [6, 2, 5, 6, 8, 9, 3, 2, 1]

# removes duplicates and preserves order
# result = list(OrderedDict.fromkeys(data))
result = list(dict.fromkeys(data))
print(result)