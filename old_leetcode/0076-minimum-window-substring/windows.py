"""
My previous solution was higher than linear in size of window being searched.

I looked up the hackrank solution because I couldn't see how to do better -
this is their solution
"""
from collections import Counter
from unittest import TestCase

from parameterized import parameterized


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        chars_required = Counter(t)
        chars_in_window = Counter()
        chars_satisfied = 0

        leading_chars = iter(enumerate(s))
        following_chars = iter(enumerate(s))

        smallest_window = len(s)
        max_ind_leading = -1
        max_ind_following = 0

        for ind_leading, leading in leading_chars:

            chars_in_window[leading] += 1
            if leading in chars_required and chars_in_window[leading] == chars_required[leading]:
                chars_satisfied += 1

            if chars_satisfied >= len(chars_required):

                for ind_following, following in following_chars:

                    if ind_leading - ind_following < smallest_window:
                        max_ind_leading = ind_leading
                        max_ind_following = ind_following
                        smallest_window = ind_leading - ind_following

                    chars_in_window[following] -= 1
                    if following in chars_required and chars_in_window[following] < chars_required[following]:
                        chars_satisfied -= 1
                        break

        return s[max_ind_following:max_ind_leading + 1]


class TestSolution(TestCase):

    @parameterized.expand([
        ("ABC", "DEF", ""),  # empty string
        ("ABC", "A", "A"),
        ("ABC", "AB", "AB"),
        ("ABC", "AC", "ABC"),
        ("ADBA", "AB", "BA"),
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("ABC", "AA", ""),
        ("ABCA", "AA", "ABCA"),
        ("ABACB", "AB", "AB"),  # shortest leading
        (
            "kgfidhktkjhlkbgjkylgdracfzjduycghkomrbfbkoowqwgaurizliesjnveoxmvjdjaepdqftmvsuyoogobrutahogxnvuxyezevfuaaiyufwjtezuxtpycfgasburzytdvazwakuxpsiiyhewctwgycgsgdkhdfnzfmvhwrellmvjvzfzsdgqgolorxvxciwjxtqvmxhxlcijeqiytqrzfcpyzlvbvrksmcoybxxpbgyfwgepzvrezgcytabptnjgpxgtweiykgfiolxniqthzwfswihpvtxlseepkopwuueiidyquratphnnqxflqcyiiezssoomlsxtyxlsolngtctjzywrbvajbzeuqsiblhwlehfvtubmwuxyvvpwsrhutlojgwktegekpjfidgwzdvxyrpwjgfdzttizquswcwgshockuzlzulznavzgdegwyovqlpmnluhsikeflpghagvcbujeapcyfxosmcizzpthbzompvurbrwenflnwnmdncwbfebevwnzwclnzhgcycglhtbfjnjwrfxwlacixqhvuvivcoxdrfqazrgigrgywdwjgztfrbanwiiayhdrmuunlcxstdsrjoapntugwutuedvemyyzusogumanpueyigpybjeyfasjfpqsqotkgjqaxspnmvnxbfvcobcudxflmvfcjanrjfthaiwofllgqglhkndpmiazgfdrfsjracyanwqsjcbakmjubmmowmpeuuwznfspjsryohtyjuawglsjxezvroallymafhpozgpqpiqzcsxkdptcutxnjzawxmwctltvtiljsbkuthgwwbyswxfgzfewubbpowkigvtywdupmankbndyligkqkiknjzchkmnfflekfvyhlijynjlwrxodgyrrxvzjhoroavahsapdiacwjpucnifviyohtprceksefunzucdfchbnwxplhxgpvxwrmpvqzowgimgdolirslgqkyc",
            "tjcwallfkarlrvfxchdqqtiutvfpoovjxzgxmtextvintpmvypnplyletrwhftreszdhshenfocadoxegkvrigxbzvleqckjdnsvvwkckncpdztjloauxaxwvibmmlxpbpmwnzaxmcopdiboydkvdisbqvpfiowjfjhsihrwlfnopodosnjxxdyqynvhbrqgcyamhrktzyhoomcgcoezrerssozvipekpezxyjqxjzlymqeqgkrzpjrjxqgfimszrtwrcoqmqbketqubbnbswsbwljdvwxupqtgtjwhzztdvjzwmnzglsjjftnapkwedpmybkfalyggjffyueegyopfhefyreeuvsswczznxfwimbghhlpgbelklticxoyugsrkrqzqxvyjyhqiufqvmdfzwpdvddqlvjvozwewuehslyahfsctwjsuyxsdaiqvtnlskpqewxyjxzrfttypftkdqcjtmzofnczxrrbpqzboastuntlsovyhxhalgqqtsrsmivbzxcnzwivkdhesccbcjbnsrelmvgygbbfyguyeetohavbfxehjfwbzconaulgwolwwhwblsruumyzmcivkfylhmyhjlphbadyjczwusrohrotvyqfdosncqwldmsfoyfyaeuuynifeyyaxqhcgaplsmywardorimtohnmuxsbysdxlkzrmrehfdffwitnqigepvslumoshrpserlsiqzpteupmneexkkmhdabrquyilqocegmuibpmxgbnkhkwszdxzeorapbmhpqlydhggyueevrqfdmxcrwdwmvwdwklmbykeismgmqnkjdpnqopjmtfyqeemopapnmvveierardkuuzmiqwwldwbhaowpqnfdjchrgarxfduzeihvedikakraapsqdxtmzdfidyfjebiiksfqxoazaucajusotmcuphcuikfmlqwxkcohsqhsmluyfmmaypupyzmgjtuwjrutvkdncmhpxb",
            ""
        )
    ])
    def test_empty_string(
            self, initial_string, window_letters, expected_output):

        solution = Solution()

        self.assertEqual(
            expected_output,
            solution.minWindow(initial_string, window_letters)
        )
