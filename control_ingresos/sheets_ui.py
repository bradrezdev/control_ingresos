"""Archivo de interfaz de usuario para visualizar las hojas modales (sheets)."""

import reflex as rx

# Hoja modal para agregar nuevo ingreso, gasto o ahorro
from .utils.ui_components import *

def sheets_ui() -> rx.Component:
    return rx.flex(
        #new_entry_sheet(),
        confirmation_pill(
            "Hecho",
            Custom_theme().light_colors()["primary"]
        ),
        align="center",
        justify="center",
        width="100%",
    )