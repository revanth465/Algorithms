"""
    Rabin Karp Algorithm works on the concept of Hashing.
    It uses hash of pattern, and hash of input string (equal to pattern length)
    If both hashes are equal, it compares the characters of pattern and input string (pattern length) to determine if pattern is found in ths string.
    ****      Heart of Rabin Karp algorithm lies in its Hash Function       ****
            Hash Function : Rolling Hash
            prime : 101
    ****                                                                    ****
"""
import math
prime = 101
char_length = 256
pattern_length = 0
h = 1

class rabinKarp:
    def calculateFirstHash(self, pattern):
        value = 0
        for ch in pattern:
            value = ( value*char_length + ord(ch) ) % prime
        return value

    def calculateHash(self, text, text_hash, i):
        value =  (char_length*(text_hash-ord(text[i-1])*h) + ord(text[i+pattern_length-1]))%prime
        if(value<0):
            value = value + prime
        return value

    def computePatternMatch(self, text, pattern):
        indices = list()
        i = 0
        pattern_hash = rabinkarp.calculateFirstHash(pattern)
        text_hash = rabinkarp.calculateFirstHash(text[:pattern_length])
        if(pattern_hash == text_hash):
            result = rabinkarp.comparePatternAndSubText(pattern, text[i:len(pattern)])
            if (result):
                indices.append(i)
        i = 1
        while( i <= (len(text) - pattern_length)):
            text_hash = rabinkarp.calculateHash(text, text_hash, i)
            if(text_hash == pattern_hash):
                result = rabinkarp.comparePatternAndSubText(pattern, text[i:i+pattern_length])
                if(result):
                    indices.append(i)
            i += 1
        return indices

    def comparePatternAndSubText(self, pattern, sub_text):
        i = 0
        while(i < pattern_length):
            if( not str(pattern[i:i+1]).__eq__(str(sub_text[i:i+1])) ):
                return False
            i += 1
        return True

    def main(self):
        global pattern_length, h
        try:
            text = str(input("Enter the text : ")).strip()
            pattern = str(input("Enter the pattern to match :")).strip()
            if(len(pattern) > len(text)):
                raise ValueError("Pattern Length is greater than Text Length !!!")
            elif(len(pattern) == 0 or len(text) == 0):
                raise ValueError("Either Pattern or Text are empty, Please Enter again !!!")
            else:
                pattern_length = len(pattern)
                h = math.pow(char_length, pattern_length-1) % prime
                indices = rabinkarp.computePatternMatch(text,pattern)
                if(len(indices) == 0 ):
                    print("Program Executed Successfully, But No Pattern Found in Text :( :( ")
                else:
                    print("Program Executed Successfullu, Pattern found at : " + str(indices))
        except Exception as e:
            print("Error occured : " + str(e))

rabinkarp = rabinKarp()
if __name__ == '__main__':
    rabinkarp.main()
