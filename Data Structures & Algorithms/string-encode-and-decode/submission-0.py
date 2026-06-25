class Solution:

    def encode(self, strs: List[str]) -> str:
        # im thinking to use the lengths of the strings and then 
        # put that at the begining of each string so it, im also thinkg of using a certain cahracter as a delimiter? it would be a tad bit over the 
        # space usasge but itcould work, then only read to the | and then skip
        final_encoded_string_list = ""

        for string in strs:
            encoded_prefix = str(len(string)) + '|'
            # using a delimiter for every single one because ill know 
            # it is always there, and i wont get confused if the strings 
            # start with numbers 

            encoded_string = encoded_prefix + string
            final_encoded_string_list += encoded_string

        print(final_encoded_string_list)

        return final_encoded_string_list

    def decode(self, s: str) -> List[str]:

        final_list = []
        length = len(s)
        
        index = 0
        index2 = 0


        while index2 < length:
            if s[index2] == '|':
                length_of_string = s[index:index2]
                start_of_string = index2 + 1
                end_of_string = index2 + int(length_of_string)

                final_list.append(s[start_of_string: end_of_string + 1])
                # ending index is not inclusive so it shouldnt include the |

                index = end_of_string + 1
                index2 = end_of_string + 1
            else:
                index2 += 1

        return final_list
            
                



