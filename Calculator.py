import re

class Calculator:
    def add(self, string):
        new_string = re.sub(r'[^0-9]', ',', string)
        if string == "":
            return 0
        elif "," in new_string:
            total = 0
            for i in new_string:
                if i != ',':
                    total += int(i)
            return total
        else:
            return int(string)

