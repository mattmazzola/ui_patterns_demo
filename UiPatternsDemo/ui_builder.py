import omni.ui as ui
from omni.isaac.ui.element_wrappers import UIWidgetWrapper


class UIBuilder:

    def __init__(self):
        self.wrapped_ui_elements: list[UIWidgetWrapper] = []

    def cleanup(self):
        for ui_elem in self.wrapped_ui_elements:
            ui_elem.cleanup()

    def build_ui(self):
        self._create_example_frame()

    def _create_example_frame(self):
        self._buttons_container = ui.ScrollingFrame(height=40)

        # Overwrite frame contents whenever the model changes
        # Create Frame first, use reference inside the callback
        def changed(model: ui.SimpleIntModel, recreate_ui=self._buttons_container):
            with recreate_ui:
                with ui.HStack():
                    for i in range(model.as_int):
                        ui.Button(f"Button #{i}")

        model = ui.IntDrag(min=0, max=10).model
        model.add_value_changed_fn(changed)
