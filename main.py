from nicegui import ui
from cardview import *

#Cards page
@ui.page('/cards')
async def cards():
    ui.label("This should be the cards page")
    cardgrid = ui.aggrid({
    'defaultColDef': {'flex': 1},
    'columnDefs': [
        {'headerName': 'Name', 'field': 'name'},
        {'headerName': 'Age', 'field': 'age'},
        {'headerName': 'Parent', 'field': 'parent', 'hide': True},
    ],
    'rowData': [
        {'name': 'Alice', 'age': 18, 'parent': 'David'},
        {'name': 'Bob', 'age': 21, 'parent': 'Eve'},
        {'name': 'Carol', 'age': 42, 'parent': 'Frank'},
    ],
    'rowSelection': 'multiple',
}).classes('max-h-40')


#Home Page
ui.label("Card Collector")
ui.button("Cards", on_click=lambda: ui.navigate.to(cards,new_tab=False))
ui.run()