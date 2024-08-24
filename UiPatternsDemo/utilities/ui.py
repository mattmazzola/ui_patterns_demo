import omni.kit.app
import omni.ui as ui


async def dock_window(
    target_window_title: str,
    docking_window_title: str,
    dock_position: ui.DockPosition,
    ratio: float = 0.5,
):
    await omni.kit.app.get_app().next_update_async()

    # Get window references
    target_window = ui.Workspace.get_window(target_window_title)
    docking_window = ui.Workspace.get_window(docking_window_title)

    # If windows exist, dock to target
    if docking_window and target_window:
        docking_window.dock_in(target_window, dock_position, ratio)

    await omni.kit.app.get_app().next_update_async()

    return docking_window
