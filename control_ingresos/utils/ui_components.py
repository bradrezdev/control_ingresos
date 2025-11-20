"""Archivo de componentes de interfaz de usuario"""

import reflex as rx

# Importar componentes individuales
from .theme_colors import Custom_theme
from .buttons import *
from .cards import *

# Barra de menú superior
def menu_bar() -> rx.Component:
    """Crea una barra de navegación simple."""
    return rx.hstack(
            rx.drawer.root(
                rx.drawer.trigger(add_button("Agregar")),
                rx.drawer.overlay(z_index="500"),
                rx.drawer.portal(
                    rx.drawer.content(
                    new_entry_sheet(),
                    )
                ),
                direction="bottom",
            ),
            width="100%",
            padding="1rem",
            justify="end",
            position="fixed",
            top="0",
            z_index="1",
        )

# Componente de tarjetas de información (gastos, ingresos, billetera, ahorros)
def info_cards() -> rx.Component:
    """Crea un conjunto de tarjetas de información financiera responsivas."""
    return rx.vstack(
        rx.grid(  # ⬅️ Cambio a flex con wrap
            info_card(
                "Gastos fijos",
                "$6,500.00",
                "#000000",
                "#E0FFC2"
                ),
            info_card(
                "Ingresos del mes",
                "$13,200.00",
                "#000000",
                "#FDFBF0"
                ),
            info_card(
                "Billetera",
                "$16,500.00", 
                "#FFFFFF", 
                "#465940"
                ),
            info_card(
                "Ahorros",
                "$19,230.00",
                "#000000",
                "#F5F5F5"
                ),
            spacing="2",
            columns="2",
            width="100%",
        ),
        margin_top="6em",
        spacing="2",
        width="100%",
    )

# Sheet 'Nuevo Ingreso/Gasto/Ahorro' (Modal)
def new_entry_sheet() -> rx.Component:
    """Crea un sheet modal para agregar nuevos ingresos, gastos o ahorros."""
    return rx.box(
        rx.heading("Nueva entrada", size="4", margin="1.5em 0 1.5em 0", align="center"),

        # Control de segmento para seleccionar tipo de operación
        rx.segmented_control.root(
            rx.segmented_control.item("Ingreso", value="ingreso"),
            rx.segmented_control.item("Gasto", value="gasto"),
            rx.segmented_control.item("Ahorro", value="ahorro"),
            default_value="gasto",
            margin="0 14vw 2em",
            on_change=FormsState.set_operation_type,
            value=FormsState.operation_type,
            radius="full",
            size="3",
            bg=rx.color_mode_cond(
                light=Custom_theme().light_colors()["background"],
                dark=Custom_theme().dark_colors()["background"],
            ),
            box_shadow=rx.color_mode_cond(
                light=Custom_theme().light_colors()["box_shadow"],
                dark=Custom_theme().dark_colors()["box_shadow"],
            ),
            width="60%",
        ),

        # Renderizado condicional del formulario según selección
        rx.cond(
            FormsState.operation_type == "gasto",
            Forms.gasto_form(),
            rx.cond(
                FormsState.operation_type == "ingreso",
                Forms.ingreso_form(),
                Forms.ahorro_form(),
            )
        ),

        bg=rx.color_mode_cond(
            light=Custom_theme().light_colors()["background"],
            dark=Custom_theme().dark_colors()["background"],
        ),
        border_radius="38px 38px 0 0",
        bottom="0",
        position="fixed",
        padding_x="1em",
        height="90%",
        width="100%",
    )

class FormsState(rx.State):
    # Variable que almacena el tipo de operación (ingreso, gasto, ahorro)
    operation_type: str = "gasto" # Valor por defecto.

    def set_operation_type(self, value: str | list[str]):
        """Actualiza el tipo de operación."""
        self.operation_type = value if isinstance(value, str) else value[0]

