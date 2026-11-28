"""
TDD-Template für Currency-API Service
=====================================

Aufgabe:
- Funktion ruft Currency-API auf (mocken!)
- Extrahiert Wechselkurs aus JSON
- Gibt Bewertung zurück basierend auf Kurs

Wechselkurs-Bewertungen (Beispiel: EUR → USD):
- < 0.90:     "sehr ungünstig"
- 0.90-0.99:  "ungünstig"
- 1.00-1.09:  "fair"
- 1.10-1.19:  "günstig"
- ≥ 1.20:     "sehr günstig"

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!

Dokumentiert eure Autorschaft: Wer hat welchen TDD-Schritt gemacht?
"""

import pytest
"""
TDD-Template für Currency-API Service
=====================================

Team B - Currency API mit Mocking

TDD-Prozess:
RED -> GREEN -> REFACTOR
"""

from unittest.mock import patch

from Uebung4.Code.currency_service import get_exchange_rate_assessment


class TestCurrencyService:
    """
    Tests für Currency-API Service
    """

    # TDD-Zyklus 1: RED von RTRE
    # TDD-Zyklus 1: GREEN von RTRE
    # TDD-Zyklus 1: REFACTOR von RTRE
    def test_fair_rate(self):
        """Kurs 1.05 -> fair"""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"rate": 1.05}

            result = get_exchange_rate_assessment("EUR", "USD")

            assert result == "fair"

    # TDD-Zyklus 2: RED von RTRE
    # TDD-Zyklus 2: GREEN von RTRE
    # TDD-Zyklus 2: REFACTOR von RTRE
    def test_sehr_unguenstig(self):
        """Kurs 0.85 -> sehr ungünstig"""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"rate": 0.85}

            result = get_exchange_rate_assessment("EUR", "GBP")

            assert result == "sehr ungünstig"

    # TDD-Zyklus 3: RED von RTRE
    # TDD-Zyklus 3: GREEN von RTRE
    # TDD-Zyklus 3: REFACTOR von RTRE
    def test_unguenstig(self):
        """Kurs 0.95 -> ungünstig"""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"rate": 0.95}

            result = get_exchange_rate_assessment("EUR", "GBP")

            assert result == "ungünstig"

    # TDD-Zyklus 4: RED von RTRE
    # TDD-Zyklus 4: GREEN von RTRE
    # TDD-Zyklus 4: REFACTOR von RTRE
    def test_guenstig(self):
        """Kurs 1.15 -> günstig"""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"rate": 1.15}

            result = get_exchange_rate_assessment("USD", "EUR")

            assert result == "günstig"

    # TDD-Zyklus 5: RED von RTRE
    # TDD-Zyklus 5: GREEN von RTRE
    # TDD-Zyklus 5: REFACTOR von RTRE
    def test_sehr_guenstig(self):
        """Kurs 1.25 -> sehr günstig"""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"rate": 1.25}

            result = get_exchange_rate_assessment("USD", "EUR")

            assert result == "sehr günstig"

    # TDD-Zyklus 6: RED von RTRE
    # TDD-Zyklus 6: GREEN von RTRE
    # TDD-Zyklus 6: REFACTOR von RTRE
    def test_api_url_wird_korrekt_aufgerufen(self):
        """Prüft den korrekten API-Aufruf"""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"rate": 1.05}

            get_exchange_rate_assessment("EUR", "USD")

            mock_get.assert_called_once_with(
                "https://api.exchangerate.com/convert?from=EUR&to=USD",
                timeout=5,
            )