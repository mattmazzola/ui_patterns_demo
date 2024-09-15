import omni.log
import omni.ui as ui
from omni.ui import color as cl

from ..components.counter import counter_component
from ..themes.colors import (
    color_black,
    color_gray,
    color_gray_dark,
    color_green,
    color_green_light,
)

modal_style = {
    "Label::large": {
        "font_size": 28,
    },
    "Button": {
        "border_radius": 6,
        "background_color": color_green,
    },
    "Button:hovered": {
        "background_color": color_green_light,
    },
    "Button.Label": {
        "font_size": 22,
        "color": color_gray_dark,
    },
    "Button.Label:hovered": {
        "color": color_black,
    },
}

menu_bar_style = {
    "MenuBar": {
        "color": color_gray,
        "background_selected_color": cl.green,
        "border_radius": 2,
        "border_width": 1,
        "border_color": cl.yellow,
        "padding": 2,
    },
}


# https://docs.omniverse.nvidia.com/kit/docs/omni.kit.documentation.ui.style/latest/window.html#menubar
def create_modal(modal_window: ui.Window | None, int_model: ui.SimpleIntModel):
    coupled_counter = None

    if not modal_window:
        modal_window = ui.Window(
            "Example Modal",
            width=280,
            height=430,
            flags=ui.WINDOW_FLAGS_MENU_BAR,
            visible=False,
        )

        modal_window.menu_bar.style = menu_bar_style
        with modal_window.menu_bar:
            with ui.Menu("File"):
                ui.MenuItem("Save")
                ui.MenuItem("Export")
                ui.Separator()
                with ui.Menu("More Cameras"):
                    ui.MenuItem("This Menu is Pushed")
                    ui.MenuItem("and Aligned with a widget")

            with ui.Menu("Window"):

                def hide_window():
                    omni.log.info("Hiding Window")
                    # self._window_menu_example.destroy()
                    modal_window.visible = False

                ui.MenuItem(
                    "Hide",
                    # hide_on_click=True,
                    triggered_fn=hide_window,
                )

        with modal_window.frame:
            with ui.VStack(spacing=20, height=0, style=modal_style):
                int_label = ui.Label(
                    "",
                    name="large",
                )

                def on_int_changed(model: ui.SimpleIntModel):
                    int_label.text = f"Total Value: {model.as_int}"

                int_model.add_value_changed_fn(on_int_changed)
                on_int_changed(int_model)

                coupled_counter = counter_component("Coupled Counter")
                coupled_counter.int_model.add_value_changed_fn(on_int_changed)

                counter_component("Modal Counter")

                def show_hide_menu(menubar: ui.MenuBar):
                    menubar.visible = not menubar.visible

                ui.Button(
                    "Show/Hide Menu",
                    clicked_fn=lambda: show_hide_menu(modal_window.menu_bar),
                    height=40,
                )

                def add_menu(menubar: ui.MenuBar):
                    with menubar:
                        with ui.Menu("New Menu"):
                            ui.MenuItem("I don't do anything")

                ui.Button(
                    "Add New Menu",
                    clicked_fn=lambda: add_menu(modal_window.menu_bar),
                    height=40,
                )

    return modal_window, coupled_counter
