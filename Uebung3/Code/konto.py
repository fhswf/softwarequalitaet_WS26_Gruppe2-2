# RTRE
# NOVE

from decimal import Decimal, InvalidOperation
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
        if not isinstance(konto_id, int) or konto_id <= 0:
            raise ValueError("Konto-ID muss eine positive Zahl sein")

        try:
            saldo = Decimal(str(saldo))
        except (InvalidOperation, TypeError, ValueError) as error:
            raise ValueError("Saldo muss eine gültige Zahl sein") from error

        if saldo < 0:
            raise ValueError("Saldo darf nicht negativ sein")

        self._konto_id = konto_id
        self._saldo = saldo

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
        self._saldo += betrag

    # Funktion Auszahlen eines Betrags vom Konto
    def auszahlen(self, betrag: Decimal) -> None:
        if betrag <= 0:
            raise ValueError("Abhebbarer Betrag muss positiv sein")
        if self.saldo < betrag:
            raise ValueError("Konto nicht ausreichend gedeckt")
        self._saldo -= betrag
