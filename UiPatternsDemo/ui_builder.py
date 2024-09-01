import omni.ui as ui
from omni.isaac.ui.element_wrappers import UIWidgetWrapper

from .components import counter_component, create_modal, create_value_description_frame
from .themes.default import main_ui_style


class UIBuilder:
    def __init__(self):
        self.wrapped_ui_elements: list[UIWidgetWrapper] = []
        self._modal: ui.Window = None

    def cleanup(self):
        for ui_elem in self.wrapped_ui_elements:
            ui_elem.cleanup()

        if self._modal is not None:
            self._modal.visible = False
            self._modal.destroy()
            self._modal = None

    def build_ui(self):
        with ui.VStack(
            spacing=20,
            style=main_ui_style,
        ):
            ui.Label(
                "UI Patterns (Omniverse)",
                alignment=ui.Alignment.CENTER,
                name="header",
            )

            self._counter_1 = counter_component("Counter 1")
            self._counter_2 = counter_component("Counter 2")

            # Create computed value from the sum of the two counters
            self._computed_int_model = ui.SimpleIntModel(0)

            def update_computed_value(_: ui.SimpleIntModel):
                total = self._counter_1.int_model.as_int + self._counter_2.int_model.as_int
                self._computed_int_model.set_value(total)

            self._counter_1.int_model.add_value_changed_fn(update_computed_value)
            self._counter_2.int_model.add_value_changed_fn(update_computed_value)

            self._computed_label = ui.Label(
                f"Total: {self._computed_int_model.as_int}",
                alignment=ui.Alignment.CENTER,
                name="large",
            )

            def update_computed_label(model: ui.SimpleIntModel):
                self._computed_label.text = f"Total: {model.as_int}"

            self._computed_int_model.add_value_changed_fn(update_computed_label)

            create_value_description_frame(
                self._computed_int_model,
                low_threshold=-3,
                high_threshold=4,
            )

            def create_model_inner():
                self._modal = create_modal(self._modal, self._computed_int_model)

            ui.Button(
                text="Create Modal",
                clicked_fn=create_model_inner,
                height=40,
            )
