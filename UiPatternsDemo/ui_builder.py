import omni.log
import omni.ui as ui
from omni.isaac.ui.element_wrappers import UIWidgetWrapper
from omni.ui import color as cl

from .components import counter_component, create_value_description_frame


class UIBuilder:

    def __init__(self):
        self.wrapped_ui_elements: list[UIWidgetWrapper] = []
        self._window_menu_example = None

    def cleanup(self):
        for ui_elem in self.wrapped_ui_elements:
            ui_elem.cleanup()

        if self._window_menu_example is not None:
            self._window_menu_example.visible = False
            self._window_menu_example.destroy()
            self._window_menu_example = None

    def build_ui(self):
        with ui.VStack(spacing=20):
            ui.Label(
                "UI Patterns Demo",
                alignment=ui.Alignment.CENTER,
                style={"font_size": 28},
            )

            self._counter_1_int_model = counter_component("Counter 1")
            self._counter_2_int_model = counter_component("Counter 2")

            # Create computed value from the sum of the two counters
            self._computed_value = ui.SimpleIntModel(0)

            def update_computed_value(_: ui.SimpleIntModel):
                total = self._counter_1_int_model.as_int + self._counter_2_int_model.as_int
                self._computed_value.set_value(total)

            self._counter_1_int_model.add_value_changed_fn(update_computed_value)
            self._counter_2_int_model.add_value_changed_fn(update_computed_value)

            self._computed_label = ui.Label(
                f"Total: {self._computed_value.as_int}",
                alignment=ui.Alignment.CENTER,
                style={"font_size": 28},
            )

            def update_computed_label(model: ui.SimpleIntModel):
                self._computed_label.text = f"Total: {model.as_int}"

            self._computed_value.add_value_changed_fn(update_computed_label)

            create_value_description_frame(
                self._computed_value,
                low_threshold=-3,
                high_threshold=4,
            )

            with ui.HStack(width=0):
                ui.Button(
                    text="window with MenuBar Example",
                    clicked_fn=self.create_and_show_window_with_menu,
                )
                ui.Label(
                    "this populates the menuBar",
                    name="text",
                    style={"margin_width": 10},
                )

    # https://docs.omniverse.nvidia.com/kit/docs/omni.kit.documentation.ui.style/latest/window.html#menubar
    def create_and_show_window_with_menu(self):
        if not self._window_menu_example:
            self._window_menu_example = ui.Window(
                "Window Menu Example",
                width=300,
                height=300,
                flags=ui.WINDOW_FLAGS_MENU_BAR,
            )

            menu_bar_style = {
                "MenuBar": {
                    "background_color": cl.blue,
                    "color": cl.pink,
                    "background_selected_color": cl.green,
                    "border_radius": 2,
                    "border_width": 1,
                    "border_color": cl.yellow,
                    "padding": 2,
                }
            }

            self._window_menu_example.menu_bar.style = menu_bar_style
            with self._window_menu_example.menu_bar:
                with ui.Menu("File"):
                    ui.MenuItem("Load")
                    ui.Separator()
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
                        self._window_menu_example.visible = False

                    ui.MenuItem(
                        "Hide",
                        # hide_on_click=True,
                        triggered_fn=hide_window,
                    )

            with self._window_menu_example.frame:
                with ui.VStack():
                    ui.Button("This Window has a Menu")

                    def show_hide_menu(menubar: ui.MenuBar):
                        menubar.visible = not menubar.visible

                    ui.Button(
                        "Click here to show/hide Menu",
                        clicked_fn=lambda: show_hide_menu(self._window_menu_example.menu_bar),
                    )

                    def add_menu(menubar):
                        with menubar:
                            with ui.Menu("New Menu"):
                                ui.MenuItem("I don't do anything")

                    ui.Button("Add New Menu", clicked_fn=lambda: add_menu(self._window_menu_example.menu_bar))

        omni.log.info("Showing Window")
        self._window_menu_example.visible = True
