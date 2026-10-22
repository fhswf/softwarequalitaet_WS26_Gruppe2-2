# RTRE
# NOVE

from decimal import Decimal
from .interfaces import KontoInterface


class Konto(KontoInterface):
    """
    TODO: Implementieren Sie diese Klasse

    Regeln:
    - ID wird bei Erstellung mitgegeben (numerisch, darf nicht leer sein)
    - Konto darf nicht überzogen werden (Saldo < 0)
    - Fehler bei inkorrekter Nutzung werfen
    """

    def __init__(self, konto_id: int, saldo: Decimal = Decimal('0.00')):

        # Saldo prüfen, ob er negativ ist
        if saldo < 0:
            raise ValueError("Saldo darf nicht negativ sein")

        # Konto-ID prüfen, ob sie auch numerisch und nicht leer ist
        if konto_id is None or not isinstance(konto_id, int):
            raise ValueError("Konto-ID muss eine Zahl sein")

        # Initialisierung der Klassenattribute
        self.konto_id = konto_id
        self.saldo = saldo

    # Funktion Konto-ID ausgeben
    @property
    def konto_id(self) -> int:
        return self._konto_id

    # Funktion Saldo ausgeben
    @property
    def saldo(self) -> Decimal:
        return self._saldo

    # Funktion Einzahlen eines Betrags auf Konto
    def einzahlen(self, betrag: Decimal) -> None:
        if betrag <= 0:
            raise ValueError("Einzuzahlender Betrag muss positiv sein")
        self.saldo += betrag

    # Funktion Auszahlen eines Betrags vom Konto
    def auszahlen(self, betrag: Decimal) -> None:
        if betrag <= 0:
            raise ValueError("Abhebbarer Betrag muss positiv sein")
        if self.saldo < betrag:
            raise ValueError("Konto nicht ausreichend gedeckt")
        self.saldo -= betrag
