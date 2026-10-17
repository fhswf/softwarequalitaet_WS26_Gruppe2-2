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

    @property
    def konto_id(self) -> int:
        # TODO: Implementierung
        pass

    @property
    def saldo(self) -> Decimal:
        # TODO: Implementierung
        pass

    def einzahlen(self, betrag: Decimal) -> None:
        # TODO: Implementierung
        pass

    def auszahlen(self, betrag: Decimal) -> None:
        # TODO: Implementierung
        pass
