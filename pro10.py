from collections import Counter
X = int(input())
shoes = list(map(int, input().split()))
C = Counter(shoes)
N = int(input())
earned = 0
for i in range(0, N):
    size, price = map(int, input().split())
    if C[size] > 0:
        earned += price
        C[size] -= 1
print(earned)
# from collections import deque
# for _ in range(int(input())):
#     flag = True
#     input()
#     d = deque(map(int, input().strip().split()))
#     if (d[0] >= d[-1]):
#         max = d.popleft()
#     else:
#         max = d.pop()
#     while d:
#         if (len(d) == 1):
#             if (d[0] <= max):
#                 break
#             else:
#                 flag = False
#                 break;
#         else:
#             if d[0] <= max and d[-1] <= max:
#                 if d[0] >= d[-1]:
#                     max = d.popleft()
#                 else:
#                    max = d.pop()
#             elif d[0] <= max:
#                 max = d.popleft()
#             elif d[-1] <= max:
#                 max = d.pop()
#             else:
#                 flag = False
#                 break;
#     if flag:
#         print("Yes")
#     else:
#         print("No")
# from collections import defaultdict
# d = defaultdict(list)
# n, m = map(int, input().split())
# for i in range(n):
#     w = input()
#     d[w].append(str(i+1))
# for j in range(m):
#     w = input()
#     print(' '.join(d[w]) or -1)
# n = int(input())
# col_list = list(input().split())
# marks_col = col_list.index("MARKS")
# marks_list = []
# for i in range(n):
#     info_list = list(input().split())
#     marks_list.append(float(info_list[marks_col]))
# print(sum(marks_list)/n)
# import collections
# n = int(input())
# d = collections.deque()
# for i in range(n):
#     cmd = list(input().strip().split())
#     opt = cmd[0]
#     if opt == 'pop':
#         d.pop()
#     elif opt == 'popleft':
#         d.popleft()
#     elif opt == 'append':
#         d.append(int(cmd[1]))
#     elif opt == 'appendleft':
#         d.appendleft(int(cmd[1]))
# for i in d:
#     print(i,end=' ')
# import collections, re
# n = int(input())
# item_od = collections.OrderedDict()
# for i in range(n):
#     record_list = re.split(r'(\d+)$', input().strip())
#     item_name = record_list[0]
#     item_price = int(record_list[1])
#     if item_name not in item_od:
#         item_od[item_name] = item_price
#     else:
#         item_od[item_name] = item_od[item_name] + item_price
# for i in item_od:
#     print(i + str(item_od[i]))
# import itertools
# s = input().strip()
# s_unique_element = list(set(s))
# group = []
# key = []
# for k,g in itertools.groupby(s):
#     group.append(list(g))
#     key.append(k)
# for i in range(len(group)):
#     group_length = len(group[i])
#     k = int(key[i])
#     print(tuple((group_length,k)),end=' ')
# from itertools import combinations
# n = int(input())
# ar = input().split()
# k = int(input())
# comb_list = list(combinations(ar,k))
# a_list = [e for e in comb_list if 'a' in e]
# print(len(a_list) / len(comb_list))
# import itertools
# k, m = map(int, input().split())
# main_ar = []
# for i in range(k):
#     ar = list(map(int, input().split()))
#     main_ar.append(ar[1:])
# all_combination = itertools.product(*main_ar)
# result = 0
# for single_combination in all_combination:
#     result = max(sum([x*x for x in single_combination])%m, result)
# print(result)
# n = input()
# ar = map(int, input().split(' '))
# ar = set(ar)
# print(sum(ar) / len(ar))
# import math
# ab = float(input())
# bc = float(input())
# ac = math.sqrt((ab*ab)+(bc*bc))
# bm = ac / 2.0
# mc = bm
# b = mc
# c = bm
# a = bc
# angel_b_radian = math.acos(a / (2*b))
# angel_b_degree = int(round((180 * angel_b_radian) / math.pi))
# output_str = str(angel_b_degree)+'°'
# print(output_str)
# from html.parser import HTMLParser
# class CustomHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print(tag)
#         self.handle_attrs(attrs)
#     def handle_startendtag(self, tag, attrs):
#         print(tag)
#         self.handle_attrs(attrs)
#     def handle_attrs(self, attrs):
#         for attrs_pair in attrs:
#             print('->', attrs_pair[0].strip(), '>', attrs_pair[1].strip())
# n = int(input())
# html_string = ''
# for i in range(n):
#     html_string += input()
# customHTMLParser = CustomHTMLParser()
# customHTMLParser.feed(html_string)
# customHTMLParser.close()
# import re
# s = input()
# res = re.search(r'([A-Za-z0-9])\1',s)
# if res == None:
#     print(-1)
# else:
#     print(res.group(1))
# from html.parser import HTMLParser
# class CustomHTMLParser(HTMLParser):
#     def handle_attr(self, attrs):
#         for attr_val_tuple in attrs:
#             print('->', attr_val_tuple[0], '>', attr_val_tuple[1])
#     def handle_starttag(self, tag, attrs):
#         print("Start :", tag)
#         self.handle_attr(attrs)
#     def handle_endtag(self, tag):
#         print("End   :", tag)
#     def handle_startendtag(self, tag, attrs):
#         print("Empty :", tag)
#         self.handle_attr(attrs)
# parser = CustomHTMLParser()
# n = int(input())
# s = ''
# for i in range(n):
#     s += input()
# parser.feed(s)
# '''
# 2
# <html><head><title>HTML Parser - I</title></head>
# <body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
# '''
# from html.parser import HTMLParser
# class CustomHTMLParser(HTMLParser):
#     def handle_comment(self, data):
#         number_of_line = len(data.split('\n'))
#         if number_of_line > 1:
#             print('>>> Multi-line Comment')
#         else:
#             print('>>> Single-line Comment')
#         if data.strip():
#             print(data)
#     def handle_data(self, data):
#         if data.strip():
#             print(">>> Data")
#             print(data)
# parser = CustomHTMLParser()
# n = int(input())
# html_string = ''
# for i in range(n):
#     html_string += input().rstrip() + '\n'
# parser.feed(html_string)
# parser.close()
# import re
# n = int(input())
# for t in range(n):
#     s = input()
#     match_result = re.findall(r'(#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6})(?:[;,.)]{1})',s)
#     for i in match_result:
#         if i != '':
#             print(i)
# import re
# n, m = map(int,input().split())
# character_ar = [''] * (n*m)
# for i in range(n):
#     line = input()
#     for j in range(m):
#         character_ar[i+(j*n)]=line[j]
# decoded_str = ''.join(character_ar)
# final_decoded_str = re.sub(r'(?<=[A-Za-z0-9])([ !@#$%&]+)(?=[A-Za-z0-9])',' ',decoded_str)
# print(final_decoded_str)
# import re
# s = input()
# result = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',s)
# if result:
#     for i in result:
#         print(i)
# else:
#     print(-1)