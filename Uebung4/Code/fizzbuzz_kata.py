"""
TDD Kata: FizzBuzz
Implementieren Sie die FizzBuzz-Funktion mit Test-Driven Development

Regeln:
1. Schreiben Sie zuerst einen Test (der fehlschlägt)
2. Schreiben Sie minimal nötigen Code, um den Test zu bestehen
3. Refactoring (Code verbessern ohne Funktionalität zu ändern)
4. Wiederholen Sie 1-3

FizzBuzz Regeln:
- Zahl durch 3 teilbar -> "Fizz"
- Zahl durch 5 teilbar -> "Buzz"  
- Zahl durch 3 UND 5 teilbar -> "FizzBuzz"
- Sonst -> Zahl als String
"""


def fizzbuzz(n: int) -> str:
    """
    Liefert die FizzBuzz-Darstellung einer positiven Ganzzahl.

    Args:
        n: Eine positive Ganzzahl

    Returns:
        "Fizz", "Buzz", "FizzBuzz" oder die Zahl als String
    """
    # TDD-Zyklus 4: REFACTOR von NOVE
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"

    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        # TDD-Zyklus 3: GREEN von TNSS
        return "Buzz"

    return str(n)
