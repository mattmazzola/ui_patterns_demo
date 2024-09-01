import omni.log
import omni.ui as ui

from ..components.counter import counter_component
from ..themes.colors import cl, color_gray


# https://docs.omniverse.nvidia.com/kit/docs/omni.kit.documentation.ui.style/latest/window.html#menubar
def create_modal(modal: ui.Window | None, int_model: ui.SimpleIntModel):
    if not modal:
        modal = ui.Window(
            "Example Modal",
            width=300,
            height=300,
            flags=ui.WINDOW_FLAGS_MENU_BAR,
        )

        modal_style = {
            "Label::large": {
                "font_size": 28,
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

        modal.menu_bar.style = menu_bar_style
        with modal.menu_bar:
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
                    modal.visible = False

                ui.MenuItem(
                    "Hide",
                    # hide_on_click=True,
                    triggered_fn=hide_window,
                )

        with modal.frame:
            with ui.VStack(height=0, style=modal_style):
                int_label = ui.Label(
                    "",
                    name="large",
                )

                def on_int_changed(model: ui.SimpleIntModel):
                    int_label.text = f"Total Value: {model.as_int}"

                int_model.add_value_changed_fn(on_int_changed)
                on_int_changed(int_model)

                with ui.VStack(height=100, alignment=ui.Alignment.V_CENTER):
                    ui.Spacer()
                    counter_component("Modal Counter")
                    ui.Spacer(height=30)

                def show_hide_menu(menubar: ui.MenuBar):
                    menubar.visible = not menubar.visible

                ui.Button(
                    "Click here to show/hide Menu",
                    clicked_fn=lambda: show_hide_menu(modal.menu_bar),
                    height=40,
                )

                def add_menu(menubar: ui.MenuBar):
                    with menubar:
                        with ui.Menu("New Menu"):
                            ui.MenuItem("I don't do anything")

                ui.Button(
                    "Add New Menu",
                    clicked_fn=lambda: add_menu(modal.menu_bar),
                    height=40,
                )

    omni.log.info("Modal Exists! Set visible to True")
    modal.visible = True

    return modal
