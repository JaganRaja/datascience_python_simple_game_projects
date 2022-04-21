import os
import re
import string
import random
from graph import Graph, Vertex


def get_words_from_text(text_path):
    with open(text_path, 'rb') as file:
        text = file.read().decode("utf-8")

        # remove [verse 1: artist]
        # include the following line if you are doing song lyrics
        # text = re.sub(r'\[(.+)\]', ' ', text)

        # this is saying turn whitespace into just spaces
        text = ' '.join(text.split())
        text = text.lower()  # make everything lowercase to compare stuff
        # now we could be complex  and deal with punctuation.. but there are cases where
        # you might add a period such as (Mr. Brightside), but that's not really
        # punctuation.. so we just remove all the punctuation
        # hello! it's me. --> hello its me
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()  # splits on spaces again

    words = words[:1000]

    return words


def make_graph(words):
    g = Graph()
    prev_word = None
    # for each word
    for word in words:
        # check that word is in graph, and if not then add it
        word_vertex = g.get_vertex(word)

        # if there was a previous word, then add an edge if does not already exist in the graph,
        # if exists, increment weight by 1
        # set our word to the previous word and iterate!

        # now remember that we want to generate the probability mappings before composing
        # that is a great place to do it before we return the graph object
        if prev_word:  # prev word should be a Vertex
            # check if edge exists from previous word to current word
            prev_word.increment_edge(word_vertex)

        prev_word = word_vertex

    g.generate_probability_mappings()

    return g


def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))  # pick a random word to start!
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main():

    # what do we need to do here ?

    # step 1: get words from text
    # step 2: make graph using those words
    # step 3: get the next word for x number of words (defined by user)
    # step 4: show the user!
    words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    # for song lyrics
    # for song in os.listdir('songs/{}'.format(artist)):
    # if song == '.DS_Store':
    #     continue
    # words.extend(get_words_from_text('songs/{artist}/{song}'.format(artist=artist, song=song)))

    g = make_graph(words)
    composition = compose(g, words, 100)
    # returns a string, where all the words are seperated by a space!!
    return ' '.join(composition)


if __name__ == '__main__':
    print(main())
