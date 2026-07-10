# Come contribuire

## Segnalare un numero (il modo più semplice)

Apri una [issue con il modulo di segnalazione](../../issues/new/choose) indicando:

1. **Numero** in formato internazionale: `+39` seguito dal numero. Per i fissi
   italiani lo 0 iniziale resta (`+390212345678`), per i cellulari no zero
   (`+393471234567`).
2. **Categoria** — vedi [`data/categorie.md`](data/categorie.md).
3. **Quando** ti ha chiamato l'ultima volta.
4. **Cosa dicevano / cosa proponevano** — due righe bastano. Non inserire dati
   personali tuoi o di altri.

Un manutentore verifica (cerca riscontri pubblici o attende una seconda
segnalazione indipendente) e aggiorna il CSV.

## Proporre modifiche dirette (pull request)

Modifica `data/blocklist.csv` rispettando le regole, che sono verificate
automaticamente a ogni push da `scripts/valida.py`:

- formato numero: `+39` + 6–11 cifre; fissi con lo 0, cellulari che iniziano per 3;
- niente duplicati; righe ordinate per numero crescente;
- `categoria` tra quelle ammesse; date in formato `AAAA-MM-GG`;
- `segnalazioni` ≥ 1; `note` senza dati personali.

Per verificare in locale: `python3 scripts/valida.py`

## Segnalare un falso positivo

Se un numero legittimo è finito in lista, apri una issue con oggetto
"Falso positivo: +39..." spiegando il motivo: viene rimosso subito e il caso
viene annotato per evitare che rientri.

## Principi

- **Trasparenza**: ogni numero in lista ha una storia verificabile (issue collegata).
- **Prudenza**: meglio un numero in meno che un falso positivo.
- **Niente scraping**: la lista cresce solo con segnalazioni dirette e fonti
  pubbliche riutilizzabili lecitamente.
