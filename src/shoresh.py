import json
class shoresh:
  def __init__(letters, meaning, *verbs):
    letters = letters
    verbs = verbs

  def search(self) -> bool:
    jsonfile = open("src/conjugations.json", "rt")
    jsontxt = jsonfile.read()
    jsonlst = json.loads(jsontxt)
    shrshlst = jsonlst["Shoresh"]
    for shrsh in shrshlst:
      if(shrsh["Letters"] == shoresh):
        return True
