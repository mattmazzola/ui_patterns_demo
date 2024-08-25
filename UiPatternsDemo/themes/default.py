from omni.ui import color as cl

color_button_inc_default = cl("#117edd")
color_button_inc_label_default = cl("#aaaaaa")
color_button_inc_hover = cl("#006eff")
color_button_inc_label_hover = cl("#ffffff")

color_button_dec_default = cl("#6db2fa")
color_button_dec_label_default = cl("#444444")
color_button_dec_hover = cl("#4da2da")
color_button_dec_label_hover = cl("#000000")

button_border_radius = 15

counter_style = {
    "IncrementButton::inc": {
        "background_color": color_button_inc_default,
        "border_radius": button_border_radius,
    },
    "IncrementButton::inc:hovered": {
        "background_color": color_button_inc_hover,
    },
    "IncrementButton.Label::inc": {
        "font_weight": "bold",
        "font_size": 24,
        "color": color_button_inc_label_default,
    },
    "IncrementButton.Label::inc:hovered": {
        "color": color_button_inc_label_hover,
    },
    "DecrementButton::dec": {
        "background_color": color_button_dec_default,
        "border_radius": button_border_radius,
    },
    "DecrementButton::dec:hovered": {
        "background_color": color_button_dec_hover,
    },
    "DecrementButton.Label::dec": {
        "font_weight": "bold",
        "font_size": 24,
        "color": color_button_dec_label_default,
    },
    "DecrementButton.Label::dec:hovered": {
        "color": color_button_dec_label_hover,
    },
}
