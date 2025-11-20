"""Aquí defines botones reutilizables para la aplicación."""

import reflex as rx

from .theme_colors import Custom_theme

# Botón para agregar nuevo ingreso, gasto o ahorro
def add_button(label: str) -> rx.Component:
    """Crea un botón estilizado para agregar nuevos elementos."""
    return rx.button(
        label,
        font_weight="bold",
        bg="#465940",
        color="white",
        size="3",
        padding="0.5em 1em",
        border_radius="32px",
        _hover={"bg": "#E0FFC2", "color": "#000000"},
        box_shadow=rx.color_mode_cond(
                light=Custom_theme().light_colors()["box_shadow"],
                dark=Custom_theme().dark_colors()["box_shadow"],
        ),
    )