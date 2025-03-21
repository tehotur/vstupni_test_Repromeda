from shiny import render, reactive
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


# Funkce pro provádění SQL dotazů na SQLite databázi
def execute_query(query, params=(), fetch=False):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        
        cursor.execute(query, params)
        
        if fetch:  
            result = cursor.fetchall() # Výsledek pro SELECT dotazy
        else:
            conn.commit() # Změny pro INSERT, UPDATE a DELETE
            result = None  
        
        conn.close()
        return result

# Vytvoření tabulky v databázi (pokud neexistuje)
execute_query("""
    CREATE TABLE IF NOT EXISTS vysledky (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Výsledek TEXT,
        Popis TEXT
    )
""")

# Hlavní logika aplikace
def server(input, output):
    # Ukládání dat do reaktivní proměnné (DataFrame)
    data = reactive.Value(pd.DataFrame(columns=["ID", "Výsledek", "Popis"]))

    # Funkce pro načtení dat z databáze a uložení do reaktivní proměnné
    def load_data():
        result = execute_query("SELECT * FROM vysledky", fetch=True)
        df = pd.DataFrame(result, columns=["ID", "Výsledek", "Popis"])
        data.set(df)
    
    load_data()
    
    # Tabulka zobrazující data
    @output
    @render.table 
    def table():
        return data.get()

    # Funkce pro přidání nového řádku do databáze a aktualizaci tabulky 
    @reactive.effect
    @reactive.event(input.add)
    def add_row():
        execute_query("INSERT INTO vysledky (Výsledek, Popis) VALUES (?, ?)", 
                      (input.vysledek(), input.popis()))
        load_data()

    # Funkce pro smazání řádku z databáze na základě ID a aktualizaci tabulky
    @reactive.effect
    @reactive.event(input.delete)
    def delete_row():
        execute_query("DELETE FROM vysledky WHERE ID = ?", (input.delete_id(),))  
        load_data() 

    # Graf zobrazující počet jednotlivých výsledků
    @output
    @render.plot
    def graph():
        df = data.get()

        # Pokud nejsou data, zobrazí se zpráva v grafu
        if df.empty:
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, "Žádná data k zobrazení", 
                    fontsize=14, ha="center", va="center")
            ax.set_xticks([])
            ax.set_yticks([])
            return fig

        # Počet jednotlivých typů výsledků
        vysledky_count = df["Výsledek"].value_counts()

        # Vykreslení grafu
        fig, ax = plt.subplots()
        vysledky_count.plot(kind="bar", ax=ax, color=["navy", "blue", "lightskyblue"])
        ax.set_title("Počet jednotlivých výsledků")
        ax.set_xlabel("Typ výsledku")
        ax.set_ylabel("Počet")
        ax.grid(axis="y", linestyle="--", alpha=0.7)

        return fig