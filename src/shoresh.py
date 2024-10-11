import json
class shoresh:
  
  def __init__(self, letters, meaning):
    self.letters = letters
    self.meaning = meaning
    
  def search(self) -> bool:
    jsonfile = open("src/conjugations.json", "rt")
    jsontxt = jsonfile.read()
    jsonlst = json.loads(jsontxt)
    shrshlst = jsonlst["Shoresh"]
    x = 0
    # counts # of shoresh
    for shrsh in shrshlst:
      Letters = shrshlst[x]["Letters"]
      if(self.letters == Letters):
        return True
      x += 1

  
  def addShoresh(self):
    # Open the file in read mode, process it, and then close it automatically.
    with open("src/conjugations.json", "rt") as jsonfile:
        jsonlst = json.load(jsonfile)  # Using json.load instead of read() and then loads()
    
    shrshlst = jsonlst.get("Shoresh", [])
    
    # Check if there is a search value using self.search()
    if self.search():
        return
    
    # Create new dictionary based on self
    newshrsh = {
        "Letters": self.letters, 
        "Meaning": self.meaning
    }
    
    # Append the new shoresh to the list
    shrshlst.append(newshrsh)
    
    # Replace the old jsonlst["Shoresh"] with the new list
    jsonlst["Shoresh"] = shrshlst
    
    # Open the file in write mode to update it
    with open("src/conjugations.json", "wt") as jsonfile:
        newjson = json.dumps(jsonlst, indent=4)  # Format the json nicely
        jsonfile.write(newjson)