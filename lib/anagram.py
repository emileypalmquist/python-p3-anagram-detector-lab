class Anagram:
    def __init__(self, word=""):
        self.word = word

    def match(self, words_list):
        matches = []

        for word in words_list:
            sorted_word = sorted([letter for letter in word])
            sorted_init_word = sorted([word for word in self.word])
            if sorted_word == sorted_init_word:
                matches.append(word)

        return matches
