
class Calculator:
    def add(self, string):
        if string == "":
            return 0
        elif "," in string:
            total = 0
            for i in string:
                if i != ',':
                    total += int(i)
            return total
        else:
            return int(string)

