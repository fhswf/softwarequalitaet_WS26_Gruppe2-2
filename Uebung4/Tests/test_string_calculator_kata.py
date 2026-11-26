#implementiert von: JYBS, RTRE

"""
TDD-Template für String Calculator Kata
=======================================

TODO: Team B - Entwickelt String Calculator mit TDD!

String Calculator-Regeln:
- Leerer String → 0
- Ein String mit einer Zahl → diese Zahl
- Zwei Zahlen mit Komma getrennt → Summe
- Beliebig viele Zahlen → Summe aller
- Neue Zeilen als Trenner erlaubt: "1\n2,3" → 6
- Optional: Custom Delimiter: "//;\n1;2" → 3

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!

Autorschaft dokumentieren: Wer hat welchen TDD-Schritt gemacht?
"""

import pytest

# TODO: Team B - Import nach erster Implementierung:
from ..Code.string_calculator_kata import add


class TestStringCalculatorTDD:
    """
    TODO: Team B - Entwickelt String Calculator mit TDD!

    Tipps:
    - Startet mit dem einfachsten Test
    - Schreibt minimalen Code zum Bestehen
    - Refaktoriert wenn nötig
    - Ein Test nach dem anderen!
    """

    #TDD-Zyklus 1: RED von JYBS
    #TDD-Zyklus 1: GREEN von RTRE
    def test_empty_string_returns_zero(self):
        assert add("") == 0

    #TDD-Zyklus 2: RED von RTRE
    #TDD-Zyklus 2: GREEN von JYBS
    def test_string_with_number_returns_number(self):
        assert add("1") == 1

    #TDD-Zyklus 3: RED von JYBS
    #TDD-Zyklus 3: GREEN von RTRE
    def test_two_numbers_with_comma_are_added(self):
        assert add("1,2") == 3
        assert add("5,10") == 15
    
    #TDD-Zyklus 4: RED von RTRE
    #TDD-Zyklus 4: GREEN von JYBS
    def test_numbers_are_added(self):
        assert add("1,2,3,4,5") == 15
        assert add ("3,7,10") == 20

    #TDD-Zyklus 5: RED von JYBS
    #TDD-Zyklus 5: GREEN von RTRE
    def test_new_line_allowed(self):
        assert add("1\n2") == 3
        assert add("10\n5") == 15

    #TDD-Zyklus 6: RED von RTRE
    #TDD-Zyklus 6: GREEN von JYBS
    def test_custom_delimiter(self):
        assert add("//;\n1;2") == 3
        assert add(";\n//4;,5/;\n") ==9




class TestStringCalculatorErweitert:
    """
    TODO: Team B - Erweiterte Tests, wenn Basis funktioniert
    """

    def test_placeholder_extended_tests(self):
        """
        TODO: Team B - Entwickelt weitere Tests für String Calculator

        Ideen:
        - Custom Delimiters testen
        - Edge Cases (negative Zahlen, große Zahlen)
        - Parametrisierte Tests (@pytest.mark.parametrize)
        - Fehlerbehandlung (ungültige Eingaben)
        """
        # TODO: Erweiterte Tests hier
        assert True, "TODO: Erweiterte String Calculator-Tests implementieren"


# TODO: Team B - Optional: TDD-Protokoll
"""
TDD-Fortschritt dokumentieren:

Test 1: [Was getestet] - Autor: [Name] - Zeit: [Zeit]
Implementation 1: [Minimale Lösung] - Zeit: [Zeit]

Test 2: [Was getestet] - Autor: [Name] - Zeit: [Zeit]  
Refactoring: [Was geändert] - Zeit: [Zeit]

[Weiter dokumentieren...]

Erkenntnisse:
- Was war überraschend?
- Wo musstet ihr refaktorieren?
- Welche Tests brachten neue Herausforderungen?
- Unterschiede zu FizzBuzz?
"""
