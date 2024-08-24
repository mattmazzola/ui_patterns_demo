import omni.log
import omni.ui as ui
from omni.isaac.ui.element_wrappers import UIWidgetWrapper


class UIBuilder:

    def __init__(self):
        self.wrapped_ui_elements: list[UIWidgetWrapper] = []

    def cleanup(self):
        for ui_elem in self.wrapped_ui_elements:
            ui_elem.cleanup()

    def build_ui(self):
        ui.Label(
            "UI Patterns Demo",
            alignment=ui.Alignment.CENTER,
            style={"font_size": 28},
        )
        ui.Label(
            "Counter",
            alignment=ui.Alignment.CENTER,
            style={"font_size": 20},
        )
        self._counter_int_model = self._create_counter()
        self._create_value_description_frame(self._counter_int_model)

    def _create_counter(self):
        with ui.HStack():
            ui.Spacer()
            with ui.HStack(spacing=0, width=200, height=50, alignment=ui.Alignment.CENTER):
                counter_int_model = ui.SimpleIntModel(0)

                def _on_click_decrement():
                    omni.log.info(f"Decrement - Counter Value: {counter_int_model.as_int}")
                    counter_int_model.set_value(counter_int_model.as_int - 1)

                def _on_click_increment():
                    omni.log.info(f"Increment - Counter Value: {counter_int_model.as_int}")
                    counter_int_model.set_value(counter_int_model.as_int + 1)

                ui.Button(text="Dec", clicked_fn=_on_click_decrement)

                counter_label = ui.Label(
                    str(counter_int_model.as_int),
                    alignment=ui.Alignment.CENTER,
                    style={"font_size": 24},
                )

                def update_value(model: ui.SimpleIntModel):
                    counter_label.text = str(model.as_int)

                counter_int_model.add_value_changed_fn(update_value)

                ui.Button(text="Inc", clicked_fn=_on_click_increment)

            ui.Spacer()

        return counter_int_model

    def _create_value_description_frame(self, int_model: ui.SimpleIntModel):
        description_frame = ui.Frame(height=40)

        # Overwrite frame contents whenever the model changes
        # Create Frame first, use reference inside the callback
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
