from nicegui import ui

#Cards page
@ui.page('/cards')
async def cards():
    ui.label("This should be the cards page")
    CardGrid = ui.grid({
        'defaultColDef': {'flex': 1},
        'columnDefs': [
            {'headerName': 'Name', 'field': 'Name'},
            {'headerName': 'Set', 'field': 'SetCode'},
            {'headerName': 'Number', 'field': 'SetNum'},
        ],
        
    })


#Home Page
ui.label("Card Collector")
ui.button("Cards", on_click=lambda: ui.navigate.to(cards,new_tab=False))
ui.run()