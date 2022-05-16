import logging
from time import sleep

import flet
from flet import Page, TextButton
from flet.alert_dialog import AlertDialog
from flet.elevated_button import ElevatedButton
from flet.text import Text

logging.basicConfig(level=logging.DEBUG)


def main(page: Page):
    page.title = "Dialog Example"
    page.update()

    dlg = AlertDialog(
        title=Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = AlertDialog(
        modal=True,
        title=Text("Please confirm"),
        content=Text("Do you really want to delete all those files?"),
        actions=[
            TextButton("Yes", on_click=close_dlg),
            TextButton("No", on_click=close_dlg),
        ],
        actions_alignment="end",
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()
        sleep(7)
        dlg.open = False
        page.update()

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
        sleep(7)
        dlg_modal.open = False
        page.update()

    page.add(
        ElevatedButton("Open dialog", on_click=open_dlg),
        ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
        Text("Line 1"),
        Text("Line 2"),
        Text("Line 3"),
        Text("Line 4"),
        Text("Line 5"),
        Text("Line 6"),
    )


flet.app(name="test1", port=8550, target=main, view=flet.WEB_BROWSER)
