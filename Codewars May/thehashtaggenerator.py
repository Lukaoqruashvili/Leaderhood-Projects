def generate_hashtag(s):
    symbol = '#'
    for i in s.split():
        symbol += i.capitalize()
        
    if len(s) == 0 or len(symbol) > 140:
        return False
    else:
        return symbol