"""Lexicon and sentence templates for Elman (1990) experiment 4 ("Simple Sentences").

Table 3 lists 12 categories (the text says "thirteen") with two example words each;
the remaining members are taken from the 29 leaves of Figure 7. Table 3's
"cookie, break" under NOUN-FOOD is a typo for "bread". Table 4 has 16 rows
(the text says 15). Uniform sampling over templates and words gives ~27,500
words per 10,000 sentences, consistent with the paper's 27,534.
"""

LEXICON = {
    "NOUN-HUM":     ["man", "woman", "boy", "girl"],
    "NOUN-ANIM":    ["cat", "dog", "mouse"],
    "NOUN-INANIM":  ["book", "rock", "car"],
    "NOUN-AGRESS":  ["dragon", "monster", "lion"],
    "NOUN-FRAG":    ["glass", "plate"],
    "NOUN-FOOD":    ["cookie", "bread", "sandwich"],
    "VERB-INTRAN":  ["think", "sleep", "exist"],
    "VERB-TRAN":    ["see", "chase", "like"],
    "VERB-AGPAT":   ["move", "break"],
    "VERB-PERCEPT": ["smell", "see"],
    "VERB-DESTROY": ["break", "smash"],
    "VERB-EAT":     ["eat"],
}

# Table 4, verbatim: 12 three-word + 4 two-word frames.
TEMPLATES = [
    ("NOUN-HUM",    "VERB-EAT",     "NOUN-FOOD"),
    ("NOUN-HUM",    "VERB-PERCEPT", "NOUN-INANIM"),
    ("NOUN-HUM",    "VERB-DESTROY", "NOUN-FRAG"),
    ("NOUN-HUM",    "VERB-INTRAN"),
    ("NOUN-HUM",    "VERB-TRAN",    "NOUN-HUM"),
    ("NOUN-HUM",    "VERB-AGPAT",   "NOUN-INANIM"),
    ("NOUN-HUM",    "VERB-AGPAT"),
    ("NOUN-ANIM",   "VERB-EAT",     "NOUN-FOOD"),
    ("NOUN-ANIM",   "VERB-TRAN",    "NOUN-ANIM"),
    ("NOUN-ANIM",   "VERB-AGPAT",   "NOUN-INANIM"),
    ("NOUN-ANIM",   "VERB-AGPAT"),
    ("NOUN-INANIM", "VERB-AGPAT"),
    ("NOUN-AGRESS", "VERB-DESTROY", "NOUN-FRAG"),
    ("NOUN-AGRESS", "VERB-EAT",     "NOUN-HUM"),
    ("NOUN-AGRESS", "VERB-EAT",     "NOUN-ANIM"),
    ("NOUN-AGRESS", "VERB-EAT",     "NOUN-FOOD"),
]

WORDS = sorted({w for ws in LEXICON.values() for w in ws})   # 29 unique words
N_BITS = 31                                                 # 29 + 2 spare bits (for "zog")
