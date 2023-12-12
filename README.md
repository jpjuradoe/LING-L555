# LING-L555: Part-of-speech tagging in Python3

`JESSICA P. JURADO E.`

`Indiana University`

The aim of part-of-speech tagging is to label (or tag) each word in a corpus with the correct part of speech to indicate their grammatical behavior. According to Martinez (2012), tagging is one of the earliest steps in many natural language processes (NLPs)” (p.107).  To be able to run the code for this project, which labels words in sentences within a corpus, other codes were previously implemented. The first step was to take texts from a corpus and output each sentence in a new line. This code was the `segmenter.py`. Taking the output from the `segmenter.py`, each word was tokenized following a format similar to CoNLL-U. The next code used was the `train.py` that outputs word frequency and the frequency of the part-of-speech tag. The output of the `train.py` serves the labeling of the words in the corpus.

```ruby
require 'model.tsv'
import sys
# create the dictionaries for tag frequency and word-tag frequency
tag_frequency = {}
word_tag_frequency = {}

# open the file containing the output from the train.py
for line in open('model.tsv').readlines():
        row = line.strip().split('\t')
        form = row[3].strip()
        tag = row[2].strip()
        count = row[1]
        if tag not in tag_frequency:
                tag_frequency[tag] = 0
        tag_frequency[tag] = tag_frequency[tag] + 1
        if form not in word_tag_frequency:
                word_tag_frequency[form] = {}
        if tag not in word_tag_frequency[form]:
                word_tag_frequency[form][tag] = count

# create the dictionaries for tag frequency and word-tag frequency
most_freq_pw = {}

for form, t in word_tag_frequency.items():
        m = max(t, key=t.get)
        most_freq_pw[form] = m

most_freq_general = sorted(tag_frequency.items(), key=lambda x: x[1], reverse=True)

for tag, t in most_freq_general:
        if tag in ['ADJ', 'ADV', 'NOUN', 'VERB']:
                second_most_freq_tag = tag
                break

for line in sys.stdin.readlines():
        line = line.strip('\n')
        if '\t' not in line:
                print(line)
        if '\t' in line:
                row = line.split('\t')

                form = row[1].strip()
                if form in most_freq_pw:
                        row[3] = most_freq_pw[form]
                else:
                        row[3] = second_most_freq_tag
                print('\t'.join(row))
```
## References
Universal Dependencies project. (n.d.). CoNLL-U Format. Retrieved December 12, 2023, from [https://universaldependencies.org/format.html#words-tokens-and-empty-nodes] 
Marshall, I. (1983). Choice of Grammatical Word-Class without Global Syntactic Analysis: Tagging Words in the LOB Corpus. Computers and the Humanities, 17(3), 139–150. http://www.jstor.org/stable/30204076
Martines, A. R. (2012). Part-of-speech tagging. WIREs Comp Stat, 4, 107-113. DOI: https://doi.org/10.1002/wics.195 
