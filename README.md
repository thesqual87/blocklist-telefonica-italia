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
immediata), oppure risulta inattivo da oltre 12 mesi.

Non si accettano: numeri di privati cittadini in contesti personali, liste copiate
da servizi terzi senza permesso, numeri raccolti tramite scraping. I numeri di
servizi di emergenza, strutture sanitarie e istituzioni non entrano in lista in
nessun caso.

La lista contiene esclusivamente numero, categoria, date e conteggio delle
segnalazioni: niente nomi né altri dati che identifichino persone fisiche.
Persegue un legittimo interesse di protezione dalle chiamate indesiderate
(art. 6.1.f GDPR), che nella maggior parte dei casi violano già la normativa
sul telemarketing.

## Come segnalare un numero

Apri una [segnalazione guidata](../../issues/new/choose) — bastano il numero, la
categoria e due righe di descrizione. Oppure proponi direttamente una modifica al
CSV con una pull request.

## Il tuo numero è in lista e ritieni sia un errore?

Apri una [issue](../../issues/new/choose) oppure — se non hai un account GitHub —
scrivi a **support@kallm.app** indicando il numero. Verifichiamo e rispondiamo
**entro 7 giorni**; se l'inserimento risulta errato il numero viene rimosso
subito e protetto da reinserimenti. Richieste ed esiti vengono registrati.

## Licenza

Dati rilasciati sotto [CC BY-SA 4.0](LICENSE): usali liberamente, anche in
prodotti commerciali, citando la fonte e mantenendo aperte le versioni derivate.
La lista è mantenuta con diligenza ma su base comunitaria e volontaria: se la usi
in un tuo progetto, prevedi sempre un meccanismo di whitelist/contestazione.

## English summary

Open, community-maintained blocklist of Italian spam/scam phone numbers
(CSV, E.164 format, CC BY-SA 4.0). Contributions welcome via issues or PRs.
Inclusion requires 2+ independent reports; false positives are removed
immediately — owners can also email support@kallm.app.

---

Progetto avviato dalla community di **Kallm**, app iOS per il blocco dei call
center. La lista è indipendente e aperta al contributo di chiunque.
