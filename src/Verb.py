from src.shoresh import shoresh

class Verb:
    def __init__(self, Shoresh, Binyan, Spelling, ):
        self.shoresh = Shoresh
        self.binyan = Binyan
        self.spelling = Spelling
        if(self.shoresh.search() != True):
            self.shoresh.addShoresh()
        pass

    def AddVerb(self, shoresh, binyan, *tenses): 
        for tense in tenses:
            if searchVerb(shoresh, binyan, tense):
                pass
        #function to add new verb info
            pass


    def GetVerb():
        #function to find verb info
        pass

    def searchVerb(self, shoresh, binyan, tense):
        #function to look for verb.
        pass