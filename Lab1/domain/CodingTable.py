class CodingTable:

    def __init__(self):
        self.dict = {
            "identifier": 0,
            "constant": 1,
            "program": 2,
            "array": 3,
            "of": 4,
            "var": 5,
            "integer": 6,
            "real": 7,
            "boolean": 8,
            "begin": 9,
            "end": 10,
            "read": 11,
            "write": 12,
            "for": 13,
            "to": 14,
            "do": 15,
            "if": 16,
            "then": 17,
            "else": 18,
            "and": 19,
            "or": 20,
            "not": 21,
            ":": 22,
            ";": 23,
            ",": 24,
            ".": 25,
            "+": 26,
            "*": 27,
            "(": 28,
            ")": 29,
            "[": 30,
            "]": 31,
            "-": 32,
            "<": 33,
            ">": 34,
            "=": 35,
            "{": 36,
            "}": 37,
            "declare": 38,
            "while": 39,
            "<=": 40,

        }
        # print(self.dict)

    def get_value_for_key(self, key):
        return self.dict[key]

    def get_key_for_value(self, value):
        for key, value1 in self.dict.items():
            if value1 == value:
                return key
        return None

    def get_dict(self):
        return dict
