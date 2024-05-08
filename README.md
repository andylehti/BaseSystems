# BaseSystems
#### Author: Andrew Lehti, apache2.0 license

I have created numerous base systems, some more complex than others. Initially, I had hundreds of code snippets, but I eventually consolidated them into just one or two snippets. The first version of **CompactBase** was over 100 lines long, but now it's under 20 lines. Developing this system took me a few months to fully understand. It's a base system where `00` equals `10` in base 10, and `000` equals `110`.

### AnyBase System
The **anyBase** system originated from experimenting with larger bases. However, converting to bases with many symbols became cumbersome and impractical due to the inefficiency of loading billions of symbols. I then wrote code that converts numbers into indexed symbols, so values could be represented as indices instead of the symbols themselves.

Example of converting a number into base `852794613`:

```python
anyBase(5638428967836249768942872649736, 852794613) = '9091 234051888 405375402 125093311'
```

### MultiBase System
The **multiBase** system was built upon anyBase and allows for multiple bases that can grow or progress according to your preferences. For instance, you can specify base 2 for the first slot and base 10 for the subsequent slots, or alternate bases for every second slot. Simply modify the behavior of `b` in the code.

Example conversions:

```python
10053 = 1 1 3 3 5 6 1 = 10053  True
10054 = 0 2 3 3 5 6 1 = 10054  True
```

### CompactBase System
The **CompactBase** system ensures data integrity while manipulating numerical parts. A number like `'250595065030'` can be divided into chunks without losing data. When converting and joining back, the integrity remains intact:

```python
convertBase('250 595 065 030', 10) = convertDecimal('140 485 55 20', 10) = '250 595 065 030', and joined again: '250595065030'
```

This system has other practical applications as well. Below are the values of each significant 0 in various bases:

#### Base 2:
```plaintext
0 = 0
00 = 2
000 = 6
0000 = 14
00000 = 30
000000 = 62
0000000 = 126
00000000 = 254
000000000 = 510
```

#### Base 3:
```plaintext
0 = 0
00 = 3
000 = 12
0000 = 39
00000 = 120
000000 = 363
0000000 = 1092
00000000 = 3279
000000000 = 9840
```

#### Base 4:
```plaintext
0 = 0
00 = 4
000 = 20
0000 = 84
00000 = 340
000000 = 1364
0000000 = 5460
00000000 = 21844
000000000 = 87380
```

#### Base 5:
```plaintext
0 = 0
00 = 5
000 = 30
0000 = 155
00000 = 780
000000 = 3905
0000000 = 19530
00000000 = 97655
000000000 = 488280
```

#### Base 6:
```plaintext
0 = 0
00 = 6
000 = 42
0000 = 258
00000 = 1554
000000 = 9330
0000000 = 55986
00000000 = 335922
000000000 = 2015538
```

#### Base 7:
```plaintext
0 = 0
00 = 7
000 = 56
0000 = 399
00000 = 2800
000000 = 19607
0000000 = 137256
00000000 = 960799
000000000 = 6725600
```

#### Base 8:
```plaintext
0 = 0
00 = 8
000 = 72
0000 = 584
00000 = 4680
000000 = 37448
0000000 = 299592
00000000 = 2396744
000000000 = 19173960
```

#### Base 9:
```plaintext
0 = 0
00 = 9
000 = 90
0000 = 819
00000 = 7380
000000 = 66429
0000000 = 597870
00000000 = 5380839
000000000 = 48427560
```

#### Base 10:
```plaintext
0 = 0
00 = 10
000 = 110
0000 = 1110
00000 = 11110
000000 = 111110
0000000 = 1111110
00000000 = 11111110
000000000 = 111111110
```

#### Base 11:
```plaintext
0 = 0
00 = 11
000 = 132
0000 = 1463
00000 = 16104
000000 = 177155
0000000 = 1948716
00000000 = 21435887
000000000 = 235794768
```

#### Base 12:
```plaintext
0 = 0
00 = 12
000 = 156
0000 = 1884
00000 = 22620
000000 = 271452
0000000 = 3257436
00000000 = 39089244
000000000 = 469070940
```

#### Base 13:
```plaintext
0 = 0
00 = 13
000 = 182
0000 = 2379
00000 = 30940
000000 = 402233
0000000 = 5229042
00000000 = 67977559
000000000 = 883708280
```

#### Base 14:
```plaintext
0 = 0
00 = 14
000 = 210
0000 = 2954
00000 = 41370
000000 = 579194
0000000 = 8108730
00000000 = 113522234
000000000 = 1589311290
```

#### Base 15:
```plaintext
0 = 0
00 = 15
000 = 240
0000 = 3615
00000 = 54240
000000 = 813615
0000000 = 12204240
00000000 = 183063615
000000000 = 2745954240
```
