from dataclasses import dataclass, field

import omni.log
import omni.ui as ui

from ..themes.default import counter_style


@dataclass
class CounterComponent:
    int_model: ui.SimpleIntModel = field(default_factory=ui.SimpleIntModel)


def counter_component(title: str = "Counter"):
    # https://docs.omniverse.nvidia.com/kit/docs/omni.kit.documentation.ui.style/latest/styling.html#customize-the-selector-type-using-style-type-name-override
    with ui.VStack(
        style=counter_style,
        spacing=10,
    ):
        ui.Label(
            title,
            alignment=ui.Alignment.CENTER,
            name="title",
        )

        with ui.HStack():
            ui.Spacer()
            with ui.HStack(
                spacing=0,
                width=200,
                height=50,
                alignment=ui.Alignment.CENTER,
            ):
                counter_int_model = ui.SimpleIntModel(0)

                def _on_click_decrement():
                    omni.log.info(f"Decrement - Counter Value: {counter_int_model.as_int}")
                    counter_int_model.set_value(counter_int_model.as_int - 1)

                def _on_click_increment():
                    omni.log.info(f"Increment - Counter Value: {counter_int_model.as_int}")
                    counter_int_model.set_value(counter_int_model.as_int + 1)

                ui.Button(
                    text="Dec",
                    name="dec",
                    style_type_name_override="DecrementButton",
                    clicked_fn=_on_click_decrement,
                )

                counter_label = ui.Label(
                    str(counter_int_model.as_int),
                    alignment=ui.Alignment.CENTER,
                    style={"font_size": 24},
                )

                def update_value(model: ui.SimpleIntModel):
                    counter_label.text = str(model.as_int)

                counter_int_model.add_value_changed_fn(update_value)

                ui.Button(
                    text="Inc",
                    name="inc",
                    style_type_name_override="IncrementButton",
                    clicked_fn=_on_click_increment,
                )

            ui.Spacer()

    counter_component = CounterComponent(int_model=counter_int_model)

    return counter_component
