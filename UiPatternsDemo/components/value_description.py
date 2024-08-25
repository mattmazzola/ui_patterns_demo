import omni.ui as ui


def create_value_description_frame(
    int_model: ui.SimpleIntModel,
    low_threshold=-5,
    high_threshold=5,
):
    description_frame = ui.Frame(height=40)

    # Overwrite frame contents whenever the model changes
    # Create Frame first, use reference inside the callback
    # https://docs.omniverse.nvidia.com/kit/docs/omni.kit.documentation.ui.style/latest/containers.html#frame
    def int_changed(model: ui.SimpleIntModel):
        with description_frame:
            if model.as_int <= low_threshold:
                ui.Label(
                    "Low",
                    alignment=ui.Alignment.CENTER,
                    style={"font_size": 42},
                )

            elif model.as_int >= high_threshold:
                ui.Label(
                    "High",
                    alignment=ui.Alignment.CENTER,
                    style={"font_size": 42},
                )

            else:
                ui.Spacer()

    int_model.add_value_changed_fn(lambda model: int_changed(model))
