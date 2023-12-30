def strtobool (val):
    inp = val.lower()
    check = ["yes","true","ok","1"]
    if (check.__contains__(inp)):
        return True
    return False