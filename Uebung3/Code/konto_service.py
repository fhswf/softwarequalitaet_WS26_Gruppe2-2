# Implementiert von: TNSS, JYBS
"""
KontoService-Klasse basierend auf dem KontoServiceInterface
"""

from decimal import Decimal
from typing import List, Dict
from .interfaces import KontoServiceInterface, KontoInterface


# TODO: Team B - Später ersetzt ihr diesen Import durch Team A's Implementation:
from .konto import Konto


class KontoService(KontoServiceInterface):
    """
    Implementierung des KontoService.
    Verwaltet Konten, validiert Benutzereingaben und führt bankweite Operationen durch.
    """

    def __init__(self):
        self._konten: List[KontoInterface] = []

    def _create_konto(self, konto_id: int, saldo: Decimal) -> KontoInterface:
        """
        Factory-Methode für Konto-Erstellung - ermöglicht parallele Entwicklung!

        TODO: Team B - STARTEN SIE HIER! Diese Methode gibt Ihnen EXTREM EINFACHE Dummy-Objekte.

        JETZT: Verwenden Sie diese Dummy-Implementation für Ihre Service-Entwicklung
        SPÄTER: Ersetzen Sie durch `return Konto(konto_id, saldo)` wenn Team A fertig ist

        WICHTIG: Diese Dummy-Implementation macht fast NICHTS - das ist Absicht!
        Bei der Integration werden Sie Probleme entdecken, die Sie dann gemeinsam lösen.
        """

        # EXTREM EINFACHE DUMMY-IMPLEMENTATION für Team B:
        # Macht fast nichts, gibt nur konstante Werte zurück!
        #class DummyKonto(KontoInterface):
            #def __init__(self, konto_id: int, saldo: Decimal):
                # Speichert die Werte, aber macht keine Validierung!
                #pass

            #@property
            #def konto_id(self) -> int:
                #return 1  # ← Immer konstant 1!

            #@property
            #def saldo(self) -> Decimal:
                #return Decimal("100.00")  # ← Immer konstant 100!

            #def einzahlen(self, betrag: Decimal) -> None:
                #pass  # ← Macht nichts!

            #def auszahlen(self, betrag: Decimal) -> None:
                #pass  # ← Macht nichts, wirft keine Fehler!

        #return DummyKonto(konto_id, saldo)

        # TODO: Team B - Später ersetzen Sie die obige Dummy-Implementation durch:
        return Konto(konto_id, saldo)

    def konten_auflisten(self) -> List[Dict]:
        return [{"konto_id": k.konto_id, "saldo": k.saldo} for k in self._konten]

    def konto_erstellen(self, saldo: Decimal = Decimal('0.00')) -> int:
        konto_id = self.get_max_konto_id() + 1
        konto = self._create_konto(konto_id, saldo)
        self._konten.append(konto)
        return konto_id

    def _get_konto(self, konto_id: int) -> KontoInterface:
        """Hilfsmethode zum Suchen eines Kontos anhand der ID."""
        for konto in self._konten:
            if konto.konto_id == konto_id:
                return konto
        raise ValueError(f"Konto mit der ID {konto_id} konnte nicht gefunden werden.")

    def ueberweisen(self, von_konto_id: int, zu_konto_id: int, betrag: Decimal) -> None:
        if von_konto_id == zu_konto_id:
            raise ValueError("Quell- und Zielkonto dürfen nicht identisch sein.")
        if betrag <= 0:
            raise ValueError("Der Betrag muss positiv sein.")
            
        von_konto = self._get_konto(von_konto_id)
        zu_konto = self._get_konto(zu_konto_id)
        
        von_konto.auszahlen(betrag)
        zu_konto.einzahlen(betrag)

    def einziehen(self, von_konto_id: int, zu_konto_id: int, betrag: Decimal) -> None:
        if von_konto_id == zu_konto_id:
            raise ValueError("Quell- und Zielkonto dürfen nicht identisch sein.")
        if betrag <= 0:
            raise ValueError("Der Betrag muss positiv sein.")
            
        von_konto = self._get_konto(von_konto_id)
        zu_konto = self._get_konto(zu_konto_id)
        
        von_konto.auszahlen(betrag)
        zu_konto.einzahlen(betrag)

    def get_max_konto_id(self) -> int:
        if not self._konten:
            return 0
        return max(konto.konto_id for konto in self._konten)

    def gesamtsaldo_berechnen(self) -> Decimal:
        return sum((konto.saldo for konto in self._konten), Decimal('0.00'))