# Modal de gasto
class Forms:
    """Contiene formularios reutilizables para ingresos, gastos y ahorros."""

    # Formulario de gasto
    @staticmethod
    def gasto_form() -> rx.Component:
        return rx.box(
            rx.vstack(
                rx.hstack(
                    rx.text("Monto:"),
                    rx.input(
                        font_size="1em",
                        placeholder="Obligatorio",
                        border_radius="38px",
                        variant="soft",
                        bg=rx.color_mode_cond(
                            light=Custom_theme().light_colors()["tertiary"],
                            dark=Custom_theme().dark_colors()["tertiary"],
                        ),
                        width="100%",
                    ),
                    align="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("Descripción:"),
                    rx.input(
                        font_size="1em",
                        placeholder="Obligatorio",
                        border_radius="38px",
                        variant="soft",
                        bg=rx.color_mode_cond(
                            light=Custom_theme().light_colors()["tertiary"],
                            dark=Custom_theme().dark_colors()["tertiary"],
                        ),
                        width="100%",
                    ),
                    align="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("Categoría:", margin_right="0.5em"),
                    rx.select(
                        ["Vivienda (renta, servicios, mantenimiento)",
                            "Alimentación (súper, restaurantes, cafés)",
                            "Transporte (gasolina, Uber, transporte público)",
                            "Salud (médico, medicinas, seguro)",
                            "Educación (cursos, libros, materiales)",
                            "Entretenimiento (cine, conciertos, suscripciones)",
                            "Vestimenta (ropa, calzado, accesorios)",
                            "Tecnología (apps, gadgets, servicios en línea)",
                            "Servicios (internet, teléfono, streaming)",
                            "Otros (varios)"],
                        placeholder="Selecciona una categoría",
                        radius="full",
                        variant="ghost",
                        bg=rx.color_mode_cond(
                            light=Custom_theme().light_colors()["tertiary"],
                            dark=Custom_theme().dark_colors()["tertiary"],
                        ),
                        size="3",
                    ),
                    align="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("Subcategoría:"),
                    rx.input(
                        placeholder="Obligatorio",
                        font_size="1em",
                        border_radius="38px",
                        variant="soft",
                        bg=rx.color_mode_cond(
                            light=Custom_theme().light_colors()["tertiary"],
                            dark=Custom_theme().dark_colors()["tertiary"],
                        ),
                        width="100%",
                    ),
                    align="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("Método:", margin_right="0.5em"),
                    rx.select(
                        ["Efectivo",
                            "Tarjeta de débito",
                            "Tarjeta de crédito",
                            "Transferencia bancaria",
                            "Otro"],
                        placeholder="Selecciona un método de pago",
                        radius="full",
                        variant="ghost",
                        bg=rx.color_mode_cond(
                            light=Custom_theme().light_colors()["background"],
                            dark=Custom_theme().dark_colors()["background"],
                        ),
                        size="3",
                    ),
                    align="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("Repetir:", margin_right="0.5em"),
                    rx.select(
                        ["Anualmente",
                            "Bimestralmente",
                            "Mensualmente",
                            "Quincenalmente",
                            "Semanalmente",
                            "Nunca"],
                        placeholder="Selecciona una opción",
                        default_value="Nunca",
                        radius="full",
                        variant="ghost",
                        bg=rx.color_mode_cond(
                            light=Custom_theme().light_colors()["background"],
                            dark=Custom_theme().dark_colors()["background"],
                        ),
                        size="3",
                    ),
                    align="center",
                    width="100%",
                ),
                # Elemento condicional para mostrar al seleccionar repetir diferente de "Nunca"
                rx.hstack(
                    rx.text("Repetir hasta:", margin_right="0.5em"),
                    rx.select(
                        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
                        placeholder="Día",
                        radius="full",
                        variant="ghost",
                        bg=rx.color_mode_cond(
                            light=Custom_theme().light_colors()["background"],
                            dark=Custom_theme().dark_colors()["background"],
                        ),
                        size="3",
                    ),
                    rx.select(
                        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                        placeholder="Mes",
                        radius="full",
                        variant="ghost",
                        bg=rx.color_mode_cond(
                            light=Custom_theme().light_colors()["background"],
                            dark=Custom_theme().dark_colors()["background"],
                        ),
                        size="3",
                    ),
                    rx.select(
                        ["2025", "2026", "2027", "2028", "2029", "2030"],
                        placeholder="Año",
                        radius="full",
                        variant="ghost",
                        bg=rx.color_mode_cond(
                            light=Custom_theme().light_colors()["background"],
                            dark=Custom_theme().dark_colors()["background"],
                        ),
                        size="3",
                    ),
                    align="center",
                    width="100%",
                ),
                bg=rx.color_mode_cond(
                    light=Custom_theme().light_colors()["tertiary"],
                    dark=Custom_theme().dark_colors()["tertiary"],
                ),
                border_radius="38px",
                padding="1em",
                justify="center",
                spacing="3",
                width="100%",
            ),
            rx.button(
                "Confirmar operación",
                size="4",
                width="92%",
                position="absolute",
                bottom="1em",
                radius="full",
                bg="#0039F2",
                color="white",
            ),
        )

    # Formulario de ingreso
    @staticmethod
    def ingreso_form() -> rx.Component:
        """Formulario para registrar un ingreso."""
        return rx.box(
            rx.vstack(
                rx.hstack(
                    rx.text("Monto:"),
                    rx.input(
                        font_size="1em",
                        placeholder="Obligatorio",
                        border_radius="38px",
                        variant="soft",
                        bg=rx.color_mode_cond(
                            light=Custom_theme().light_colors()["tertiary"],
                            dark=Custom_theme().dark_colors()["tertiary"],
                        ),
                        width="100%",
                    ),
                    align="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("Descripción:"),
                        rx.input(
                            font_size="1em",
                            placeholder="Obligatorio",
                            border_radius="38px",
                            variant="soft",
                            bg=rx.color_mode_cond(
                                light=Custom_theme().light_colors()["tertiary"],
                                dark=Custom_theme().dark_colors()["tertiary"],
                            ),
                            width="100%",
                        ),
                    align="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("Categoría:", margin_right="0.5em"),
                    rx.select(
                        ["Negocio propio",
                         "Inversiones",
                         "Venta de productos",
                         "Regalos",
                         "Otros"],
                        placeholder="Selecciona una categoría",
                        radius="full",
                        variant="ghost",
                        bg=rx.color_mode_cond(
                            light=Custom_theme().light_colors()["tertiary"],
                            dark=Custom_theme().dark_colors()["tertiary"],
                        ),
                        size="3",
                    ),
                    align="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("Subcategoría:"),
                        rx.input(
                            font_size="1em",
                            placeholder="Obligatorio",
                            border_radius="38px",
                            variant="soft",
                            bg=rx.color_mode_cond(
                                light=Custom_theme().light_colors()["tertiary"],
                                dark=Custom_theme().dark_colors()["tertiary"],
                            ),
                            width="100%",
                        ),
                    align="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("Método:", margin_right="0.5em"),
                    rx.select(
                        ["Efectivo",
                         "Transferencia bancaria",
                         "Depósito",
                         "Otro"],
                        placeholder="Selecciona un método",
                        radius="full",
                        variant="ghost",
                        bg=rx.color_mode_cond(
                            light=Custom_theme().light_colors()["background"],
                            dark=Custom_theme().dark_colors()["background"],
                        ),
                        size="3",
                    ),
                    align="center",
                    width="100%",
                ),
                bg=rx.color_mode_cond(
                    light=Custom_theme().light_colors()["tertiary"],
                    dark=Custom_theme().dark_colors()["tertiary"],
                ),
                border_radius="38px",
                padding="1em",
                spacing="3",
                width="100%",
            ),
            rx.button(
                "Confirmar operación",
                size="4",
                width="92%",
                position="absolute",
                bottom="1em",
                radius="full",
                bg="#0039F2",
                color="white",
            ),
        )

    # Formulario de ahorro
    @staticmethod
    def ahorro_form() -> rx.Component:
        """Formulario para registrar un ahorro."""
        return rx.box(
            rx.vstack(
                rx.hstack(
                    rx.text("Monto:"),
                    rx.input(
                        placeholder="Obligatorio",
                        border_radius="38px",
                        variant="soft",
                        bg=rx.color_mode_cond(
                            light=Custom_theme().light_colors()["tertiary"],
                            dark=Custom_theme().dark_colors()["tertiary"],
                        ),
                        width="100%",
                    ),
                    align="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("Descripción:"),
                    rx.input(
                        placeholder="Opcional",
                        border_radius="38px",
                        variant="soft",
                        bg=rx.color_mode_cond(
                            light=Custom_theme().light_colors()["tertiary"],
                            dark=Custom_theme().dark_colors()["tertiary"],
                        ),
                        width="100%",
                    ),
                    align="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("Destino:", margin_right="0.5em"),
                    rx.select(
                        ["Fondo de emergencia",
                         "Vacaciones",
                         "Compra importante",
                         "Inversión",
                         "Retiro",
                         "Otro"],
                        placeholder="Selecciona un destino",
                        radius="full",
                        variant="ghost",
                        bg=rx.color_mode_cond(
                            light=Custom_theme().light_colors()["tertiary"],
                            dark=Custom_theme().dark_colors()["tertiary"],
                        ),
                        size="3",
                    ),
                    align="center",
                    width="100%",
                ),
                bg=rx.color_mode_cond(
                    light=Custom_theme().light_colors()["tertiary"],
                    dark=Custom_theme().dark_colors()["tertiary"],
                ),
                border_radius="38px",
                padding="1em",
                spacing="3",
                width="100%",
            ),
            rx.button(
                "Confirmar operación",
                size="4",
                width="92%",
                position="absolute",
                bottom="1em",
                radius="full",
                bg="#0039F2",
                color="white",
            ),
        )

