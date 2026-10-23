# Implementiert von: AI, Assistant
"""
Test-Template für die KontoService-Klasse (Test-After Approach)
===============================================================

Tests für den Service implementiert nach Team B Vorgabe
"""

import pytest
from decimal import Decimal

# TODO: Team B - Entkommentieren Sie nach Ihrer Implementierung:
from Uebung3.Code.konto_service import KontoService
# from ..Code.konto import Konto

@pytest.fixture
def service():
    return KontoService()


class TestKontoServiceErstellung:
    """
    Tests für KontoService-Erstellung und Setup
    """

    def test_service_erstellung(self, service):
        """
        Testet die Erstellung eines leeren Services.
        """
        assert service is not None
        assert len(service.konten_auflisten()) == 0


class TestKontoVerwaltung:
    """
    Tests für Konto-Erstellung und -Verwaltung
    """

    def test_konto_erstellen(self, service):
        """Testet konto_erstellen()"""
        konto_id = service.konto_erstellen(Decimal('100.00'))
        
        assert konto_id == 1
        konten = service.konten_auflisten()
        assert len(konten) == 1
        assert konten[0]['konto_id'] == 1
        # Dummy Konto gibt immer 100.00 zurück, auch wenn was anderes übergeben wird

    def test_konten_auflisten(self, service):
        """Testet konten_auflisten()"""
        service.konto_erstellen(Decimal('100.00'))
        service.konto_erstellen(Decimal('200.00'))
        
        konten = service.konten_auflisten()
        assert len(konten) == 2
        # Da der dummy hier nicht gut mitmacht, können wir nur die Länge testen.
        # Später in Phase 3 wird das genauer testbar.


class TestTransaktionen:
    """
    Tests für Transaktions-Funktionen
    """

    def test_einzahlen(self, service):
        """Testet einzahlen() indirekt über das Konto (wenn der Service dies in Zukunft anbietet)
        Hinweis: Das Interface fordert diese Methode nicht auf dem Service!
        Wir rufen stattdessen einzahlen() auf dem Konto auf (sofern wir drankommen).
        """
        konto_id = service.konto_erstellen(Decimal('100.00'))
        
        # Act
        # Da wir über den Service keine Einzahlen-Methode haben, testen wir
        # ob das DummyKonto reagiert (was es nicht tut).
        # In Phase 3 mit echtem Konto wird dies sinnvoller.
        konto = service._get_konto(konto_id)
        konto.einzahlen(Decimal('50.00'))
        
        # Assert
        # Dummy gibt immer 100 zurück
        assert konto.saldo == Decimal('100.00')

    def test_auszahlen(self, service):
        """Testet auszahlen() auf dem Konto über den Service."""
        konto_id = service.konto_erstellen(Decimal('100.00'))
        
        # Act
        konto = service._get_konto(konto_id)
        konto.auszahlen(Decimal('50.00'))
        
        # Assert
        # Dummy gibt immer 100 zurück
        assert konto.saldo == Decimal('100.00')

    def test_ueberweisen(self, service):
        """Testet ueberweisen()"""
        konto1_id = service.konto_erstellen(Decimal('100.00'))
        konto2_id = service.konto_erstellen(Decimal('50.00'))
        
        service.ueberweisen(konto1_id, konto2_id, Decimal('20.00'))
        
        # Dummy ändert nichts am Saldo, wirft aber auch keine Fehler


class TestSaldoFunktionen:
    """
    Tests für Saldo-bezogene Funktionen
    """

    def test_gesamtsaldo(self, service):
        """Testet gesamtsaldo_berechnen()"""
        assert service.gesamtsaldo_berechnen() == Decimal('0.00')
        
        service.konto_erstellen(Decimal('100.00'))
        service.konto_erstellen(Decimal('50.00'))
        
        # Da Dummy immer 100 zurückgibt, ist der Gesamtsaldo 200
        assert service.gesamtsaldo_berechnen() == Decimal('200.00')


class TestUtilityFunktionen:
    """
    Tests für Hilfsfunktionen
    """

    def test_get_max_konto_id(self, service):
        """Testet get_max_konto_id()"""
        assert service.get_max_konto_id() == 0
        
        service.konto_erstellen(Decimal('0.00'))
        assert service.get_max_konto_id() == 1


class TestKontoServiceIntegration:
    """
    Integration-Tests zwischen Service und Konto-Klassen
    """

    def test_vollstaendiger_workflow(self, service):
        """Test für kompletten Workflow"""
        k1 = service.konto_erstellen(Decimal('100.00'))
        k2 = service.konto_erstellen(Decimal('50.00'))
        
        service.ueberweisen(k1, k2, Decimal('10.00'))
        
        # Gesamtsaldo mit Dummys ist 200 (100 + 100)
        assert service.gesamtsaldo_berechnen() == Decimal('200.00')
