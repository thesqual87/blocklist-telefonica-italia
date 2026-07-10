#!/usr/bin/env python3
"""Validazione di data/blocklist.csv.

Regole:
- intestazione esatta: numero,categoria,prima_segnalazione,ultima_attivita,segnalazioni,note
- numero: +39 seguito da 6-11 cifre; cellulari iniziano per 3, fissi per 0
- niente duplicati; righe ordinate per valore numerico crescente
- categoria tra quelle ammesse (vedi data/categorie.md)
- date in formato ISO AAAA-MM-GG, prima_segnalazione <= ultima_attivita
- segnalazioni: intero >= 1

Uso: python3 scripts/valida.py  (exit code 0 = ok, 1 = errori)
"""

import csv
import re
import sys
from datetime import date
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "blocklist.csv"
HEADER = ["numero", "categoria", "prima_segnalazione",
          "ultima_attivita", "segnalazioni", "note"]
CATEGORIE = {"truffa", "finanza", "energia", "telefonia",
             "sondaggi", "pubblicita", "ping", "altro"}
NUMERO_RE = re.compile(r"^\+39[03]\d{5,10}$")
DATA_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

errori = []


def errore(riga, msg):
    errori.append(f"riga {riga}: {msg}")


def data_valida(testo):
    if not DATA_RE.match(testo):
        return None
    try:
        return date.fromisoformat(testo)
    except ValueError:
        return None


def main():
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        righe = list(csv.reader(f))

    if not righe or righe[0] != HEADER:
        print(f"ERRORE: intestazione errata, attesa: {','.join(HEADER)}")
        sys.exit(1)

    visti = set()
    precedente = 0
    for i, riga in enumerate(righe[1:], start=2):
        if len(riga) != len(HEADER):
            errore(i, f"attese {len(HEADER)} colonne, trovate {len(riga)}")
            continue
        numero, categoria, prima, ultima, segnalazioni, note = riga

        if not NUMERO_RE.match(numero):
            errore(i, f"numero non valido: {numero!r} "
                      "(atteso +39 + 6-11 cifre, fissi con 0, cellulari con 3)")
            continue

        valore = int(numero[1:])
        if numero in visti:
            errore(i, f"duplicato: {numero}")
        visti.add(numero)
        if valore <= precedente:
            errore(i, f"ordinamento: {numero} non è maggiore del precedente")
        precedente = valore

        if categoria not in CATEGORIE:
            errore(i, f"categoria sconosciuta: {categoria!r} "
                      f"(ammesse: {', '.join(sorted(CATEGORIE))})")

        d1, d2 = data_valida(prima), data_valida(ultima)
        if d1 is None:
            errore(i, f"prima_segnalazione non valida: {prima!r}")
        if d2 is None:
            errore(i, f"ultima_attivita non valida: {ultima!r}")
        if d1 and d2 and d1 > d2:
            errore(i, "prima_segnalazione successiva a ultima_attivita")

        if not segnalazioni.isdigit() or int(segnalazioni) < 1:
            errore(i, f"segnalazioni non valide: {segnalazioni!r} (intero >= 1)")

    if errori:
        print(f"VALIDAZIONE FALLITA — {len(errori)} errori:")
        for e in errori:
            print(" -", e)
        sys.exit(1)

    print(f"OK — {len(righe) - 1} voci valide.")


if __name__ == "__main__":
    main()
