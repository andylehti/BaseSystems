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

```
Base 2:

| Compact Base | Decimal Conversion | Decimal Value ÷ Base |
|--------------|--------------------|----------------------|
| 0            | 0                  | 0                    |
| 00           | 2                  | 1                    |
| 000          | 6                  | 3                    |
| 0000         | 14                 | 7                    |
| 00000        | 30                 | 15                   |
| 000000       | 62                 | 31                   |
| 0000000      | 126                | 63                   |

Base 3:

| Compact Base | Decimal Conversion | Decimal Value ÷ Base |
|--------------|--------------------|----------------------|
| 0            | 0                  | 0                    |
| 00           | 3                  | 1                    |
| 000          | 12                 | 4                    |
| 0000         | 39                 | 13                   |
| 00000        | 120                | 40                   |
| 000000       | 363                | 121                  |
| 0000000      | 1092               | 364                  |

Base 4:

| Compact Base | Decimal Conversion | Decimal Value ÷ Base |
|--------------|--------------------|----------------------|
| 0            | 0                  | 0                    |
| 00           | 4                  | 1                    |
| 000          | 20                 | 5                    |
| 0000         | 84                 | 21                   |
| 00000        | 340                | 85                   |
| 000000       | 1364               | 341                  |
| 0000000      | 5460               | 1365                 |

Base 5:

| Compact Base | Decimal Conversion | Decimal Value ÷ Base |
|--------------|--------------------|----------------------|
| 0            | 0                  | 0                    |
| 00           | 5                  | 1                    |
| 000          | 30                 | 6                    |
| 0000         | 155                | 31                   |
| 00000        | 780                | 156                  |
| 000000       | 3905               | 781                  |
| 0000000      | 19530              | 3906                 |

Base 6:

| Compact Base | Decimal Conversion | Decimal Value ÷ Base |
|--------------|--------------------|----------------------|
| 0            | 0                  | 0                    |
| 00           | 6                  | 1                    |
| 000          | 42                 | 7                    |
| 0000         | 258                | 43                   |
| 00000        | 1554               | 259                  |
| 000000       | 9330               | 1555                 |
| 0000000      | 55986              | 9331                 |

Base 7:

| Compact Base | Decimal Conversion | Decimal Value ÷ Base |
|--------------|--------------------|----------------------|
| 0            | 0                  | 0                    |
| 00           | 7                  | 1                    |
| 000          | 56                 | 8                    |
| 0000         | 399                | 57                   |
| 00000        | 2800               | 400                  |
| 000000       | 19607              | 2801                 |
| 0000000      | 137256             | 19608                |

Base 8:

| Compact Base | Decimal Conversion | Decimal Value ÷ Base |
|--------------|--------------------|----------------------|
| 0            | 0                  | 0                    |
| 00           | 8                  | 1                    |
| 000          | 72                 | 9                    |
| 0000         | 584                | 73                   |
| 00000        | 4680               | 585                  |
| 000000       | 37448              | 4681                 |
| 0000000      | 299592             | 37449                |

Base 9:

| Compact Base | Decimal Conversion | Decimal Value ÷ Base |
|--------------|--------------------|----------------------|
| 0            | 0                  | 0                    |
| 00           | 9                  | 1                    |
| 000          | 90                 | 10                   |
| 0000         | 819                | 91                   |
| 00000        | 7380               | 820                  |
| 000000       | 66429              | 7381                 |
| 0000000      | 597870             | 66430                |

Base 10:

| Compact Base | Decimal Conversion | Decimal Value ÷ Base |
|--------------|--------------------|----------------------|
| 0            | 0                  | 0                    |
| 00           | 10                 | 1                    |
| 000          | 110                | 11                   |
| 0000         | 1110               | 111                  |
| 00000        | 11110              | 1111                 |
| 000000       | 111110             | 11111                |
| 0000000      | 1111110            | 111111               |

Base 11:

| Compact Base | Decimal Conversion | Decimal Value ÷ Base |
|--------------|--------------------|----------------------|
| 0            | 0                  | 0                    |
| 00           | 11                 | 1                    |
| 000          | 132                | 12                   |
| 0000         | 1463               | 133                  |
| 00000        | 16104              | 1464                 |
| 000000       | 177155             | 16105                |
| 0000000      | 1948716            | 177156               |

Base 12:

| Compact Base | Decimal Conversion | Decimal Value ÷ Base |
|--------------|--------------------|----------------------|
| 0            | 0                  | 0                    |
| 00           | 12                 | 1                    |
| 000          | 156                | 13                   |
| 0000         | 1884               | 157                  |
| 00000        | 22620              | 1885                 |
| 000000       | 271452             | 22621                |
| 0000000      | 3257436            | 271453               |

Base 13:

| Compact Base | Decimal Conversion | Decimal Value ÷ Base |
|--------------|--------------------|----------------------|
| 0            | 0                  | 0                    |
| 00           | 13                 | 1                    |
| 000          | 182                | 14                   |
| 0000         | 2379               | 183                  |
| 00000        | 30940              | 2380                 |
| 000000       | 402233             | 30941                |
| 0000000      | 5229042            | 402234               |

Base 14:

| Compact Base | Decimal Conversion | Decimal Value ÷ Base |
|--------------|--------------------|----------------------|
| 0            | 0                  | 0                    |
| 00           | 14                 | 1                    |
| 000          | 210                | 15                   |
| 0000         | 2954               | 211                  |
| 00000        | 41370              | 2955                 |
| 000000       | 579194             | 41371                |
| 0000000      | 8108730            | 579195               |

Base 15:

| Compact Base | Decimal Conversion | Decimal Value ÷ Base |
|--------------|--------------------|----------------------|
| 0            | 0                  | 0                    |
| 00           | 15                 | 1                    |
| 000          | 240                | 16                   |
| 0000         | 3615               | 241                  |
| 00000        | 54240              | 3616                 |
| 000000       | 813615             | 54241                |
| 0000000      | 12204240           | 813616               |
```
