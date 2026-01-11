# micropython-calc-programs
Some little Micropython programs I've written for Numworks, HP,  and
TI calculators in MicroPython.

These may or may not be useful to people, and your mileage may vary.
They're experiments to compare programming different calculators that
I have, with the hopes fo getting a better understanding of the
programming environments for each.

Not all programs may be tested on all calculators.

Targets include the HP Prime, Numworks, and TI Nspire machines.

## baseconverter.py
Converts numbers to binary, octal, hexadecimal, and decimal.

Enter  `number current base`, , where the base can be one of
`2`, `8`, `10`, `16`

like this:

```
100 16

Binary:		0b10000000
Octal: 		0o400
Decimal: 	256
Hexadecimal: 	0x100
```

So far, tested on the Numworks calculator.
