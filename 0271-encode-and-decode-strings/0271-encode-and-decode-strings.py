class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        encoded_string = ""
        
        for string in strs:
            # Encode as <length>#<string>
            encoded_string += str(len(string)) + "#" + string
        
        return encoded_string
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        decoded_strings = []
        i = 0
        
        while i < len(s):
            # Find the delimiter (the "#")
            delimiter = s.find("#", i)
            # Extract the length
            length = int(s[i:delimiter])
            # Extract the string using the length
            i = delimiter + 1  # Move i to the start of the actual string
            decoded_strings.append(s[i:i+length])
            i += length  # Move i to the start of the next encoded part
        
        return decoded_strings
        

# Example Usage:
# codec = Codec()
# encoded = codec.encode(["hello", "world"])
# print(encoded)  # Output should be "5#hello5#world"
# decoded = codec.decode(encoded)
# print(decoded)  # Output should be ["hello", "world"]
