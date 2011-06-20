class Team:
    def __init__(self):
        """ Asks for the user input for a noun and stores the noun in
        the instance variable self.word.  Remember a noun is a person,
        place, or thing. """
	self.word = raw_input("Please enter a noun: ")
        # TODO by person 3

    def reverse_input(self):
        """ Changes self.word to its reverse.  For example if
        self.word is 'apples', then it becomes 'selppa'."""
        self.word=word
	self.noun = self.word[::-1]
	return self.noun
        # TODO by person 1
    
    def print_in_sentence(self):
        """ Insert self.word in the sentence 'Today I dreamt of
        <self.word> while walking on the beach.' replacing <self.word>
        for the noun that was chosen during class construction. """
        print "Today I dreamt of "+self.word+" while walking on the beach "
	  # TODO by person 2

t = Team()
t.reverse_input()
t.print_in_sentence()
