'''Archivo de utilidades para crear tarjetas de información estilizadas.'''

import reflex as rx

# Tarjeta de información reutilizable (gastos, ingresos, billetera, ahorros)
def info_card(title: str, content: str, font_color: str, color: str) -> rx.Component:
    """Crea una tarjeta estilizada con un título y contenido."""
    return rx.box(
        # Título de la tarjeta
        rx.heading(
            title,
            size="2",
            color=font_color,
            margin_bottom="0.25em",
        ),
        # Contenido
        rx.text(
            content,
            size="6",
            color=font_color,
        ),
        bg=color,
        padding="1em",
        border_radius="32px",
        width="100%",
    )