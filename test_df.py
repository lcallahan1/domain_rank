import pandas as pd
from pandas import DataFrame

import enchant
d = enchant.Dict("en_US")

def substrings_in_set(s):
    if d.check(s):
        yield [s]
    for i in range(1, len(s)):
        if not d.check(s[:i]):
            continue
        for rest in substrings_in_set(s[i:]):
            yield [s[:i]] + rest

def words_by_domain():
    words = {}
    no_match = []
    domains = ["examplecartrading.com", "examplepensions.co.uk", 
        "exampledeals.org", "examplesummeroffers.com"]

    # Assume domains is the list of domain names ["examplecartrading.com", ...]
    for domain in domains:
        words[domain] = []
        # Extract the part in front of the first ".", and make it lower case
        name = domain.partition(".")[0].lower()
        found = set()
        for split in substrings_in_set(name):
            found |= set(split)
        for word in found:   
            if len(word) >= 3:
                count[domain].append(word) # append each word in found if it matches the criteria
        if not found:
            no_match.append(name)

    return(words)



# # convert to dataframe for Dash table. 
# df_words = pd.DataFrame.from_dict(count, orient='index')

# df_words.to_csv (r'/Users/lissacallahan/Python/domain_names/words_dataframe.csv', header=True)


