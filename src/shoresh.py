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
    def searchReturn(self):
        with open("conjugations.json", "rt", encoding='utf-8') as jsonfile:
            jsonlst = json.load(jsonfile)
        shrshlst = jsonlst.get("Shoresh", [])

        # Check if any shoresh has matching letters and return the corresponding dictionary
        return next((shrsh_info for shrsh_info in shrshlst if self.letters == shrsh_info["Letters"]), None)
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
        # Find the shoresh that matches self.letters, or None if not found
        verbshrsh = self.searchReturn()

        # If a matching shoresh was found, check if the binyan exists
        if verbshrsh and any(b in verbshrsh and binyan == b for b in
                             ["Pa'al", "Niphal", "Piel", "Pual", "Hifil", "Hufal", "Hitpa'el"]):
            return True

        return False
    def searchReturnBinyan(self, binyan):
        verbshrsh = self.searchReturn()
        return verbshrsh[binyan]
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

    def autoConjugatePaal(self, tense):
        letters = self.letters
        final_letter_map = {
            "כ": "ך",
            "נ": "ן",
            "פ": "ף",
            "צ": "ץ",
            "מ": "ם"
        }
        gutturals = ["א", "ע", "ה", "ח"]
        if tense is None:
            print("No tense to conjugate")
            return None
        if len(letters) >= 4 or len(letters) <= 2:
            print("irregular verb")
            return None

        if tense == "Present":
            if letters[2] in ["י", "ה"]:
                sm = [letters[0], "ו", letters[1], "ה"]
                sf = [letters[0], "ו", letters[1], "ה"]
                pm = [letters[0], "ו", letters[1], "י", "ם"]
                pf = [letters[0], "ו", letters[1], "ו", "ת"]

                # Convert lists to strings
                sm_str = "".join(sm)
                sf_str = "".join(sf)
                pm_str = "".join(pm)
                pf_str = "".join(pf)
            elif letters[1] in ["ו", "י"]:
                # Build the forms
                sm = [letters[0], final_letter_map.get(letters[2], letters[2])]  # single masc
                sf = [letters[0], letters[2], "ה"]  # single fem
                pm = [letters[0], letters[2], "י", "ם"]  # plural masc
                pf = [letters[0], letters[2], "ו", "ת"]  # plural fem

                # Convert lists to strings
                sm_str = "".join(sm)
                sf_str = "".join(sf)
                pm_str = "".join(pm)
                pf_str = "".join(pf)
            else:
                sm = [letters[0], "ו", letters[1], final_letter_map.get(letters[2], letters[2])]
                sf = [letters[0], "ו", letters[1], letters[2], "ת"]
                pm = [letters[0], "ו", letters[1], letters[2], "י", "ם"]
                pf = [letters[0], "ו", letters[1], letters[2], "ו", "ת"]

                # Convert lists to strings
                sm_str = "".join(sm)
                sf_str = "".join(sf)
                pm_str = "".join(pm)
                pf_str = "".join(pf)
            return [sm_str, sf_str, pm_str, pf_str]
        elif tense == "Past":
            if letters[2] in ["י", "ה"]:
                first = [
                    [letters[0], letters[1], letters[2], "ת", "י"],
                    [letters[0], letters[1], letters[2], "ת", "י"],
                    [letters[0], letters[1], letters[2], "נ", "ו"],
                    [letters[0], letters[1], letters[2], "נ", "ו"],
                ]
                second = [
                    [letters[0], letters[1], letters[2], "ת"],
                    [letters[0], letters[1], letters[2], "ת"],
                    [letters[0], letters[1], letters[2], "ת", "ם"],
                    [letters[0], letters[1], letters[2], "ת", "ן"],
                ]
                third = [
                    [letters[0], letters[1], "ה"],
                    [letters[0], letters[1], "ת", "ה"],
                    [letters[0], letters[1],  "ו"],
                    [letters[0], letters[1],  "ו"]
                ]

                first_str = ["".join(first[0]), "".join(first[1]), "".join(first[2]), "".join(first[3])]
                second_str = ["".join(second[0]), "".join(second[1]), "".join(second[2]), "".join(second[3])]
                third_str = ["".join(third[0]), "".join(third[1]), "".join(third[2]), "".join(third[3])]
            elif letters[1] in ["י", "ו"]:
                first = [
                    [letters[0], letters[2], "ת", "י"],
                    [letters[0], letters[2], "ת", "י"],
                    [letters[0], letters[2], "נ", "ו"],
                    [letters[0], letters[2], "נ", "ו"],
                ]
                second = [
                    [letters[0], letters[2], "ת"],
                    [letters[0], letters[2], "ת"],
                    [letters[0], letters[2], "ת", "ם"],
                    [letters[0], letters[2], "ת", "ן"],
                ]
                third = [
                    [letters[0], final_letter_map.get(letters[2], letters[2])],
                    [letters[0], letters[2], "ה"],
                    [letters[0], letters[2], "ו"],
                    [letters[0], letters[2], "ו"]
                ]

                first_str = ["".join(first[0]), "".join(first[1]), "".join(first[2]), "".join(first[3])]
                second_str = ["".join(second[0]), "".join(second[1]), "".join(second[2]), "".join(second[3])]
                third_str = ["".join(third[0]), "".join(third[1]), "".join(third[2]), "".join(third[3])]
            else:
                first = [
                    [letters[0], letters[1], letters[2], "ת", "י"],
                    [letters[0], letters[1], letters[2], "ת", "י"],
                    [letters[0], letters[1], letters[2], "נ", "ו"],
                    [letters[0], letters[1], letters[2], "נ", "ו"],
                ]
                second = [
                    [letters[0], letters[1], letters[2], "ת"],
                    [letters[0], letters[1], letters[2], "ת"],
                    [letters[0], letters[1], letters[2], "ת", "ם"],
                    [letters[0], letters[1], letters[2], "ת", "ן"],
                ]
                third = [
                    [letters[0], letters[1], letters[2]],
                    [letters[0], letters[1], letters[2], "ה"],
                    [letters[0], letters[1], letters[2], "ו"],
                    [letters[0], letters[1], letters[2], "ו"]
                ]

                first_str = ["".join(first[0]), "".join(first[1]), "".join(first[2]), "".join(first[3])]
                second_str = ["".join(second[0]), "".join(second[1]), "".join(second[2]), "".join(second[3])]
                third_str = ["".join(third[0]), "".join(third[1]), "".join(third[2]), "".join(third[3])]
            return [first_str, second_str, third_str]
        elif tense == "Future":

            if letters[0] == "י":


                exception = input("is the verb a) no root yod, \n"
                                  " b) full root yod, \n"
                                  " c) efol ")

                if exception == "a":
                    first = [
                        ["א", letters[1], letters[2]],  # ms
                        ["א", letters[1], letters[2]],
                        ["נ", letters[1], letters[2]],
                        ["נ", letters[1], letters[2]]
                    ]
                    second = [
                        ["ת", letters[1], letters[2]],
                        ["ת", letters[1], letters[2], "י"],
                        ["ת", letters[1], letters[2], "ו"],
                        ["ת", letters[1], letters[2], "ו"]
                    ]
                    third = [
                        ["י", letters[1], letters[2]],
                        ["ת", letters[1], letters[2]],
                        ["י", letters[1], letters[2], "ו"],
                        ["י", letters[1], letters[2], "ו"]
                    ]
                    first_str = ["".join(first[0]), "".join(first[1]), "".join(first[2]), "".join(first[3])]
                    second_str = ["".join(second[0]), "".join(second[1]), "".join(second[2]), "".join(second[3])]
                    third_str = ["".join(third[0]), "".join(third[1]), "".join(third[2]), "".join(third[3])]
                elif exception == "b":
                    first = [
                        ["א", letters[0], letters[1], letters[2]],  # ms
                        ["א", letters[0], letters[1], letters[2]],
                        ["נ", letters[0], letters[1], letters[2]],
                        ["נ", letters[0], letters[1], letters[2]]
                    ]
                    second = [
                        ["ת", letters[0], letters[1], letters[2]],
                        ["ת", letters[0], letters[1], letters[2], "י"],
                        ["ת", letters[0], letters[1], letters[2], "ו"],
                        ["ת", letters[0], letters[1], letters[2], "ו"]
                    ]
                    third = [
                        ["י", letters[0], letters[1], letters[2]],
                        ["ת", letters[0], letters[1], letters[2]],
                        ["י", letters[0], letters[1], letters[2], "ו"],
                        ["י", letters[0], letters[1], letters[2], "ו"]
                    ]
                    first_str = ["".join(first[0]), "".join(first[1]), "".join(first[2]), "".join(first[3])]
                    second_str = ["".join(second[0]), "".join(second[1]), "".join(second[2]), "".join(second[3])]
                    third_str = ["".join(third[0]), "".join(third[1]), "".join(third[2]), "".join(third[3])]
                elif exception == "c":
                    # efol rule:
                    first = [
                        ["א", letters[0], letters[1], "ו", letters[2]],  # ms
                        ["א", letters[0], letters[1], "ו", letters[2]],
                        ["נ", letters[0], letters[1], "ו", letters[2]],
                        ["נ", letters[0], letters[1], "ו", letters[2]]
                    ]
                    second = [
                        ["ת", letters[0], letters[1], "ו", letters[2]],
                        ["ת", letters[0], letters[1], letters[2], "י"],
                        ["ת", letters[0], letters[1], letters[2], "ו"],
                        ["ת", letters[0], letters[1], letters[2], "ו"]
                    ]
                    third = [
                        ["י", letters[0], letters[1], "ו", letters[2]],
                        ["ת", letters[0], letters[1], "ו", letters[2]],
                        ["י", letters[0], letters[1], letters[2], "ו"],
                        ["י", letters[0], letters[1], letters[2], "ו"]
                    ]
                    first_str = ["".join(first[0]), "".join(first[1]), "".join(first[2]), "".join(first[3])]
                    second_str = ["".join(second[0]), "".join(second[1]), "".join(second[2]), "".join(second[3])]
                    third_str = ["".join(third[0]), "".join(third[1]), "".join(third[2]), "".join(third[3])]
                else:
                    print("invalid input")
                    return

            elif letters[2] == "ה":
                first = [
                    ["א", letters[0], letters[1], letters[2]],  # ms
                    ["א", letters[0], letters[1], letters[2]],
                    ["נ", letters[0], letters[1], letters[2]],
                    ["נ", letters[0], letters[1], letters[2]]
                ]
                second = [
                    ["ת", letters[0], letters[1], letters[2]],
                    ["ת", letters[0], letters[1], letters[2], "י"],
                    ["ת", letters[0], letters[1], letters[2], "ו"],
                    ["ת", letters[0], letters[1], letters[2], "ו"]
                ]
                third = [
                    ["י", letters[0], letters[1], letters[2]],
                    ["ת", letters[0], letters[1], letters[2]],
                    ["י", letters[0], letters[1], letters[2], "ו"],
                    ["י", letters[0], letters[1], letters[2], "ו"]
                ]
                first_str = ["".join(first[0]), "".join(first[1]), "".join(first[2]), "".join(first[3])]
                second_str = ["".join(second[0]), "".join(second[1]), "".join(second[2]), "".join(second[3])]
                third_str = ["".join(third[0]), "".join(third[1]), "".join(third[2]), "".join(third[3])]

            elif letters[1] in gutturals or letters[2] in gutturals:
                #efal rule
                first = [
                    ["א", letters[0], letters[1], letters[2]],  # ms
                    ["א", letters[0], letters[1], letters[2]],
                    ["נ", letters[0], letters[1], letters[2]],
                    ["נ", letters[0], letters[1], letters[2]]
                ]
                second = [
                    ["ת", letters[0], letters[1], letters[2]],
                    ["ת", letters[0], letters[1], letters[2], "י"],
                    ["ת", letters[0], letters[1], letters[2], "ו"],
                    ["ת", letters[0], letters[1], letters[2], "ו"]
                ]
                third = [
                    ["י", letters[0], letters[1], letters[2]],
                    ["ת", letters[0], letters[1], letters[2]],
                    ["י", letters[0], letters[1], letters[2], "ו"],
                    ["י", letters[0], letters[1], letters[2], "ו"]
                ]
                first_str = ["".join(first[0]), "".join(first[1]), "".join(first[2]), "".join(first[3])]
                second_str = ["".join(second[0]), "".join(second[1]), "".join(second[2]), "".join(second[3])]
                third_str = ["".join(third[0]), "".join(third[1]), "".join(third[2]), "".join(third[3])]

            else:
                # efol rule:
                first = [
                    ["א", letters[0], letters[1], "ו", letters[2]], #ms
                    ["א", letters[0], letters[1], "ו", letters[2]],
                    ["נ", letters[0], letters[1], "ו", letters[2]],
                    ["נ", letters[0], letters[1], "ו", letters[2]]
                ]
                second = [
                    ["ת", letters[0], letters[1], "ו", letters[2]],
                    ["ת", letters[0], letters[1], letters[2], "י"],
                    ["ת", letters[0], letters[1], letters[2], "ו"],
                    ["ת", letters[0], letters[1], letters[2], "ו"]
                ]
                third = [
                    ["י", letters[0], letters[1], "ו", letters[2]],
                    ["ת", letters[0], letters[1], "ו", letters[2]],
                    ["י", letters[0], letters[1], letters[2], "ו"],
                    ["י", letters[0], letters[1], letters[2], "ו"]
                ]
                first_str = ["".join(first[0]), "".join(first[1]), "".join(first[2]), "".join(first[3])]
                second_str = ["".join(second[0]), "".join(second[1]), "".join(second[2]), "".join(second[3])]
                third_str = ["".join(third[0]), "".join(third[1]), "".join(third[2]), "".join(third[3])]
            print("conjugations for future tense pa'a, are unreliable due to large amounts of irregularity") #will add suport later
            return [first_str, second_str, third_str]

        elif tense == "Imperative":
            return

        elif tense == "Infinitive":
            return

        return

    def autoConjugatePiel(self, tense):
        pass

    def autoConjugateHifil(self, tense):
        pass

    def autoConjugateHitpael(self, tense):
        pass

    def autoConjugateHufal(self, tense):
        pass

    def autoConjugatePual(self, tense):
        pass

    def autoConjugateNiphal(self, tense):
        pass

    def autoConjugate(self, binyan, meaning):
        pass