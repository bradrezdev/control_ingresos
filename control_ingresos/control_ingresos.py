"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

# Import de UI components
from .utils.ui_components import *

# Import de pages
from .sheets_ui import sheets_ui

from rxconfig import config


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.flex(
        menu_bar(),
        info_cards(),
        operations_summary(),
        direction="column",
        align="center",
        spacing="7",
        padding_x="10px",
        height="100%",
    )


app = rx.App()
app.add_page(index)
app.add_page(sheets_ui, route="/sheets_ui")