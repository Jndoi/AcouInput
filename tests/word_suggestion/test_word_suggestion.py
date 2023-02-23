"""
@Project :AcouInput
@File ：test_word_suggestion.py
@Date ： 2023/2/23 16:52
@Author ： Qiuyang Zeng
@Software ：PyCharm

"""
from word_suggestion.word_suggestion import spell_correction


def test_spell_correction():
    res = spell_correction("intereting")
    assert res == "interesting"


# lookup suggestions for single-word input strings
# arr = ['bg', 'dag', 'dag', 'tven', 'gjve', 'havc', 'havs', 'mere', 'nere', 'nere', 'htre', 'ber', 've', 'cike',
# 'mang', 'mang', 'ng', 'onlg', 'sag', 'sag', 'thejr', 'theg', 'theg', 'yheg', 'yheg', 'verg', 'erg', 'rery', 'wag',
# 'yag', 'ytar', 'ycar', 'gcar', 'gear']
# label = ['by', 'day', 'day', 'even', 'give', 'have', 'have', 'here', 'here', 'here', 'here', 'her', 'he', 'like',
#          'many', 'many', 'my', 'only', 'say', 'say', 'their', 'they', 'they', 'they', 'they', 'very', 'very', 'very',
#          'way', 'way', 'year', 'year', 'year', 'year']
# suggestions = []
# max edit distance per lookup
# for term in arr:
#     suggestion = sym_spell.lookup(
#         term, Verbosity.CLOSEST, max_edit_distance=2, include_unknown=True
#     )[0].term
#     suggestions.append(suggestion)
# display suggestion term, edit distance, and term frequency
# print(suggestions)
# count = 0
# for i, j in zip(suggestions, label):
#     if i == j:
#         count = count + 1
# print(count)
# print(cal_cer_total(suggestions, label))
