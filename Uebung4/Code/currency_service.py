"""
Implementierung: Currency-API Service
=====================================

Die Funktion soll:
1. Currency-API aufrufen (in Tests gemockt)
2. Wechselkurs extrahieren
3. Bewertung zurückgeben

Hinweise:
- Nutzt requests.get() für API-Aufrufe
- API-URL: https://api.exchangerate.com/convert?from={from_currency}&to={to_currency}
- Response-Format: {"rate": 1.05}
- Startet mit minimalster Implementierung!
"""

import requests

def get_exchange_rate_assessment(from_currency: str, to_currency: str) -> str:
    """
    Ruft Currency-API auf und gibt Bewertung des Wechselkurses zurück.
    """

    url = (
        f"https://api.exchangerate.com/convert"
        f"?from={from_currency}&to={to_currency}"
    )

    response = requests.get(url, timeout=5)

    data = response.json()
    rate = data.get("rate")

    if rate < 0.90:
        return "sehr ungünstig"
    elif rate < 1.00:
        return "ungünstig"
    elif rate < 1.10:
        return "fair"
    elif rate < 1.20:
        return "günstig"
    else:
        return "sehr günstig"
    pass
