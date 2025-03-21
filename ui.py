from shiny import ui


# Definice hlavního UI layoutu aplikace
app_ui = ui.page_fluid(
    # První řádek - vstupní formuláře + graf
    ui.row(
        ui.column(4, 
            # Panel pro přidání záznamu
            ui.panel_well(
                ui.h4("Přidání záznamu:"),
                ui.input_select(  
                    "vysledek",  
                    "Vyber výsledek:",  
                    {"aneuploidie": "aneuploidie", "mozaika": "mozaika", "euploidní": "euploidní"},     
                ),

                ui.input_text("popis", "Popis"),

                ui.input_action_button("add", "Přidat řádek", class_="btn btn-info")
            ),
            # Panel pro smazání záznamu
            ui.panel_well(
                ui.h4("Smazání záznamu:"),
                ui.input_numeric("delete_id", "Zadejte ID ke smazání", value=1, min=1),
                ui.input_action_button("delete", "Smazat řádek", class_="btn btn-info")
            )    
        ),
        ui.column(8,
                ui.card(
                    ui.h3("Graf výsledků"),
                    ui.output_plot("graph"),
                ),      
        ),
    ),
    # Druhý řádek - tabulka výsledků
    ui.row(
        ui.card(
            ui.h3("Tabulka výsledků"),
            ui.div(
                ui.output_table("table"),
                style="width: 100%; table-layout: auto;" 
            )           
        )    
    )    
)