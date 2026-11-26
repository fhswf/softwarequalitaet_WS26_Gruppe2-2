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
    #TDD-Zyklus 7: RED von JYBS
    #TDD-Zyklus 7: GREEN von RTRE
    def test_negative_numbers_are_returned(self):
        assert add("-5") == -5
        assert add("/;-6,//") == -6

    #TDD-Zyklus 8: RED & GREEN von RTRE (keine Codeanpassung nötig)
    def test_big_numbers_are_returned(self):
        assert add("1234567890") == 1234567890

    #TDD-Zyklus 9: RED von JYBS
    #TDD-Zyklus 9: GREEN von RTRE
    def test_invalid_entries(self):
        assert add("?") == "Ungültige Eingabe."
        assert add("Buchstaben")
        assert add("+")
        
        """
        TODO: Team B - Entwickelt weitere Tests für String Calculator

        Ideen:
        - Custom Delimiters testen
        - Edge Cases (negative Zahlen, große Zahlen)
        - Parametrisierte Tests (@pytest.mark.parametrize)
        - Fehlerbehandlung (ungültige Eingaben)
        """

# TODO: Team B - Optional: TDD-Protokoll
"""
TDD-Fortschritt dokumentieren:

Test 1: [leerer String gibt 0 zurück] - Autor: [JYBS]
Implementation 1: [if numbers == "": return 0] - Autor: [RTRE]

Test 2: [String mit Nummer gibt diese Nummer zurück] - Autor: [RTRE] 
Implementation 2: [return int(numbers)] - Autor: [JYBS]

Test 3: [Zwei durch Komma getrennte Zahlen werden addiert] - Autor: [JYBS]  
Implementation 3: [ if "," in numbers:
                    nums = numbers.split(",")
                    return (int(nums[0])+int(nums[1])) ] - Autor: [RTRE]

Test 4: [Mehrere durch Komma getrennte Zahlen werden addiert] - Autor: [RTRE] 
Implementation 4: [ if "," in numbers:
                    nums = numbers.split(",")
                    result = 0
                    for num in nums:
                        result += int(num)
                    return result ] - Autor: [JYBS]

Test 5: [Neue Zeilen ("\n") als Trenner erlaubt] - Autor: [JYBS]  
Implementation 5: [numbers = numbers.replace("\n", ",")] - Autor: [RTRE]

Test 6: [Custom Delimiter: auch "/" und ";" erlaubt, auch direkt hintereinander] - Autor: [RTRE] 
Implementation 6: [ numbers = numbers.replace("/",",")
                    numbers = numbers.replace(";",",")
                    ...
                    for num in nums:
                        if num == "":
                            num = 0
                        result += int(num) ] - Autor: [JYBS]

Test 7: [Negative Zahlen werden zurückgegeben] - Autor: [JYBS]
Implementation 7: [ if "," in numbers:
                        nums = numbers.split(",")
                        result = 0
                        index = 0
                        for num in nums:
                            if num == "": num = 0
                            if num == "-":
                                num = 0
                                nums[index+1] = nums[index+1]*(-1)
                            result += int(num)
                            index += 1
                        return result ]

Test 8: [Große Zahlen werden zurückgegeben] - Autor: [RTRE]
Implementation 8: [keine Änderung nötig, Code funktioniert direkt korrekt]

Test 9: [Ungültige Eingaben] - Autor: [JYBS]
Implementation: [for char in numbers:
                    if not (char.isdigit() or (char == "-") or (char == ",")):
                        return "Ungültige Eingabe."] - Autor:  [RTRE]

Erkenntnisse:
- Was war überraschend?
- Wo musstet ihr refaktorieren?
- Welche Tests brachten neue Herausforderungen?
- Unterschiede zu FizzBuzz?
"""
