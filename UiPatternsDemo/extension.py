import gc
import os
import weakref
from pathlib import Path

import omni
import omni.kit.app
import omni.kit.commands
import omni.log
import omni.timeline
import omni.ui as ui
import omni.ui.workspace_utils
import omni.usd
from dotenv import load_dotenv
from omni.isaac.ui.element_wrappers import ScrollingWindow
from omni.isaac.ui.menu import make_menu_item_description
from omni.kit.menu.utils import add_menu_items, remove_menu_items

from .global_variables import EXTENSION_TITLE, MENU_BAR_BUTTON_NAME
from .ui_builder import UIBuilder


class Extension(omni.ext.IExt):

    def on_startup(self, ext_id: str):
        self.ext_id = ext_id
        self.ui_builder = UIBuilder()

        name = EXTENSION_TITLE

        extension_root = Path(__file__).parent.parent
        env_file_path = extension_root / ".env"
        load_dotenv(dotenv_path=env_file_path)
        is_debug = os.getenv("DEBUG", False) == "True"

        # Build Window
        self._window = ScrollingWindow(
            title=name,
            width=320,
            height=500,
            visible=is_debug,
            dockPreference=ui.DockPreference.LEFT_BOTTOM,
        )
        self._window.set_visibility_changed_fn(self._on_window)

        # Add menu item
        self._menu_items = [
            make_menu_item_description(self.ext_id, name, lambda a=weakref.proxy(self): a._menu_callback())
        ]

        add_menu_items(self._menu_items, MENU_BAR_BUTTON_NAME)

        # If debug, show winodow by default
        self._on_window(is_debug)

    def on_shutdown(self):
        omni.log.info(f"on_shutdown")
        remove_menu_items(self._menu_items, MENU_BAR_BUTTON_NAME)

        if self._window:
            self._window = None
        self.ui_builder.cleanup()
        gc.collect()

    def _on_window(self, visible: bool):
        omni.log.info(f"{self._on_window.__name__}: {visible}")
        if self._window.visible:
            self._build_ui()
        else:
            self.ui_builder.cleanup()

    def _build_ui(self):
        with self._window.frame:
            with ui.VStack(spacing=5, height=0):
                self._build_extension_ui()

        # asyncio.ensure_future(
        #     dock_window(
        #         target_window_title="Viewport",
        #         docking_window_title=EXTENSION_TITLE,
        #         dock_position=ui.DockPosition.LEFT,
        #         ratio=0.3,
        #     )
        # )

    def _menu_callback(self):
        self._window.visible = not self._window.visible

    def _build_extension_ui(self):
        self.ui_builder.build_ui()
