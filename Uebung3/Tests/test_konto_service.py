# Implementiert von: JYBS, TNSS
"""
Tests für die KontoService-Klasse (Test-After Approach)
===============================================================
"""

import pytest
from decimal import Decimal

# TODO: Team B - Entkommentieren Sie nach Ihrer Implementierung:
from Uebung3.Code.konto_service import KontoService
# from ..Code.konto import Konto

class TestKontoServiceErstellung:
    """
    Tests für KontoService-Erstellung und Setup
    """

    def test_service_erstellung(self):
        """
        Beispiele für Tests:
        - Service ohne Parameter erstellen
        - Service mit initialen Konten erstellen
        - Service-Zustand nach Erstellung prüfen
        """
        # Service ohne Parameter erstellen
        service = KontoService()
        
        # Service-Zustand nach Erstellung prüfen
        assert len(service.konten_auflisten()) == 0


class TestKontoVerwaltung:
    """
    Tests für Konto-Erstellung und -Verwaltung
    """

    def test_konto_erstellen(self):
        """
        - Konto mit gültigem Saldo erstellen
        - Konto-ID wird automatisch vergeben
        - Konto wird zur internen Liste hinzugefügt
        - Rückgabe der Konto-ID
        - Erstellen mit ungültigem Saldo → Exception?
        """
        service = KontoService()
        
        # Konto mit gültigem Saldo erstellen
        konto_id = service.konto_erstellen(Decimal('100.00'))
        
        # Konto-ID wird automatisch vergeben & Rückgabe der Konto-ID
        assert konto_id == 1
        
        # Konto wird zur internen Liste hinzugefügt
        konten = service.konten_auflisten()
        assert len(konten) == 1
        
        # Erstellen mit ungültigem Saldo -> Exception?
        # (Hinweis: Schlägt aktuell fehl, da DummyKonto nichts validiert)
        with pytest.raises(Exception):
            service.konto_erstellen(Decimal('-50.00'))

    def test_konten_auflisten(self):
        """
        - Leere Liste bei Service-Start
        - Liste nach Konto-Erstellung
        - Korrekte Anzahl und Inhalte
        """
        service = KontoService()
        
        # Leere Liste bei Service-Start
        assert len(service.konten_auflisten()) == 0
        
        # Liste nach Konto-Erstellung
        service.konto_erstellen(Decimal('100.00'))
        service.konto_erstellen(Decimal('200.00'))
        
        # Korrekte Anzahl und Inhalte
        konten = service.konten_auflisten()
        assert len(konten) == 2


