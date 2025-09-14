
def regexToStandarizeRegex(regex:str)->str:
    new_regex = regex.replace("𝜀",">")
    new_regex = new_regex.replace("|", "_")

    print(new_regex)
    return new_regex
