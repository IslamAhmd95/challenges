"""
Problem:
    Implement a rate_limiter(limit) function that returns another function.
    The returned function accepts a user_id and tracks how many times that user has called it.
    If the number exceeds the given limit, it prints a warning message.
    Use closure and nonlocal to preserve user states across calls.
"""

def rate_limiter(limit):
    users = {
        1: 'Alice',
        2: 'bob',
        3: 'john'
    }
    
    users_counts = {}

    def count_login(user_id):

        if user_id not in users:
            return "Unknown user"
        
        nonlocal users_counts

        if users_counts.get(user_id, 0) >= limit:

            return f"Limit exceeded for {users[user_id]}"
        
        users_counts[user_id] = users_counts.get(user_id, 0) + 1

        return f"Access granted to {users[user_id]}"
    
    return count_login

limiter = rate_limiter(3)
print(limiter(1))
print(limiter(1))
print(limiter(2))
print(limiter(1))
print(limiter(3))
print(limiter(1))
print(limiter(2))
print(limiter(1))
print(limiter(3))
print(limiter(2))
print(limiter(1))
print(limiter(2))