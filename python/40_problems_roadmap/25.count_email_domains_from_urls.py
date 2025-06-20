"""
Problem:
    Given a list of emails and a list of URLs, count how many emails belong to each domain extracted from the URLs. Domains are extracted from both URLs and emails, and only matching domains are counted.
"""

"""
Approach:

1. Check that both emails and urls lists are not empty. Raise an error if either is empty.

2. Remove duplicate URLs by converting the list to a set.

   Input: ['www.a.com', 'www.b.com', 'www.a.com']
   Output: {'www.a.com', 'www.b.com'}

3. Extract the domain part from each email (i.e., part after '@') and build a frequency Counter.

   Input: ['foo@a.com', 'bar@a.com', 'bar@b.com']
   Output: Counter({'a.com': 2, 'b.com': 1})

4. Initialize an empty dictionary to store counts for each valid domain found in the URLs.

5. Loop through each unique URL:
   - Split the URL by '.' to extract parts.
   - If the URL is valid (has at least 2 parts), construct the domain using the last two parts.
   - Use the domain as a key in the result dictionary.
   - Lookup the domain in the email Counter to get the count.

6. Print the final domain counts.
"""

from collections import Counter

emails = ['foo@a.com', 'bar@a.com', 'bar@b.com', 'qux@d.com', 'bla@m.com']
urls = ['www.a.com', 'www.b.com', 'www.a.com', 'www.d.com', 'www.c.com', 'invalid']

# Validate input
if not emails or not urls:
    raise ValueError("Emails list or URLs list can't be empty.")

# Remove duplicate URLs
urls_set = set(urls)

# Extract domains from emails and count them
email_domains = [email.split('@')[1] for email in emails]
email_domains_count = Counter(email_domains)

# Dictionary to store final domain counts
domain_count = {}

# Loop through each unique URL
for url in urls_set:

    # Split URL into parts
    url_parts = url.split('.')

    # Proceed only if it's a valid URL (e.g., 'www.a.com' -> 3 parts)
    if len(url_parts) >= 2:
        # Extract the domain as the last two parts (e.g., 'a.com')
        url_domain = url_parts[-2] + '.' + url_parts[-1]
    else:
        # Skip invalid URLs
        continue

    # Set count from email domain Counter (default 0 if not found)
    domain_count[url_domain] = email_domains_count.get(url_domain, 0)

# Output the result
print(domain_count)
