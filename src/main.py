import flet as ft
import dataprotection as dn
from localisations import *
import asyncio


def main(page: ft.Page):
    hf = ft.HapticFeedback()

    async def heavy_impact():
        await hf.heavy_impact()

    async def medium_impact():
        await hf.medium_impact()

    async def light_impact():
        await hf.light_impact()

    async def vibrate():
        await hf.vibrate()

    page.auto_scroll = True
    dlg = ft.AlertDialog(
        title=ft.Text(dn.heading),
        content=ft.Column(controls=[ft.Text(dn.content)], scroll=ft.ScrollMode.ALWAYS),
        modal=True,
        actions=[ft.Button("OK", on_click=lambda e: page.pop_dialog())],
    )
    urllauncher = ft.UrlLauncher()
    page.update()

    async def github(e):
        await urllauncher.launch_url("https://github.com/tct123")

    async def dataprotection(e):
        await urllauncher.launch_url("https://tct123.github.io")

    def dataprotectionpopup(e):
        page.show_dialog(dlg)

    page.title = TITLE(page=page)

    # page.window_full_screen = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.adaptive = True
    page.appbar = ft.AppBar(
        title=ft.Text(str(page.title)),
        bgcolor=ft.Colors.BLUE,
        center_title=True,
        actions=[
            ft.PopupMenuButton(
                tooltip=MENUEHINTMSG(page=page),
                items=[
                    ft.PopupMenuItem(
                        content=ft.Text("GitHub"),
                        icon=ft.Icons.DEVELOPER_BOARD,
                        on_click=github,
                    ),
                    ft.PopupMenuItem(
                        content=ft.Text(DATAPROTECTIONITEM(page=page)),
                        icon=ft.Icons.WARNING,
                        on_click=dataprotectionpopup,
                    ),
                ],
            )
        ],
    )

    result = ft.TextField(
        text_align=ft.TextAlign.RIGHT,
        expand=1,
        read_only=True,
        border=ft.InputBorder.NONE,
    )

    async def btnclick(e: ft.Event) -> None:
        btn_text = e.control.content.value
        if btn_text == "C":
            await heavy_impact()
            result.value = ""
        elif btn_text == "=":
            try:
                await vibrate()
                result.value = str(eval(result.value))
            except:
                await heavy_impact()
                result.value = "Error"
        else:
            result.value += btn_text
        result.update()

    buttons = ["789/", "456*", "123-", "0.C+", "(=)"]
    page.add(ft.SafeArea(result))
    for row in buttons:
        row_controls = []
        for btntext in row:
            btn = ft.TextButton(content=ft.Text(btntext), on_click=btnclick, expand=1)
            row_controls.append(btn)
        page.add(
            ft.SafeArea(
                ft.Row(
                    controls=row_controls,
                    expand=1,
                )
            )
        )


ft.run(main)
