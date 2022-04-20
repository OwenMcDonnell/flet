import logging
from datetime import datetime
from time import sleep

import flet
from flet import Column, ElevatedButton, Image, Page, Row, Text, Theme, padding
from flet.progress_bar import ProgressBar
from flet.progress_ring import ProgressRing
from flet.stack import Stack

# logging.basicConfig(level=logging.DEBUG)


def main(page: Page):
    page.title = "Images Example"
    page.theme_mode = "light"
    page.padding = padding.all(10)
    page.update()

    pr = ProgressRing(width=16, height=16, stroke_width=2)
    pb = ProgressBar(width=400)

    page.add(
        Text("Circle progress indicator", style="headlineSmall"),
        Row([pr, Text("Wait for the completion...")]),
        Text("Indeterminate cicrular progress", style="headlineSmall"),
        Column(
            [ProgressRing(), Text("I'm going to run for ages...")],
            horizontal_alignment="center",
        ),
        Text("Linear progress indicator", style="headlineSmall"),
        Column([Text("Doing something..."), pb]),
        Text("Indeterminated progress bar", style="headlineSmall"),
        ProgressBar(width=400, color="amber", bgcolor="#eeeeee"),
    )

    for i in range(0, 101):
        pr.value = i * 0.01
        pb.value = i * 0.01
        sleep(0.1)
        page.update()


flet.app(name="test1", port=8550, target=main, view=flet.WEB_BROWSER)