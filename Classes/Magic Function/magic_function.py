class Magic:
    def __init__(self):
        pass

    def replace(self, string, old, new):
        return string.replace(old, new)

    def str_length(self, string):
        return len(string)

    def trim(self, string):
        return string.strip()

    def list_slice(self, list, tuple):
        return list[tuple[0]:tuple[1]]


magic = Magic
print(magic.replace("AzErty-QwErty", "E", "e"))
print(magic.str_length("hello world"))
print(magic.trim("      python is awesome      "))
print(magic.list_slice([1, 2, 3, 4, 5], (2, 4)))
