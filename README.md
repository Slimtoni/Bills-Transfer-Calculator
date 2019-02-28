# Bills-Transfer-Calculator

## Input

### Rechnungen (bills.csv)

```
5.5;Rechnung Jason;30.03.18
200;Rechnung Welcome Party;30.04.18
240.32;Rechnung IT;30.03.13
7.4;Rechnung 1;30.03.18
30;Rechnung 2;30.03.18
27.32;Rechnung 3;30.03.18
```
### Ueberweisungen (transfer.csv)

```
275.82;30.04.18
234.73;30.04.18
37.4;30.04.18
```

## Ausführung

```
.\Bills-Transfer-Calculator.exe
```

## Output

```
Rechnungen: 
Rechnung Jason: 5.5 vom 30.03.18
Rechnung Welcome Party: 200.0 vom 30.04.18
Rechnung IT: 240.32 vom 30.03.13
Rechnung 1: 7.4 vom 30.03.18
Rechnung 2: 30.0 vom 30.03.18
Rechnung 3: 27.32 vom 30.03.18

Überweisungen: 
275.82 vom 30.04.18
234.73 vom 30.04.18
37.4 vom 30.04.18

Kalkulation: ----------------------------------------

Überweisung: 275.82 vom 30.04.18
gefundener, passender Betrag: 275.82
passende Rechnungen: 
Rechnung Jason: 5.5 vom 30.03.18
Rechnung IT: 240.32 vom 30.03.13
Rechnung 2: 30.0 vom 30.03.18
-------------------------------------------------------------------------

Überweisung: 234.73 vom 30.04.18
gefundener, passender Betrag: 234.72
passende Rechnungen: 
Rechnung Welcome Party: 200.0 vom 30.04.18
Rechnung 1: 7.4 vom 30.03.18
Rechnung 3: 27.32 vom 30.03.18
-------------------------------------------------------------------------

Überweisung: 37.4 vom 30.04.18
gefundener, passender Betrag: 37.4
passende Rechnungen: 
Rechnung 1: 7.4 vom 30.03.18
Rechnung 2: 30.0 vom 30.03.18
-------------------------------------------------------------------------
```