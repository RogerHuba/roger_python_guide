from corpus_loader import word_list, name_list

sentences = [
    "A dark and stormy night",
    "j uehsf le a look jdheane iuwndlf",
    "where art thou dear brother",
]

for sentence in sentences:
    print(sentence)
    for word in sentence.split():
        print(word)
        if word in word_list:
            print("yep")
        else:
            print("nope")

