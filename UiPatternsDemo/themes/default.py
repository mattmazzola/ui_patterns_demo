from .colors import (
    color_black,
    color_blue,
    color_blue_dark,
    color_gray,
    color_gray_dark,
    color_red,
    color_red_dark,
    color_white,
)

button_border_radius = 15

counter_style = {
    "Label::title": {
        "font_size": 24,
    },
    "Label::value": {
        "font_size": 24,
    },
    "IncrementButton::inc": {
        "border_color": color_white,
        "border_width": 2,
        "background_color": color_blue,
        "border_radius": button_border_radius,
    },
    "IncrementButton::inc:hovered": {
        "background_color": color_blue_dark,
        "border_color": color_gray,
    },
    "IncrementButton.Label::inc": {
        "font_weight": "bold",
        "font_size": 24,
        "color": color_gray,
    },
    "IncrementButton.Label::inc:hovered": {
        "color": color_white,
    },
    "DecrementButton::dec": {
        "border_color": color_black,
        "border_width": 2,
        "background_color": color_red,
        "border_radius": button_border_radius,
    },
    "DecrementButton::dec:hovered": {
        "background_color": color_red_dark,
    },
    "DecrementButton.Label::dec": {
        "font_weight": "bold",
        "font_size": 24,
        "color": color_gray_dark,
    },
    "DecrementButton.Label::dec:hovered": {
        "color": color_black,
    },
}

main_ui_style = {
    "Label::header": {
        "font_size": 32,
    },
    "Label::large": {
        "font_size": 28,
    },
}
