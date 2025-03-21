# Shiny aplikace pro správu výsledků  

Tato aplikace umožňuje **přidávání, mazání a vizualizaci** výsledků karyotypu.  
Data jsou ukládána do **SQLite databáze** a zobrazována v tabulce a grafu.  

## Požadavky  

- Python 3  
- Knihovny: `shiny`, `pandas`, `matplotlib`, `sqlite3`  

Instalace závislostí:  
```bash
pip install shiny pandas matplotlib
```

Spuštění aplikace:
aplikace poběží na http://localhost:8000
```bash
shiny run --reload app.py
```

## UI (Grafické rozhraní)  
- **Sekce pro přidání nového záznamu** (výsledek + popis)  
- **Sekce pro smazání záznamu** podle ID  
- **Tabulka** zobrazující uložená data  
- **Graf**, který vizualizuje počet jednotlivých výsledků  

## Server (Logika aplikace)
- **Při spuštění aplikace se inicializuje databáze** a vytvoří se prázdná tabulka vysledků 
- **Načítání dat** z SQLite databáze  
- **Přidávání nových záznamů**  
- **Mazání záznamů** podle ID  
- **Automatická aktualizace** tabulky a grafu po změně dat 
