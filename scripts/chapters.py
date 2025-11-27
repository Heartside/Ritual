import re

chaps = '''
00:00:00.000                             : en:30 days remain
00:02:29.191                             : en:29 days remain
00:03:31.878                             : en:28 days remain
00:05:43.885                             : en:27 days remain
00:11:46.039                             : en:26 days remain
00:14:18.649                             : en:25 days remain
00:22:17.169                             : en:24 days remain
00:26:18.494                             : en:23 days remain
00:32:04.005                             : en:22 days remain
00:33:54.366                             : en:21 days remain
00:41:52.218                             : en:20 days remain
00:43:10.046                             : en:19 days remain
00:48:46.048                             : en:18 days remain
00:51:25.207                             : en:17 days remain
00:52:10.419                             : en:16~12 days remain
00:53:11.980                             : en:11 days remain 
00:55:10.807                             : en:10 days remain
01:00:43.139                             : en:9 days remain
01:09:26.329                             : en:3 days remain
01:17:18.509                             : en:2 days remain
01:34:26.953                             : en:the day before
01:54:00.834                             : en:the day
02:01:49.427                             : en:the day after
02:07:42.029                             : en:unknown 
'''.strip().splitlines()

for i, line in enumerate(chaps, 1):
    time, name = re.split(' : (?:[a-z]{2}:)?', line.strip())
    # name = name.split('. ', 1)[1]  # uncomment to remove numbers in front of the names
    print(f'CHAPTER{i:02d}={time}\nCHAPTER{i:02d}NAME={name}')