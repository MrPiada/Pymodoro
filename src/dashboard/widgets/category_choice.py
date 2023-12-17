import dash_bootstrap_components as dbc
from dash import html, dcc

CATEGORIES = ["pippo", "ciccio", 'piada', 'new category']

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
                    id="category-dropodown",
                    options=CATEGORIES,
                    multi=False
                )
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
