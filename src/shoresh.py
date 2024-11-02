import json


class Shoresh:

    def __init__(self, letters, meaning):
        self.letters = letters
        self.meaning = meaning

    def search(self) -> bool:
        # Open the JSON file and check if the shoresh with the given letters exists
        with open("conjugations.json", "rt", encoding = 'utf-8') as jsonfile:
            jsonlst = json.load(jsonfile)
        shrshlst = jsonlst.get("Shoresh", [])

        # Check if any shoresh has matching letters
        return any(self.letters == shrsh_info["Letters"] for shrsh_info in shrshlst)

    def addShoresh(self):
        # Open the JSON file once and store data in jsonlst
        with open("conjugations.json", "rt", encoding = 'utf-8') as jsonfile:
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
            with open("conjugations.json", "wt", encoding = 'utf-8') as jsonfile:
                json.dump(jsonlst, jsonfile, indent=4)

    def searchBinyan(self, binyan) -> bool:
        # Open the JSON file and load data
        with open("conjugations.json", "rt", encoding = 'utf-8') as jsonfile:
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

        # Open the JSON file once and store data in jsonlst
        with open("conjugations.json", "rt", encoding='utf-8') as jsonfile:
            jsonlst = json.load(jsonfile)
        shrshlst = jsonlst.get("Shoresh", [])

        # Find the shoresh that matches self.letters, or None if not found
        shrsh_info = next((shrsh_info for shrsh_info in shrshlst if self.letters == shrsh_info["Letters"]), None)

        if binyan not in ["Pa'al", "Niphal", "Piel", "Pual", "Hifil", "Hufal", "Hitpa'el"]:
            return

        # Only add if binyan does not already exist
        if not self.searchBinyan(binyan):
            #add basic details
            shrsh_info[binyan] = {
                "Infinitive": "",
                "Past": [],
                "Present": [],
                "Future": [],
                "Imperative": [],
                "Meaning": []
            }

            jsonlst["Shoresh"] = shrshlst

            # Write the updated list back to the file
            with open("conjugations.json", "wt", encoding='utf-8') as jsonfile:
                json.dump(jsonlst, jsonfile, ensure_ascii=False, indent=4)  # Write the updated JSON data

    def binyanInfo(self, binyan, infinitive, past, present, future, imperative, meaning):
        with open("conjugations.json", "rt", encoding='utf-8') as jsonfile:
            jsonlst = json.load(jsonfile)
        shrshlst = jsonlst.get("Shoresh", [])

        # Find the shoresh that matches self.letters, or None if not found
        shrsh_info = next((shrsh_info for shrsh_info in shrshlst if self.letters == shrsh_info["Letters"]), None)

        if not (isinstance(infinitive, str) or infinitive is None):
            print("infinitive is not a string")
            return
        if not (isinstance(past, list) or past is None):
            print("past is not a list")
            return
        if not (isinstance(present, list) or present is None):
            print("present is not a list")
            return
        if not (isinstance(future, list) or future is None):
            print("future is not a list")
            return
        if not (isinstance(imperative, list) or imperative is None):
            print("imperative is not a list")
            return
        if not (isinstance(meaning, list) or meaning is None):
            print("meaning is not a list")
            return
        
        # Only add if binyan already exists
        if self.searchBinyan(binyan):
            #add basic details
            shrsh_info[binyan] = {
                "Infinitive": infinitive,
                "Past": past,
                "Present": present,
                "Future": future,
                "Imperative": imperative,
                "Meaning": meaning
            }

            jsonlst["Shoresh"] = shrshlst

            # Write the updated list back to the file
            with open("conjugations.json", "wt", encoding='utf-8') as jsonfile:
                json.dump(jsonlst, jsonfile, ensure_ascii=False, indent=4)  # Write the u
        pass