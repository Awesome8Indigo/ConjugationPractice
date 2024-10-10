import json
class shoresh:
  
  def __init__(self, letters, meaning):
    self.letters = letters
    self.meaning = meaning
    self.jsonfileWrite = open("src/conjugations.json", "wt")
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
      #create new dictionary based of self.
      newshrsh = {"Letters": self.letters, 
                  "Meaning": self.meaning}
      #take the shrshlst, and edit it. 
      length = len(self.shrshlst)
      self.shrshlst.append(newshrsh)
      #replace the old jsonlst["Shoresh"] with the new one
      self.jsonlst["Shoresh"] = self.shrshlst
      newjson = json.dumps(self.jsonlst)
