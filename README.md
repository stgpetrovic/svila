## Vrijeme

Za sada imas ode vrijeme/ koje implementira Vrijeme i Epizoda sa svim sta triba.

Uz to, imas i testove. Pogledaj kako izvrsit testove:

```bash
$ python vrijeme/vrijeme_test.py
..............
----------------------------------------------------------------------
Ran 14 tests in 0.001s

OK
```

Pizdarija.

Svi testovi prolaze naravno, al promini malo kod pa runnaj opet da vidis kako padaju.

Coverage -- kolika je pokrivenost testovima, koliko koda je pokriveno a koliko ne:
(Triba https://coverage.readthedocs.io/en/coverage-5.1/)


```bash
~/.local/bin/coverage3 run -m unittest discover  -s vrijeme -p "*_test.py"
```

```bash
~/.local/bin/coverage3 report
Name                      Stmts   Miss  Cover
---------------------------------------------
vrijeme/vrijeme.py           64     10    84%
---------------------------------------------
TOTAL                        64     10    84%

```

Uzas. Ajde vidi u htmlcov/ di fale testovi pa dodaj da bude oko 100%.
