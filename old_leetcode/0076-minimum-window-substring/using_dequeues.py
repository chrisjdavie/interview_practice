"""


"""
from collections import Counter, deque
from typing import Deque, Dict, List, Optional, Set
from unittest import TestCase

from parameterized import parameterized


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        candidate_posn: Dict[str, Deque[int]] = {
            cand: deque() for cand in t
        }
        required_chars_count = Counter(t)

        shortest_first: Optional[int] = None
        shortest_last: Optional[int] = None
        shortest_length: int = len(s) + 1  # initialise to a large number
        current_first: Optional[int] = None

        posns: Set[int] = set()

        for index, char in enumerate(s):
            if char in candidate_posn:
                candidate_posn[char].append(index)
                posns.add(index)

                if current_first is None:
                    first = index

                if len(candidate_posn[char]) > required_chars_count[char]:
                    removed = candidate_posn[char].popleft()
                    posns.remove(removed)
                    if removed == first:
                        

                if len(posns) == len(t):
                    tmp_first: int = min(posns)
                    tmp_last = index
                    tmp_length: int = tmp_last - tmp_first
                    if tmp_length < length:
                        length, first, last = \
                            tmp_length, tmp_first, tmp_last

        if first is not None and last is not None:
            return s[first:last + 1]
        return ""


class TestSolution(TestCase):

    @parameterized.expand([
        ("ABC", "DEF", ""),  # empty string
        ("ABC", "A", "A"),
        ("ABC", "AB", "AB"),
        ("ABC", "AC", "ABC"),
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("ABC", "AA", ""),
        ("ABCA", "AA", "ABCA"),
        ("ABACB", "AB", "AB"),  # shortest first
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
