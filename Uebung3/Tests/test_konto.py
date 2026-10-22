# RTRE
# NOVE

"""
Test-Template für die Konto-Klasse (Test-After Approach)
========================================================

TODO: Team A - Implementieren Sie hier Ihre Tests NACH der Konto-Implementierung!

Arbeitsablauf:
1. Implementieren Sie zuerst die Konto-Klasse in Code/konto.py
2. Schreiben Sie dann hier umfassende Tests für Ihren Code
3. Testen Sie normale Fälle UND Grenzfälle
4. Dokumentieren Sie Ihre Autorschaft in den Tests

Tipps für gute Tests:
- Verwenden Sie aussagekräftige Test-Namen
- Testen Sie eine Sache pro Test
- Nutzen Sie pytest.raises() für Exception-Tests
- Denken Sie an Grenzwerte (0, negative Zahlen)
"""

import pytest
from decimal import Decimal

# TODO: Team A - Entkommentiert nach eurer Implementierung:
from .konto import Konto


class TestKontoErstellung:
    """
    Tests für die Konto-Erstellung
    TODO: Team A - Implementieren Sie Tests für den Konstruktor
    """

    def test_placeholder_konto_erstellung(self):

        # Konto mit gültiger ID und positivem Saldo erstellen
        def test_konto_erstellen_mit_gid_und_psaldo(self):
            Konto = Konto(1000, 50)
            assert konto.kontoid == 1
            assert konto.saldo == Decimal("50.00")

        # Konto mit gültiger ID und Saldo 0 erstellen
        def test_konto_erstellen_mit_gid_und_nullsaldo(self):
            Konto = Konto(1001, 0)
            assert konto.kontoid == 1
            assert konto.saldo == Decimal("0.00")

        # Konto mit ungültiger ID (negativ, 0, String) mit pytest
        def test_konto_erstellen_mit_ungueltiger_id(self):
            with pytest.raises(ValueError):
                Konto(-1, 50)
            with pytest.raises(ValueError):
                Konto(0, 50)
            with pytest.raises(ValueError):
                Konto("abc", 50)

         # Konto mit ungültigem Saldo (negativ, String) mit pytest
        def test_konto_erstellen_mit_ungueltigem_saldo(self):
            with pytest.raises(ValueError):
                Konto(1002, -10)
            with pytest.raises(ValueError):
                Konto(1003, "abc")


class TestKontoEigenschaften:
    """
    Tests für Konto-Eigenschaften (Properties)
    TODO: Team A - Testet konto_id und saldo Properties
    """

    def test_placeholder_eigenschaften(self):

        # konto.konto_id gibt korrekte ID zurück
        def test_konto_id_property(self):
            konto = Konto(1004, 20)
            assert konto.konto_id == 1004

        # konto.saldo gibt korrekten Saldo zurück
        def test_konto_saldo_property(self):
            konto = Konto(1005, 30)
            assert konto.saldo == Decimal("30.00")

        # Properties sind read-only mit pytest
        def test_properties_read_only(self):
            konto = Konto(1006, 40)
            with pytest.raises(AttributeError):
                konto.konto_id = 2000
            with pytest.raises(AttributeError):
                konto.saldo = Decimal("50.00")


class TestEinzahlung:
    """
    Tests für die Einzahlungs-Funktionalität
    TODO: Team A - Testet alle Einzahlungs-Szenarien
    """

    def test_placeholder_einzahlung(self):
        """TODO: Team A - Tests für einzahlen() Methode"""

        # Einzahlung vom pos Beitrag
        def test_einzahlung_pos_betrag(self):
            konto = Konto(1007, 10)
            konto.einzahlen(Decimal("20.00"))
            assert konto.saldo == Decimal("30.00")

        # Saldo korrekt erhöht
        def test_saldo_korrekt_erhoeht(self):
            konto = Konto(1008, 15)
            konto.einzahlen(Decimal("5.00"))
            assert konto.saldo == Decimal("20.00")

        # Einzahlung von 0 mit pytest
        def test_einzahlung_von_null(self):
            konto = Konto(1009, 10)
            with pytest.raises(ValueError):
                konto.einzahlen(Decimal("0.00"))

        # Einzahlung von negativem Betrag mit pytest
        def test_einzahlung_von_negativem_betrag(self):
            konto = Konto(1010, 10)
            with pytest.raises(ValueError):
                konto.einzahlen(Decimal("-5.00"))

        # Einzahlung von ungültigem Typ mit pytest
        def test_einzahlung_von_ungueltigem_typ(self):
            konto = Konto(1011, 10)
            with pytest.raises(TypeError):
                konto.einzahlen("fünf")


class TestAuszahlung:
    """
    Tests für die Auszahlungs-Funktionalität  
    TODO: Team A - Testet alle Auszahlungs-Szenarien
    """

    def test_placeholder_auszahlung(self):
        """TODO: Team A - Tests für auszahlen() Methode"""

        # Auszahlung bei ausreichendem Saldo
        def test_auszahlung_bei_ausreichendem_saldo(self):
            konto = Konto(1012, 50)
            konto.auszahlen(Decimal("20.00"))
            assert konto.saldo == Decimal("30.00")

        # Saldo wird korrekt reduziert
        def test_saldo_korrekt_reduziert(self):
            konto = Konto(1013, 40)
            konto.auszahlen(Decimal("10.00"))
            assert konto.saldo == Decimal("30.00")

        # Auszahlung bei unzureichendem Saldo mit pytest
        def test_auszahlung_bei_unzureichendem_saldo(self):
            konto = Konto(1014, 10)
            with pytest.raises(ValueError):
                konto.auszahlen(Decimal("20.00"))

        # Auszahlung von 0 mit pytest
        def test_auszahlung_von_null(self):
            konto = Konto(1015, 10)
            with pytest.raises(ValueError):
                konto.auszahlen(Decimal("0.00"))

        # Auszahlung von negativem Betrag mit pytest
        def test_auszahlung_von_negativem_betrag(self):
            konto = Konto(1016, 10)
            with pytest.raises(ValueError):
                konto.auszahlen(Decimal("-5.00"))

        # Überziehung vermeiden
        def test_ueberziehung_vermeiden(self):
            konto = Konto(1017, 10)
            with pytest.raises(ValueError):
                konto.auszahlen(Decimal("15.00"))


class TestKontoGrenzfaelle:
    """
    Tests für Grenzfälle und Besonderheiten
    TODO: Team A - Testet Edge Cases und besondere Situationen
    """

    def test_placeholder_grenzfaelle(self):
        """TODO: Team A - Tests für Grenzfälle"""
        # Beispiel-Tests:
        # - Sehr große Beträge
        # - Sehr kleine Beträge (Cent-Bereich)
        # - Decimal-Präzision
        # - String-Repräsentation (__str__, __repr__)
        # - Gleichheit von Konten
        assert True, "TODO: Tests für Grenzfälle implementieren"


# TODO: Team A - Erweitern Sie diese Klassen oder fügen Sie neue hinzu!
# Weitere mögliche Test-Klassen:
# - TestKontoStringRepresentation
# - TestKontoEquality
# - TestKontoValidation
