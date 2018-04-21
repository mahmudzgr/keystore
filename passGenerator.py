import secrets

lower_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
upper_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
specials = [' ','!','\"','#','$','%','&','\'','(',')','*','+','-',',','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']

def randCharL(length):
    password = []
    for i in range(length):
        odds = secrets.SystemRandom().randrange(0,1)
        if odds == 0:
            password += secrets.choice(lower_letters)
        else:
            password += secrets.choice(upper_letters)
    return password

def randCharLD(length):
    password = []
    password +=  secrets.choice(numbers)
    for i in range(length-1):
        odds = secrets.SystemRandom().randrange(0, 95)
        if odds < 40:
            password += secrets.choice(lower_letters)
        elif odds < 80:
            password += secrets.choice(upper_letters)
        else:
            password += secrets.choice(numbers)
    secrets.SystemRandom().shuffle(password)
    return password

def randCharLS(length):
    password = []
    password += secrets.choice(specials)
    for i in range(length-2):
        odds = secrets.SystemRandom().randrange(0, 85)
        if odds < 40:
            password += secrets.choice(lower_letters)
        elif odds < 80:
            password += secrets.choice(upper_letters)
        else:
            password += secrets.choice(specials)
    secrets.SystemRandom().shuffle(password)
    return password

def randCharLDS(length):
    password = []
    password += secrets.choice(numbers)
    password += secrets.choice(specials)
    for i in range(length-2):
        odds = secrets.SystemRandom().randrange(0, 100)
        if odds < 40:
            password += secrets.choice(lower_letters)
        elif odds < 80:
            password += secrets.choice(upper_letters)
        elif odds < 95:
            password += secrets.choice(numbers)
        else:
            password += secrets.choice(specials)
    secrets.SystemRandom().shuffle(password)
    return password


def passGenerator(length,digits,specials):
    if digits == "on" and specials == "on":
        return "".join(randCharLDS(length))
    elif digits == "on" and specials == "off":
        return "".join(randCharLD(length))
    elif digits == "off" and specials == "on":
        return "".join(randCharLS(length))
    elif digits == "off" and specials == "off":
        return "".join(randCharL(length))
