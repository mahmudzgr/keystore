import secrets


class WeightedRandom:
    total_weight    = 0
    weighted_values = []

    def __init__(self, weighted_values):
        self.weighted_values = weighted_values
        for val in weighted_values:
            self.total_weight += val.weight

    def get(self):
        odds = secrets.randbelow(self.total_weight)
        for i in range(len(self.weighted_values)):
            if odds < self.sum_until(i):
                return self.weighted_values[i]

    def sum_until(self, until):
        sum = 0
        for i in range(until + 1):
            sum += self.weighted_values[i].weight
        return sum


class WeightedValue:
    weight = 0

    def __init__(self, weight):
        self.weight = weight


class CharType(WeightedValue):
    chars = ""

    def __init__(self, chars, weight):
        WeightedValue.__init__(self, weight)
        self.chars = chars


class PasswordGenerator:

    __lowercase_chars    = list("abcdefghijklmnopqrstuvwxyz")
    __uppercase_chars    = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    __digit_chars        = list("0123456789")
    __special_chars      = list(" !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")

    __lowercase_weight   = 8
    __uppercase_weight   = 8
    __digits_weight      = 3
    __specials_weight    = 1

    char_types = {}

    lowercase   = False
    uppercase   = False
    digits      = False
    specials    = False

    def __init__(self):
        self.char_types['lowercase'] = CharType(self.__lowercase_chars,   self.__lowercase_weight)
        self.char_types['uppercase'] = CharType(self.__uppercase_chars,   self.__uppercase_weight)
        self.char_types['digits'] = CharType(self.__digit_chars,       self.__digits_weight)
        self.char_types['specials'] = CharType(self.__special_chars,     self.__specials_weight)

    def reset(self):
        self.lowercase  = False
        self.uppercase  = False
        self.digits     = False
        self.specials   = False

    def set(self, lowercase, uppercase, digits, specials):
        self.lowercase  = lowercase
        self.uppercase  = uppercase
        self.digits     = digits
        self.specials   = specials

    def generate(self, length):
        weighted_values = []
        if self.lowercase:
            weighted_values.append(self.char_types['lowercase'])
        if self.uppercase:
            weighted_values.append(self.char_types['uppercase'])
        if self.digits:
            weighted_values.append(self.char_types['digits'])
        if self.specials:
            weighted_values.append(self.char_types['specials'])
        if len(weighted_values) == 0:
            return 'Options are not specified!'
        weighted_random = WeightedRandom(weighted_values)
        password = ""
        for i in range(length):
            char_type = weighted_random.get()
            password += secrets.choice(char_type.chars)

        # Check if the password suits needs
        if self.lowercase and not contains_one(password, self.char_types['lowercase'].chars):
            return self.generate(length)
        if self.uppercase and not contains_one(password, self.char_types['uppercase'].chars):
            return self.generate(length)
        if self.digits and not contains_one(password, self.char_types['digits'].chars):
            return self.generate(length)
        if self.specials and not contains_one(password, self.char_types['specials'].chars):
            return self.generate(length)
        return password


def contains_one(text, array):
    for char in array:
        if char in text:
            return True
    return False