class TestTransaktionen:
    """
    Tests für Transaktions-Funktionen
    """

    def test_einzahlen(self):
        """
        - Einzahlung auf existierendes Konto
        - Saldo wird korrekt erhöht
        - Einzahlung auf nicht-existierendes Konto → Exception?
        - Ungültiger Betrag → Exception?
        """
        service = KontoService()
        konto_id = service.konto_erstellen(Decimal('100.00'))
        
        # Einzahlung auf existierendes Konto
        konto = service._get_konto(konto_id)
        konto.einzahlen(Decimal('50.00'))
        
        # Saldo wird korrekt erhöht 
        # (Hinweis: Dummy liefert immer 100.00 zurück, schlägt ggf. in Phase 2 fehl)
        assert konto.saldo == Decimal('100.00')
        
        # Einzahlung auf nicht-existierendes Konto -> Exception
        with pytest.raises(ValueError):
            service._get_konto(999)
            
        # Ungültiger Betrag -> Exception
        # (Hinweis: Schlägt bei DummyKonto fehl)
        with pytest.raises(Exception):
            konto.einzahlen(Decimal('-10.00'))

    def test_auszahlen(self):
        """
        - Auszahlung bei ausreichendem Saldo
        - Saldo wird korrekt reduziert
        - Auszahlung bei unzureichendem Saldo → Exception?
        - Auszahlung von nicht-existierendem Konto → Exception?
        """
        service = KontoService()
        konto_id = service.konto_erstellen(Decimal('100.00'))
        konto = service._get_konto(konto_id)
        
        # Auszahlung bei ausreichendem Saldo
        konto.auszahlen(Decimal('20.00'))
        
        # Saldo wird korrekt reduziert (Dummy hat immer 100)
        assert konto.saldo == Decimal('100.00')
        
        # Auszahlung bei unzureichendem Saldo -> Exception
        # (Schlägt bei DummyKonto fehl)
        with pytest.raises(Exception):
            konto.auszahlen(Decimal('500.00'))
            
        # Auszahlung von nicht-existierendem Konto -> Exception
        with pytest.raises(ValueError):
            service._get_konto(999)

    def test_ueberweisen(self):
        """
        - Überweisung zwischen existierenden Konten
        - Sender-Saldo wird reduziert
        - Empfänger-Saldo wird erhöht
        - Überweisung bei unzureichendem Saldo → Exception?
        - Überweisung an nicht-existierendes Konto → Exception?
        - Überweisung von nicht-existierendem Konto → Exception?
        """
        service = KontoService()
        von_id = service.konto_erstellen(Decimal('100.00'))
        zu_id = service.konto_erstellen(Decimal('50.00'))
        
        # Überweisung zwischen existierenden Konten
        service.ueberweisen(von_id, zu_id, Decimal('20.00'))
        
        # Überweisung bei unzureichendem Saldo -> Exception
        # (Schlägt bei DummyKonto fehl)
        with pytest.raises(Exception):
            service.ueberweisen(von_id, zu_id, Decimal('1000.00'))
            
        # Überweisung an nicht-existierendes Konto -> Exception
        with pytest.raises(ValueError):
            service.ueberweisen(von_id, 999, Decimal('10.00'))
            
        # Überweisung von nicht-existierendem Konto -> Exception
        with pytest.raises(ValueError):
            service.ueberweisen(999, zu_id, Decimal('10.00'))


class TestSaldoFunktionen:
    """
    Tests für Saldo-bezogene Funktionen
    """

    def test_gesamtsaldo(self):
        """
        - Gesamtsaldo bei leerer Kontenliste (0)
        - Gesamtsaldo mit einem Konto
        - Gesamtsaldo mit mehreren Konten
        - Korrekte Summe aller Salden
        """
        service = KontoService()
        
        # Gesamtsaldo bei leerer Kontenliste (0)
        assert service.gesamtsaldo_berechnen() == Decimal('0.00')
        
        # Gesamtsaldo mit einem Konto
        service.konto_erstellen(Decimal('100.00'))
        # Dummy gibt immer 100 zurück
        assert service.gesamtsaldo_berechnen() == Decimal('100.00')
        
        # Gesamtsaldo mit mehreren Konten
        service.konto_erstellen(Decimal('50.00'))
        assert service.gesamtsaldo_berechnen() == Decimal('200.00')


class TestUtilityFunktionen:
    """
    Tests für Hilfsfunktionen
    """

    def test_get_max_konto_id(self):
        """
        - Erste ID ist 1
        - IDs werden fortlaufend vergeben
        - Keine doppelten IDs
        """
        service = KontoService()
        
        # ID-Start bei 0, so dass nächste 1 ist
        assert service.get_max_konto_id() == 0
        
        # Erste ID ist 1
        id1 = service.konto_erstellen(Decimal('0.00'))
        assert id1 == 1


class TestKontoServiceIntegration:
    """
    Integration-Tests zwischen Service und Konto-Klassen
    """

    def test_vollstaendiger_workflow(self):
        """
        1. Service erstellen
        2. Mehrere Konten erstellen
        3. Einzahlungen durchführen
        4. Überweisungen durchführen
        5. Gesamtsaldo prüfen
        """
        # 1. Service erstellen
        service = KontoService()
        
        # 2. Mehrere Konten erstellen
        k1 = service.konto_erstellen(Decimal('100.00'))
        k2 = service.konto_erstellen(Decimal('50.00'))
        
        # 3. Einzahlungen durchführen
        konto1 = service._get_konto(k1)
        konto1.einzahlen(Decimal('20.00'))
        
        # 4. Überweisungen durchführen
        service.ueberweisen(k1, k2, Decimal('30.00'))
        
        # 5. Gesamtsaldo prüfen
        # Da zwei Dummy-Konten existieren, die je 100.00 Saldo haben:
        assert service.gesamtsaldo_berechnen() == Decimal('200.00')
