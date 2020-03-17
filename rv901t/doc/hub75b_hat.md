HUB75B "hat" hardware
=====================

Layout/numbering
----------------

Board consists of just a bunch of unnumbered connectors and 74HC245D buffers,
thus all components in this document are numbered from top-left to bottom-right
relative to "HUB75E" test printed on the board, as per a quick sketch below.
HUB75B connectors (1-8) are counted from left to right. J600/J601 connectors
are numbered as per RV901T markings. (ie. J600 being the bottom connector, near
buffers 4 & 5)

```
 .............
1  2  3
| | | | | | | |
cap        4  5
 .............
```

74HC245D buffers
----------------

`DIR` on all buffers is strapped to `VCC`.

| Buffer 1 | |
|---------|---------|
| A1 - A4 | J601.42 |
| A5 - A8 | J601.41 |
| B1 - B4 | HUB75.8 - HUB75.1 (A; bridged in pairs of 2) |
| B5 - B8 | HUB75.8 - HUB75.1 (B; bridged in pairs of 2) |

| Buffer 2 | |
|---------|---------|
| A1 - A4 | J601.44 |
| A5 - A8 | J601.43 |
| B1 - B4 | HUB75.8 - HUB75.5 (CLK) |
| B5 - B8 | HUB75.8 - HUB75.5 (STB) |

| Buffer 3 | |
|---------|---------|
| A1 - A8 | J601.6 |
| B1 - B8 | HUB75.8 - HUB75.1 (OE) |

| Buffer 4 | |
|---------|---------|
| A1 - A4 | J600.44 |
| A5 - A8 | J600.43 |
| B1 - B4 | HUB75.1 - HUB75.4 (CLK) |
| B5 - B8 | HUB75.1 - HUB75.4 (STB) |

| Buffer 5 | |
|---------|---------|
| A1 - A4 | J600.40 |
| A5 - A8 | J600.39 |
| B1 - B4 | HUB75.1 - HUB75.8 (C; bridged in pairs of 2) |
| B5 - B8 | HUB75.1 - HUB75.8 (D; bridged in pairs of 2) |

HUB75 connectors
----------------

```
  _________
 |  R1 G1  |
 |  B1 GND |
 |  R2 G2  |
  | B2 GND |
  |  A B   |
 |   C D   |
 | CLK STB |
 |  OE GND |
  ---------
```

Final pinout
------------

| Signal | Breakout pins |
|--------|---------------|
| GND    | J600.1,3,5,46,48,50 |
| GND    | J601.1,3,5,46,48,50 |
| VCC    | J600.2,4,47,49 |
| VCC    | J601.2,4,49 |
| HUB75.*.OE | J601.6 (via buffer 3) |
| HUB75.*.A  | J601.42 (via buffer 1) |
| HUB75.*.B  | J601.41 (via buffer 1) |
| HUB75.*.C  | J600.40 (via buffer 5) |
| HUB75.*.D  | J600.39 (via buffer 5) |
| HUB75.{1..4}.CLK | J600.44 (via buffer 4) |
| HUB75.{5..8}.CLK | J601.44 (via buffer 2) |
| HUB75.{1..4}.STB | J600.43 (via buffer 4) |
| HUB75.{5..8}.STB | J601.43 (via buffer 2) |
| HUB75.8.R1 | J601.38 |
| HUB75.8.G1 | J601.37 |
| HUB75.8.B1 | J601.36 |
| HUB75.8.R2 | J601.34 |
| HUB75.8.G2 | J601.33 |
| HUB75.8.B2 | J601.32 |
| HUB75.7.R1 | J601.30 |
| HUB75.7.G1 | J601.29 |
| HUB75.7.B1 | J601.28 |
| HUB75.7.R2 | J601.26 |
| HUB75.7.G2 | J601.25 |
| HUB75.7.B2 | J601.24 |
| HUB75.6.R1 | J601.22 |
| HUB75.6.G1 | J601.21 |
| HUB75.6.B1 | J601.20 |
| HUB75.6.R2 | J601.18 |
| HUB75.6.G2 | J601.17 |
| HUB75.6.B2 | J601.16 |
| HUB75.5.R1 | J601.14 |
| HUB75.5.G1 | J601.13 |
| HUB75.5.B1 | J601.12 |
| HUB75.5.R2 | J601.10 |
| HUB75.5.G2 | J601.9 |
| HUB75.5.B2 | J601.8 |
| HUB75.4.R1 | J600.38 |
| HUB75.4.G1 | J600.37 |
| HUB75.4.B1 | J600.36 |
| HUB75.4.R2 | J600.34 |
| HUB75.4.G2 | J600.33 |
| HUB75.4.B2 | J600.32 |
| HUB75.3.R1 | J600.30 |
| HUB75.3.G1 | J600.29 |
| HUB75.3.B1 | J600.28 |
| HUB75.3.R2 | J600.26 |
| HUB75.3.G2 | J600.25 |
| HUB75.3.B2 | J600.24 |
| HUB75.2.R1 | J600.22 |
| HUB75.2.G1 | J600.21 |
| HUB75.2.B1 | J600.20 |
| HUB75.2.R2 | J600.18 |
| HUB75.2.G2 | J600.17 |
| HUB75.2.B2 | J600.16 |
| HUB75.1.R1 | J600.14 |
| HUB75.1.G1 | J600.13 |
| HUB75.1.B1 | J600.12 |
| HUB75.1.R2 | J600.10 |
| HUB75.1.G2 | J600.9 |
| HUB75.1.B2 | J600.8 |
