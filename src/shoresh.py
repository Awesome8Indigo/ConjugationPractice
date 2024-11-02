import json


class Shoresh:

    def __init__(self, letters, meaning):
        self.letters = letters
        self.meaning = meaning

    def search(self) -> bool:
        # Open the JSON file and check if the shoresh with the given letters exists
        with open("conjugations.json", "rt") as jsonfile:
            jsonlst = json.load(jsonfile)
        shrshlst = jsonlst.get("Shoresh", [])

        # Check if any shoresh has matching letters
        return any(self.letters == shrsh_info["Letters"] for shrsh_info in shrshlst)

    def addShoresh(self):
        # Open the JSON file once and store data in jsonlst
        with open("conjugations.json", "rt") as jsonfile:
            jsonlst = json.load(jsonfile)

        shrshlst = jsonlst.get("Shoresh", [])

        # Only add if shoresh does not already exist
        if not self.search():
            newshrsh = {
                "Letters": self.letters,
                "Meaning": self.meaning
            }
            shrshlst.append(newshrsh)
            jsonlst["Shoresh"] = shrshlst

            # Write the updated list back to the file
            with open("conjugations.json", "wt") as jsonfile:
                json.dump(jsonlst, jsonfile, indent=4)

    def searchBinyan(self, binyan) -> bool:
        # Open the JSON file and load data
        with open("src/conjugations.json", "rt") as jsonfile:
            jsonlst = json.load(jsonfile)
        shrshlst = jsonlst.get("Shoresh", [])

        # Find the shoresh that matches self.letters, or None if not found
        verbshrsh = next((shrsh_info for shrsh_info in shrshlst if self.letters == shrsh_info["Letters"]), None)

        # If a matching shoresh was found, check if the binyan exists
        if verbshrsh and any(b in verbshrsh and binyan == b for b in
                             ["Pa'al", "Niphal", "Piel", "Pual", "Hifil", "Hufal", "Hitpa'el"]):
            return True

        return False

    def addBinyan(self, binyan):
        pass