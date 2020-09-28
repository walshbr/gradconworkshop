import spacy
import en_core_web_sm
import nltk

def spacy_pos_transform(text):
    """Given a string pasted in, take a poem and transform it into its POS tags"""
    nlp = en_core_web_sm.load()
    lines = text.split('\n')
    spacy_lines = []
    for line in lines:
        this_line = []
        doc = nlp(line)
        for token in doc:
            this_line.append(token.tag_) 
        spacy_lines.append(this_line)
    # reconstituting them now
    transformed_poem = []
    for line in spacy_lines:
        transformed_poem.append(' '.join(line))

    return transformed_poem

def nltk_pos_transform(text):
    """Given a string pasted in, take a poem and transform it into its POS tags"""
    lines = text.split('\n')
    tokenized_lines = []
    for line in lines:
        words = nltk.word_tokenize(line)
        tokenized_lines.append(words)
    tagged_lines = []
    for line in tokenized_lines:
        tagged_lines.append(nltk.pos_tag(line))
    just_tags_for_lines = []

    for line in tagged_lines:
        this_line = []
        for tag_pair in line:
            this_line.append(tag_pair[1])
        just_tags_for_lines.append(this_line)
    # reconstituting them now
    transformed_poem = []
    for line in just_tags_for_lines:
        transformed_poem.append(' '.join(line))
    return transformed_poem

def binary_poem(spacy_text, nltk_text):
    binary_poem = []
    line_counter = 0
    for line in spacy_text:
        this_line = []
        spacy_line = nltk.word_tokenize(line)
        nltk_line = nltk.word_tokenize(nltk_text[line_counter])
        for num, word in enumerate(spacy_line[:-1], start=0):
            try:
                if word == nltk_line[num]:
                    this_line.append(1)
                else:
                    this_line.append(0)
            except:
                pass
        binary_poem.append(this_line)
        line_counter += 1
    return binary_poem



our_text = """
Mother said to call her if the H-bomb exploded
And I said I would, and it about did
When Louis my brother robbed a service station
And lay cursing on the oily cement in handcuffs.

But by that time it was too late to tell Mother,
She was too sick to worry the life out of her
Over why why. Causation is sequence
And everything is one thing after another.

Besides, my other brother, Eddie, had got to be President,
And you can't ask too much of one family.
The chances were as good for a good future
As bad for a bad one.

Therefore it was surprising that, as we kept the newspapers from Mother,
She died feeling responsible for a disaster unverified,
Murmuring, in her sleep as it seemed, the ancient slogan
Noblesse oblige.
"""
spacy_text = spacy_pos_transform(our_text)
nltk_text = nltk_pos_transform(our_text)
binary_poem = binary_poem(spacy_text, nltk_text)

print('NLTK transform results:')
for line in nltk_text:
    print(line)
print('=========')
print('Spacy transform results:')
for line in spacy_text:
    print(line)
print('Comparison - zero is where they do not tag the same')
for line in binary_poem:
    line = [str(item) for item in line]
    print(' '.join(line))