HUB75E "hat" hardware
=====================

Layout/numbering
----------------

The board consists of 10 connectors (marked J1-J10) and 6 74HC245TS buffers (marked U1-U6).

J600/J601 connectors are numbered as per RV901T markings.

HUB75E connectors
----------------

```
  _________
 |  R1 G1  |
 |  B1 GND |
 |  R2 G2  |
  | B2 E   |
  |  A B   |
 |   C D   |
 | CLK STB |
 |  OE GND |
  ---------
```

74HC245 buffers
----------------

`DIR` on all buffers is strapped to `VCC`.

| Buffer U1                        |
|----------------------------------|
| Ch. | A-side   | B-side          |
|---|------------|-----------------|
| 0 | J601.44    | J1.CLK          |
| 1 | J601.44    | J2.CLK          |
| 2 | J601.44    | J3.CLK          |
| 3 | J601.44    | J4.CLK          |
| 4 | J601.44    | J5.CLK          |
| 5 | J601.43    | J1.LAT, J2.LAT  |
| 6 | J601.43    | J3.LAT, J4.LAT  |
| 7 | J601.43    | J5.LAT, J6.LAT  |

| Buffer U2                        |
|----------------------------------|
| Ch. | A-side   | B-side          |
|---|------------|-----------------|
| 0 | J601.43    | J7.LAT, J8.LAT  |
| 1 | J601.43    | J9.LAT, J10.LAT |
| 2 | J602.42    | J1.A, J2.A      |
| 3 | J602.42    | J3.A, J4.A      |
| 4 | J602.42    | J5.A, J6.A      |
| 5 | J602.42    | J7.A, J8.A      |
| 6 | J602.42    | J9.A, J10.A     |
| 7 | J601.41    | J1.B, J2.B      |


| Buffer U3                      |
|--------------------------------|
| Ch. | A-side   | B-side        |
|---|------------|---------------|
| 0 | J601.41    | J3.B, J4.B    |
| 1 | J601.41    | J5.B, J6.B    |
| 2 | J601.41    | J7.B, J8.B    |
| 3 | J601.41    | J9.B, J10.B   |
| 4 | J601.40    | J1.C, J2.C    |
| 5 | J601.40    | J3.C, J4.C    |
| 6 | J601.40    | J5.C, J6.C    |
| 7 | J601.40    | J7.C, J8.C    |

| Buffer U4                      |
|--------------------------------|
| Ch. | A-side   | B-side        |
|---|------------|---------------|
| 0 | J601.40    | J10.C, J9.C   |
| 1 | J601.39    | J1.D, J2.D    |
| 2 | J601.39    | J3.D, J4.D    |
| 3 | J601.39    | J5.D, J6.D    |
| 4 | J601.39    | J7.D, J8.D    |
| 5 | J601.39    | J9.D, J10.D   |
| 6 | J600.44    | J9.CLK        |
| 7 | J600.44    | J10.CLK       |

| Buffer U5                      |
|--------------------------------|
| Ch. | A-side   | B-side        |
|---|------------|---------------|
| 0 | J600.45    | J1.OE, J2.OE  | 
| 1 | J600.45    | J3.OE, J4.OE  | 
| 2 | J600.45    | J5.OE, J6.OE  | 
| 3 | J600.45    | J7.OE, J8.OE  | 
| 4 | J600.45    | J9.OE, J10.OE | 
| 5 | J600.44    | J6.CLK        |
| 6 | J600.44    | J7.CLK        |
| 7 | J600.44    | J8.CLK        |

| Buffer U6                             |
|---------------------------------------|
| Ch. | A-side   | B-side               |
|---|------------|----------------------|
| 0 | J600.6     | J10.E, J9.E (via R3) |
| 1 | J600.6     | J8.E, J7.E (via R4)  |
| 2 | J600.6     | J6.E, J5.E (via R5)  |
| 3 | J600.6     | J4.E, J3.E (via R6)  |
| 4 | J600.6     | J2.E, J1.E (via R7)  |
| 5 | NC         | NC                   |
| 6 | NC         | NC                   |
| 7 | NC         | NC                   |


