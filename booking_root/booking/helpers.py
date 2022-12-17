def preprocess(unformatted):
    if isinstance(unformatted, list):
        return preprocess_list(unformatted)
    if isinstance(unformatted, str):
        return preprocess_string(unformatted)
    return unformatted


def preprocess_string(unformattedString: str) -> str:
    if unformattedString is None:
        return unformattedString 
    if unformattedString == "":
        return unformattedString
    return unformattedString.replace('\r', '').replace('\n', ' ').strip()

def preprocess_list(unformattedList: list) -> str:
    if len(unformattedList) == 0:
        return ""
    else:
        return preprocess_string(' '.join(unformattedList))
