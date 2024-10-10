import json
class shoresh:
  def __init__(self, letters, meaning, *verbs):
    self.letters = letters
    self.verbs = verbs
    self.jsonfile = open("src/conjugations.json", "rt")
    self.jsontxt = self.jsonfile.read()
    self.jsonlst = json.loads(self.jsontxt)
    self.shrshlst = self.jsonlst["Shoresh"]
  def search(self) -> bool:
 
    x = 0
    # counts # of shoresh
    for shrsh in self.shrshlst:
      Letters = self.shrshlst[x]["Letters"]
      if(self.letters == Letters):
        return True
      x += 1
    
    def addShoresh(self):
      #using "search()" check if there is a search value.
      if(self.search()):
         return
      
    
