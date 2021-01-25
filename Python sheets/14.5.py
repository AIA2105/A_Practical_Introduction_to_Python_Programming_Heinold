class Wordplay:
    def __init__(self, words=[]):
        self.words = words

    def words_with_length(self, length):
        my = []
        for word in self.words:
            if len(word) == length:
                if not my.__contains__(word):
                    my.append(word)
        return my

    def starts_with(self, s):
        my = []
        for word in self.words:
            if word[0] == s:
                if not my.__contains__(word):
                    my.append(word)
        return my

    def ends_with(self, s):
        my = []
        for word in self.words:
            if word[-1] == s:
                if not my.__contains__(word):
                    my.append(word)
        return my

    def palindromes(self):
        my = []
        for word in self.words:
            for i in range(int(len(word) / 2) + 1):
                if word[i] != word[-i - 1]:
                    break
                else:
                    if not my.__contains__(word):
                        my.append(word)

        return my

    def only(self, list=[]):
        my = []
        for word in self.words:
            for letter in list:
                if str(word).__contains__(letter):
                    if not my.__contains__(word):
                        my.append(word)
        return my

    def avoid(self, list=[]):
        my = self.words
        for word in self.only(list):
            my.remove(word)
        return my


a = Wordplay(['shohs', 'ali', 'samar', 'AIA', 'shosho'])
print(a.words_with_length(5))
print(a.starts_with('s'))
print(a.ends_with('i'))
print(a.palindromes())
print(a.only(['o', 's', 'm']))
print(a.avoid(['o', 's', 'm']))
