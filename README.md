# Blocklist telefonica Italia

Lista pubblica e aperta di numeri di telefono usati per spam, telemarketing
aggressivo e truffe telefoniche in Italia. Mantenuta dalla community, utilizzabile
da chiunque: app di blocco chiamate (iOS, Android), centralini, FRITZ!Box, ricerca.

> Progetti equivalenti esistono per la Germania, la Spagna e la Francia.
> Per l'Italia non esisteva: questa lista nasce per riempire quel vuoto.

## I dati

Il file è [`data/blocklist.csv`](data/blocklist.csv), scaricabile direttamente:

```
https://raw.githubusercontent.com/thesqual87/blocklist-telefonica-italia/main/data/blocklist.csv
```

Formato (CSV, UTF-8, separatore virgola):

| Colonna | Descrizione | Esempio |
|---|---|---|
| `numero` | Formato internazionale E.164 (per i fissi italiani lo 0 resta) | `+390212345678` |
| `categoria` | Una tra quelle in [`data/categorie.md`](data/categorie.md) | `energia` |
| `prima_segnalazione` | Data ISO della prima segnalazione | `2026-07-10` |
| `ultima_attivita` | Data ISO dell'ultima chiamata segnalata | `2026-07-10` |
| `segnalazioni` | Numero di segnalazioni indipendenti ricevute | `3` |
| `note` | Testo libero facoltativo (senza dati personali) | `si spaccia per gestore luce` |

Le righe sono ordinate per numero crescente e senza duplicati; ogni modifica passa
una validazione automatica (`scripts/valida.py`).

## Criteri di inclusione

Un numero entra in lista se: **almeno 2 segnalazioni indipendenti**, oppure 1
segnalazione accompagnata da riscontri pubblici verificabili (discussioni online,
segnalazioni su altri servizi, provvedimenti pubblici).

Un numero esce dalla lista se: viene dimostrato un falso positivo (rimozione
immediata, basta aprire una issue), oppure risulta inattivo da oltre 12 mesi.

Non si accettano: numeri di privati cittadini in contesti personali, liste copiate
da servizi terzi senza permesso, numeri raccolti tramite scraping.

## Come segnalare un numero

Apri una [segnalazione guidata](../../issues/new/choose) — bastano il numero, la
categoria e due righe di descrizione. Oppure proponi direttamente una modifica al
CSV con una pull request.

## Licenza

Dati rilasciati sotto [CC BY-SA 4.0](LICENSE): usali liberamente, anche in
prodotti commerciali, citando la fonte e mantenendo aperte le versioni derivate.

## English summary

Open, community-maintained blocklist of Italian spam/scam phone numbers
(CSV, E.164 format, CC BY-SA 4.0). Contributions welcome via issues or PRs.
Inclusion requires 2+ independent reports; false positives are removed immediately.

---

Progetto avviato dalla community di **KALLM**, app iOS per il blocco dei call
center. La lista è indipendente e aperta al contributo di chiunque.
