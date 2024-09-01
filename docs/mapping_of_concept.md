# Mapping of Concepts

| React | Omniverse |
| --- | --- |
| **Styling** |  |
| class="my_class" | name="my_class" |
| .my_class { ... } | Element.my_class { ... } |
| id="my_id" | style_type_name_override="my_id" |
| my_id { ... } | MyId { ... } |
| **Layout** |  |
| flexbox, flex-direction: row, gap: gap | ui.VStack(spacing=gap) |
| flexbox, flex-direction: column, gap: gap | ui.HStack(spacing=gap) |
| position: absolute or z-index | ui.ZStack (implicit based on order) |
| **Elements** |  |
| \<button>\</button> | ui.Button(...) |
| \<textarea>\</textarea> | ui.TextBlock(...) |
| ... | ... |
| **State** |  |
| - **numbers** |
| const [value, setValue] = React.useState(initial_value) <br /> useEffect(onChanged, [value]) | model = ui.SimpleIntModel(initial_value) <br /> model.add_value_changed_fn(on_changed) |
| - **text** |  |
| [same of above]   | ui.SimpleStringModel(initial_value) |
| ... |   |
| **Modals** |  |
| \<dialog> \<React.portal> | ui.Window |
| **Components** |  |
| \<MyCounter onValueChanged={onCounterChanged} /> | my_counter = create_counter() <br /> my_counter.int_model.add_value_changed_fn(on_counter_changed) |
