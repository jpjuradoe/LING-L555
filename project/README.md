# LING-L555: Part-of-speech tagging in Python3

`JESSICA P. JURADO Eraso`

`Indiana University`

## Project description

The aim of part-of-speech tagging is to label (or tag) each word in a corpus with the correct part of speech to indicate their grammatical behavior. According to Martinez (2012), tagging is one of the earliest steps in many natural language processes (NLPs)” (p.107).  To be able to run the code for this project, which labels words in sentences within a corpus, other codes were previously implemented. The first step was to take texts from a corpus and output each sentence in a new line. This code was the `segmenter.py`. Taking the output from the `segmenter.py`, each word was tokenized, using the `tokenizer.py`, which follows a format similar to [CoNLL-U](https://universaldependencies.org/format.html#words-tokens-and-empty-nodes). The next code used was the `train.py` that outputs word frequency and the frequency of the part-of-speech tag. The output of the `train.py` serves the labeling of the words in the corpus.

The first for loop of the `tagger.py` reads the output from the `train.py` and prints the output taken to the second for loop.  For this,  *= count* instead of *+= 1* was used in the last *if* condition to get the right frequency number to extract the most frequent tag per word. Using *+= 1* would have changed the count and would have not printed the same values from the output of the `train.py`

```ruby
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

```
Although the `tagger.py` helps label the tokens in a corpus, there is not complete accuracy. There are two major problems related to tagging accuracy, words that are used in different contexts (ambiguous words) and words that have not been previously tagged, (unknown words) (Marshall, 1983; Martinez, 2012). For tokens that were already labeled, the most frequent tag per word will be used without considering the ambiguity. For new tokens, the most frequent tag in general will be used to label them.

```ruby
# create the dictionaries for the most frequent tag per word
most_freq_pw = {}

# extract the most frequent tag per word
for form, t in word_tag_frequency.items():
        m = max(t, key=t.get)
        most_freq_pw[form] = m

# extract the most frequent tag in general
most_freq_general = sorted(tag_frequency.items(), key=lambda x: x[1], reverse=True)

```
Because the most frequent tag per word is *PUNCTUATION*, the next for loop will help tag new words with a content word tag avoiding the use of a function word tag.

```ruby
for tag, t in most_freq_general:
        if tag in ['ADJ', 'ADV', 'NOUN', 'VERB']:
                second_most_freq_tag = tag
                break

```

The last for loop prints the output in the [CoNLL-U](https://universaldependencies.org/format.html#words-tokens-and-empty-nodes) format used in the `tokeniser.py`. 

```ruby
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
Running all the codes together we get the following output:
> cat practice.txt | python3 segmenter.py | python3 tokeniser.py | python3 transcriber.py | python3 tagger.py

```ruby
# sent_id = 1
# text = El españöl andino: nariñénsë-pastuso(Înga), perüano, boliviano, y eK'uatoriano.

1        El     _       DET     _       _       _       _       _       IPA= el
2        españöl        _       NOUN    _       _       _       _       _       IPA= espaɲol
3        andino         _       NOUN    _       _       _       _       _       IPA= andino
4        :      _       PUNCT   _       _       _       _       _       IPA= :
5        nariñénsë      _       ADJ     _       _       _       _       _       IPA= naɾiɲense
6        -      _       PUNCT   _       _       _       _       _       IPA= -
7        pastuso        _       ADJ     _       _       _       _       _       IPA= pastuso
8        (      _       PUNCT   _       _       _       _       _       IPA= (
9        Înga   _       NOUN    _       _       _       _       _       IPA= Îŋga
10       )      _       PUNCT   _       _       _       _       _       IPA= )
11       ,      _       PUNCT   _       _       _       _       _       IPA= ,
12       perüano        _       ADJ     _       _       _       _       _       IPA= peɾuano
13       ,      _       PUNCT   _       _       _       _       _       IPA= ,
14       boliviano      _       ADJ     _       _       _       _       _       IPA= boliβiano
15       ,      _       PUNCT   _       _       _       _       _       IPA= ,
16       y      _       CONJ    _       _       _       _       _       IPA=i
17       eK'uatoriano   _       ADJ     _       _       _       _       _       IPA= eK'watoɾiano
18       .      _       PUNCT   _       _       _       _       _       IPA= .

# sent_id = 2
# text = "Solamente en suramerica".

1        "      _       PUNCT   _       _       _       _       _       IPA= "
2        Solamente      _       NOUN    _       _       _       _       _       IPA= solamente
3        en     _       PREP    _       _       _       _       _       IPA= en
4        suramerica     _       NOUN    _       _       _       _       _       IPA= suɾameɾika
5        "      _       PUNCT   _       _       _       _       _       IPA= "
6        .      _       PUNCT   _       _       _       _       _       IPA= .
...
```

## References

<a id="1">[1]</a> 
Marshall, I. (1983). 
Choice of Grammatical Word-Class without Global Syntactic Analysis: Tagging Words in the LOB Corpus.
Computers and the Humanities, 17(3), 139–150. http://www.jstor.org/stable/30204076

<a id="1">[1]</a> 
Martines, A. R. (2012).
Part-of-speech tagging.
WIREs Comp Stat, 4, 107-113. DOI: https://doi.org/10.1002/wics.195

<a id="1">[1]</a> 
Universal Dependencies project. (n.d.).
CoNLL-U Format.
Retrieved December 12, 2023, from https://universaldependencies.org/format.html#words-tokens-and-empty-nodes
