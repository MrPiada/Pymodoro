import dash_bootstrap_components as dbc
from dash import html, dcc
from src.globals import *

modal_new_category = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Introduce new option")),
                dbc.ModalBody(
                    dcc.Input(
                        id="category-name-input",
                        type='text'
                    )
                ),
                dbc.ModalFooter(
                    children=[
                        dbc.Row(
                            dbc.Col(
                                dbc.ButtonGroup(
                                    [
                                        dbc.Button(
                                            "OK",
                                            id="category-ok",
                                            className="ms-auto",
                                            n_clicks=0
                                        ),
                                        dbc.Button(
                                            "Cancel",
                                            id="category-cancel",
                                            className="ms-auto",
                                            n_clicks=0
                                        )
                                    ]
                                )
                            )
                        )
                    ]
                )
            ],
            id="category-choice-modal",
            is_open=False,
            centered=True
        )
    ]
)

category_choice = dbc.Container(
    [
        dbc.Row(
            [
                dcc.Dropdown(
                    id="category-dropdown",
                    options=Globals.CATEGORIES,
                    multi=False
                ),
                dcc.Store(id='selected-category', data=None)
            ]
        ),
        dbc.Row(
            [
                modal_new_category,
                html.Div(id="category-modal")
            ]
        )
    ],
    fluid=True
)
