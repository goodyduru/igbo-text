## What Is Igbo Text

Igbo Text is a library for tokenizing and normalizing texts mainly written in the Igbo Language.

## Installation

```
$ pip install igbo-text
```

## Examples

### Normalization

```
from igbo-text import IgboText

# Create IgboText class instance
igbo_text = IgboText()

# normalize text 
text = "Ọ nà-ezò nnukwu mmīri n'iro?"
normalized_text = igbo_text.normalize(text, convert_to_lower=True, remove_abbreviations=True)
print(normalized_text)
```

When the code above is executed, the output will be  

ọ na ezo nnukwu mmiri n iro

Upper case characters can be left alone by setting convert_to_lower=False

Abbreviations can be left alone by setting remove_abbreviations=True

### Tokenization

```
from igbo-text import IgboText

# Create IgboText class instance
igbo_text = IgboText()

# tokenize text
text = "Ndị Fàda kwènyèrè n'atọ̀ n'ime otù."
tokenized_text = igbo_text.tokenize(text)
print(tokenized_text)
```

When the code above isi executed, the output will be

["Ndị", "Fada", "kwenyere", "n'", "atọ", "n'", "ime", "otu", "."]

You can convert all upper case characters to lower case by setting convert_to_lower=True.