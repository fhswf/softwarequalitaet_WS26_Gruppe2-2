# NOVE
# TNSS
"""
TDD-Template für FizzBuzz Kata
==============================

TODO: Team A - Entwickelt FizzBuzz mit TDD!

FizzBuzz-Regeln:
- Zahl durch 3 teilbar → "Fizz"  
- Zahl durch 5 teilbar → "Buzz"
- Zahl durch 3 UND 5 teilbar → "FizzBuzz"
- Sonst → Zahl als String

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!

Autorschaft dokumentieren: Wer hat welchen TDD-Schritt gemacht?
"""

import pytest
from ..Code.fizzbuzz_kata import fizzbuzz


class TestFizzBuzzTDD:
    """
    TODO: Team A - Entwickelt FizzBuzz mit TDD!

    Tipps:
    - Startet mit dem einfachsten Test
    - Schreibt minimalen Code zum Bestehen
    - Refaktoriert wenn nötig
    - Ein Test nach dem anderen!
    """

    # TDD-Zyklus 1: RED von TNSS
    def test_one_returns_its_string_representation(self):
        assert fizzbuzz(1) == "1"

    # TDD-Zyklus 1: GREEN von TNSS
    # Die minimale Implementierung fuer diesen Test ist str(n).

    # TDD-Zyklus 2: RED von NOVE
    def test_three_returns_fizz(self):
        assert fizzbuzz(3) == "Fizz"

    # TDD-Zyklus 2: GREEN von TNSS
    # Die minimale Implementierung prueft n % 3 == 0.

    # TDD-Zyklus 3: RED von NOVE
    def test_five_returns_buzz(self):
        assert fizzbuzz(5) == "Buzz"

    # TDD-Zyklus 3: GREEN von TNSS
    # Die minimale Implementierung prueft n % 5 == 0.

    # TDD-Zyklus 4: RED von NOVE
    def test_fifteen_returns_fizzbuzz(self):
        assert fizzbuzz(15) == "FizzBuzz"

    # TDD-Zyklus 5: RED/GREEN von NOVE
    def test_two_returns_its_string_representation(self):
        assert fizzbuzz(2) == "2"


class TestFizzBuzzErweitert:
    """
    TODO: Team A - Erweiterte Tests, wenn Basis funktioniert
    """

    # TDD-Zyklus 5: REFACTOR von NOVE & TNSS
    @pytest.mark.parametrize(
        ("number", "expected"),
        [
            (6, "Fizz"),
            (10, "Buzz"),
            (30, "FizzBuzz"),
            (7, "7"),
        ],
    )
    def test_additional_fizzbuzz_cases(self, number, expected):
        assert fizzbuzz(number) == expected


# TODO: Team A - Optional: TDD-Protokoll
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
"""
