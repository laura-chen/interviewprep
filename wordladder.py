from collections import deque
def ClassName(Word):
    def __init__(self, string):
        self.val = string
        self.neighbors = []
        self.prev = None

def word_ladder(begin_word, end_word, word_list):
    """ Main function."""

def node_neighbors(string, word_list):
    """ Creates Word object and assigns words that are "one away" to be neighbors
    of the word. Returns the Word object. """
    word_node = Word(string)
    for word in word_list:
        if one_away(string, )


def one_away(str1, str2):
    """ Determines whether two words are one letter away from one another and
    equal length. """
    if len(str1) != len(str2):
        return False
    mismatches = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            mismatches += 1
    if mismatches == 1:
        return True
    return False

def wordBFS(begin_word, end_word):
    """ Stores the shortest path to the end word and returns the node associated
    with the end word. """
    queue = deque(Word(begin_word))
    while queue != []:
        current = queue.pop()
        for neighbor in current.neighbors:
            neighbor.prev = current
            if neighbor.val = end_word:
                return neighbor
            queue.append(neighbor)
    return None
