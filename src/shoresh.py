import json
class shoresh:
  def __init__(self, letters, meaning, *verbs):
    self.letters = letters
    self.verbs = verbs

  def search(self) -> bool:
    jsonfile = open("src/conjugations.json", "rt")
    jsontxt = jsonfile.read()
    jsonlst = json.loads(jsontxt)
    shrshlst = jsonlst["Shoresh"]
    #add a for loop to count for every shoresh in shrshlst
    Letters = shrshlst[0]["Letters"]
    if(self.letters == Letters):
      return True
