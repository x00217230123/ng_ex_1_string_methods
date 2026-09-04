encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""

###############################################################
"""
1. Part of the real message is inside the the '[' and ']' brackets.
2. Each fragment inside the brackets has a number, jumbled text of the message, and 'ok'. Focus on only those fragments. The '::' are just separating these parts in the fragment 
3. To find the actual message in every fragment,take every letter in the jumbled message, and shift it backward by the number part in that fragment
For example, if the number is 3 and the jumbled message is ABC, then the actual message is XYZ.
Similarly, if the number is 5 and the jumbled message is ABC, then the actual message is VWX.
4. Ignore any fragment that has 'bad' instead of 'ok'.
5. Once you have decoded all the fragments, combine them in the order of their numbers to get the final message. First comes the fragment with number 1, then 2, and so on.
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import re

fragments = []
pattern = r'\[(\d+)::([^:]+)::ok\]'
matches = re.findall(pattern, encoded)

for num_str, jumbled in matches:
    num = int(num_str)
    decoded = ''
    for char in jumbled:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = (pos - num) % 26
            decoded += alphabet[new_pos]
        elif char == '_':
            decoded += '_'
        else:
            decoded += char
    fragments.append((num, decoded))

fragments.sort(key=lambda x: x[0])
final_message = ''.join([frag[1] for frag in fragments])

print('Decoded message:', final_message)