Final pinout
------------

| Signal          | J600/J601 pin                      |
|-----------------|------------------------------------|
| HUB75.*.OE      | J600.45 (via U5)                   |
| HUB75.*.LAT     | J601.43 (via U1, U2)               |
| HUB75.*.CLK     | J601.44 (via U1), J600.44 (via U4) |
| HUB75.*.A       | J602.42 (via U2)                   |
| HUB75.*.B       | J601.41 (via U2, U3)               |
| HUB75.*.C       | J601.40 (via U3, U4)               |
| HUB75.*.D       | J601.39 (via U4)                   |
| HUB75.*.E       | J600.6 (via U6 and resistors)      |
| HUB75.J1.RD1    | J601.38                            |
| HUB75.J1.GD1    | J601.37                            |
| HUB75.J1.BD1    | J601.36                            |
| HUB75.J1.RD2    | J601.35                            |
| HUB75.J1.GD2    | J601.34                            |
| HUB75.J1.BD2    | J601.33                            |
| HUB75.J2.RD1    | J601.32                            |
| HUB75.J2.GD1    | J601.31                            |
| HUB75.J2.BD1    | J601.30                            |
| HUB75.J2.RD2    | J601.29                            |
| HUB75.J2.GD2    | J601.28                            |
| HUB75.J2.BD2    | J601.27                            |
| HUB75.J3.RD1    | J601.26                            |
| HUB75.J3.GD1    | J601.25                            |
| HUB75.J3.BD1    | J601.24                            |
| HUB75.J3.RD2    | J601.23                            |
| HUB75.J3.GD2    | J601.22                            |
| HUB75.J3.BD2    | J601.21                            |
| HUB75.J4.RD1    | J601.20                            |
| HUB75.J4.GD1    | J601.19                            |
| HUB75.J4.BD1    | J601.18                            |
| HUB75.J4.RD2    | J601.17                            |
| HUB75.J4.GD2    | J601.16                            |
| HUB75.J4.BD2    | J601.15                            |
| HUB75.J5.RD1    | J601.14                            |
| HUB75.J5.GD1    | J601.13                            |
| HUB75.J5.BD1    | J601.12                            |
| HUB75.J5.RD2    | J601.11                            |
| HUB75.J5.GD2    | J601.10                            |
| HUB75.J5.BD2    | J601.9                             |
| HUB75.J6.RD1    | J600.38                            |
| HUB75.J6.GD1    | J600.37                            |
| HUB75.J6.BD1    | J600.36                            |
| HUB75.J6.RD2    | J600.35                            |
| HUB75.J6.GD2    | J600.34                            |
| HUB75.J6.BD2    | J600.33                            |
| HUB75.J7.RD1    | J600.32                            |
| HUB75.J7.GD1    | J600.31                            |
| HUB75.J7.BD1    | J600.30                            |
| HUB75.J7.RD2    | J600.29                            |
| HUB75.J7.GD2    | J600.28                            |
| HUB75.J7.BD2    | J600.27                            |
| HUB75.J8.RD1    | J600.26                            |
| HUB75.J8.GD1    | J600.25                            |
| HUB75.J8.BD1    | J600.24                            |
| HUB75.J8.RD2    | J600.23                            |
| HUB75.J8.GD2    | J600.22                            |
| HUB75.J8.BD2    | J600.21                            |
| HUB75.J9.RD1    | J600.20                            |
| HUB75.J9.GD1    | J600.19                            |
| HUB75.J9.BD1    | J600.18                            |
| HUB75.J9.RD2    | J600.17                            |
| HUB75.J9.GD2    | J600.16                            |
| HUB75.J9.BD2    | J600.15                            |
| HUB75.J10.RD1   | J600.14                            |
| HUB75.J10.GD1   | J600.13                            |
| HUB75.J10.BD1   | J600.12                            |
| HUB75.J10.RD2   | J600.11                            |
| HUB75.J10.GD2   | J600.10                            |
| HUB75.J10.BD2   | J600.9                             |
