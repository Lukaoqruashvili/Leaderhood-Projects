#Anagram Detection
def is_anagram(test, original):
    testlowered = test.lower()
    originallowered = original.lower()
    if sorted(testlowered) == sorted(originallowered):
        return True
    else:
        return False