# Resumen de operaciones realizadas (ingresos, gastos, ahorros)
# Muestra Descripción, Monto, Fecha y Categoría
def operations_summary() -> rx.Component:
    """Crea un resumen de las operaciones financieras realizadas."""
    # Aquí se implementaría la lógica para mostrar las operaciones
    return rx.box(
        rx.heading("Resumen de operaciones", margin_bottom="1em"),
        rx.flex(
            rx.hstack(
                rx.image(
                    src="/static/icons/shopping-cart.svg",
                    border_radius="48px",
                    height="auto",
                    width="50px",
                ),
                rx.vstack(
                    rx.heading("Supermercado", size="3"),
                    rx.hstack(
                        rx.badge("Tarjeta de crédito", color_scheme="green", radius="full"),
                        rx.badge("Comida", color_scheme="crimson", radius="full"),
                        spacing="1",
                        align="center",
                    ),
                    spacing="1",
                ),
                align="center",
            ),
            rx.vstack(
                rx.heading("$9,325.30", size="4"),
                rx.text(
                    "12 Mar 2025",
                    size="1"
                    ),
                align="end",
                spacing="0",
            ),
            align="center",
            direction="row",
            justify="between",
            width="100%",
        ),
        rx.divider(margin_y="1em"),
        padding_x="0.5em",
        width="100%",
    )

# Elemento visual de confirmación.
def confirmation_pill(message: str, bg: str) -> rx.Component:
    """Crea un pill de confirmación estilizado."""
    return rx.badge(
        message,
        bg=bg,
        box_shadow="0px 4px 16px 0px #00000015",
        top="5em",
        position="fixed",
        z_index="1000",
        variant="solid",
        font_size="1em",
        padding="0.5em 1em",
        border_radius="32px",
    )