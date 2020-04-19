def substrings_in_set(s, words):
    if s in words:
        yield [s]
    for i in range(1, len(s)):
        if s[:i] not in words:
            continue
        for rest in substrings_in_set(s[i:], words):
            yield [s[:i]] + rest

# Assuming Linux. Word list may also be at /usr/dict/words. 
# If not on Linux, grab yourself an enlish word list and insert here:
words = set(x.strip().lower() for x in open("./words.txt").readlines())

# The above english dictionary for some reason lists all single letters as words.
# Remove all except "i" and "u" (remember a string is an iterable, which means
# that set("abc") == set(["a", "b", "c"])).
words -= set("bcdefghjklmnopqrstvwxyz")

# If there are more words we don't like, we remove them like this:
words -= set(("ex", "rs", "ra", "frobnicate"))

# We may also add words that we do want to recognize. Now the domain name
# slartibartfast4ever.co.uk will be properly counted, for instance.
words |= set(("4", "2", "slartibartfast")) 

count = {}
no_match = []
domains = ["examplecartrading.com", "examplepensions.co.uk", 
    "exampledeals.org", "examplesummeroffers.com"]

# Assume domains is the list of domain names ["examplecartrading.com", ...]
for domain in domains:
    # Extract the part in front of the first ".", and make it lower case
    name = domain.partition(".")[0].lower()
    found = set()
    for split in substrings_in_set(name, words):
        found |= set(split)
    for word in found:
        count[word] = count.get(word, 0) + 1
    if not found:
        no_match.append(name)

print(count)
print("No match found for:", no_match)