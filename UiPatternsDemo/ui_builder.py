import omni.ui as ui
from omni.isaac.ui.element_wrappers import UIWidgetWrapper

from .components import counter_component


class UIBuilder:

    def __init__(self):
        self.wrapped_ui_elements: list[UIWidgetWrapper] = []

    def cleanup(self):
        for ui_elem in self.wrapped_ui_elements:
            ui_elem.cleanup()

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

            self._create_value_description_frame(self._computed_value)

    def _create_value_description_frame(self, int_model: ui.SimpleIntModel):
        description_frame = ui.Frame(height=40)

        # Overwrite frame contents whenever the model changes
        # Create Frame first, use reference inside the callback
        # https://docs.omniverse.nvidia.com/kit/docs/omni.kit.documentation.ui.style/latest/containers.html#frame
        def int_changed(model: ui.SimpleIntModel):
            with description_frame:
                if model.as_int <= -5:
                    ui.Label(
                        "Low",
                        alignment=ui.Alignment.CENTER,
                        style={"font_size": 42},
                    )

                elif model.as_int >= 5:
                    ui.Label(
                        "High",
                        alignment=ui.Alignment.CENTER,
                        style={"font_size": 42},
                    )

                else:
                    ui.Spacer()

        int_model.add_value_changed_fn(lambda model: int_changed(model))
