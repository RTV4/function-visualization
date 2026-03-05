# function-visualization

Program v Pythonu, který pomocí **NumPy** generuje hodnoty a pomocí **Matplotlib** vykresluje grafy vybraných matematických funkcí.  
Výstupem jsou obrázky ve složce `images/`.

## Instalace

```bash
pip install numpy matplotlib
```

## Spuštění

V kořeni repozitáře:

```bash
python main.py all
```

Nebo vykreslení jedné konkrétní funkce (pokročilá část – volba uživatelem, možnost A):

```bash
python main.py sine
python main.py quadratic --a 1 --b -2 --c -3
python main.py exponential --k 0.5
```

Kombinovaný graf (minimálně 3 funkce):

```bash
python main.py multiple
```

Automatické vykreslení sinu pro různé parametry (pokročilá část – možnost B):

```bash
python main.py sine-multiples
```

## Jaké funkce program vykresluje

Definované v `functions.py`:

1. **Lineární**: `f(x) = a·x + b`
2. **Kvadratická**: `f(x) = a·x² + b·x + c`
3. **Sinus**: `f(x) = A·sin(freq·x + phase)`
4. **Exponenciální**: `f(x) = base^(k·x)` (defaultně `base = e`)
5. **Logistická (vlastní volba)**: `f(x) = L / (1 + e^{-k(x-x0)})`

## Generování hodnot x

Hodnoty `x` se generují pomocí `np.linspace(xmin, xmax, points)`.  
Defaultně je interval `[-10, 10]` a `points = 1000`.

## Požadavky na grafy

Každý graf má:
- název (`title`)
- popis os (`xlabel`, `ylabel`)
- legendu (`legend`)
- je uložen do složky `images/`

### Extra (pokročilejší část – možnost C)

U jednotlivých funkcí se v grafu automaticky vyznačí **maximum a minimum** (počítáno přes NumPy `argmax/argmin`).

## Experiment (část 8)

U exponenciální funkce byl změněn interval:

- **široký interval** `[-10, 10]` → exponenciála roste extrémně rychle a graf je „useknutý“ v rozsahu osy Y  
  výstup: `images/experiment_exponential_wide.png`

- **zúžený interval** `[-2, 2]` → graf je čitelnější a lépe ukazuje tvar funkce  
  výstup: `images/experiment_exponential_small.png`

Spuštění experimentu:

```bash
python main.py experiment
```

## Výstupní soubory (příklady)

- `images/linear.png`
- `images/quadratic.png`
- `images/sine.png`
- `images/exponential.png`
- `images/logistic.png`
- `images/multiple_functions.png`
- `images/sine_multiples.png`
- `images/experiment_exponential_wide.png`
- `images/experiment_exponential_small.png`
