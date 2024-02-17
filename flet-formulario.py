import flet as ft


def example(page):
    gender = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="feminino", label="Feminino"),
                ft.Radio(value="masculino", label="Masculino"),
                ft.Radio(value="not_specified", label="Outro"),
            ]
        )
    )

    def submit_form(e):
        e.control.page.dialog = dlg
        dlg.open = True
        e.control.page.update()
        print("Submit form")

    def close_dlg(e):
        dlg.open = False
        e.control.page.update()

    def validate_required_text_field(e):
        if e.control.value == "":
            e.control.error_text = "Campo Obrigatório"
            e.control.update()

    dlg = ft.AlertDialog(
        content=ft.Text("Obrigado!"),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
        on_dismiss=lambda e: print("Finalizado!"),
    )

    submit = ft.FilledButton("Enviar", on_click=submit_form)

    return ft.SafeArea(
        ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.TextField(
                    label="Nome",
                    keyboard_type=ft.KeyboardType.NAME,
                    on_blur=validate_required_text_field,
                ),
                ft.TextField(
                    label="Sobrenome",
                    keyboard_type=ft.KeyboardType.NAME,
                    on_blur=validate_required_text_field,
                ),
                ft.TextField(
                    label="E-mail",
                    keyboard_type=ft.KeyboardType.EMAIL,
                    on_blur=validate_required_text_field,
                ),
                ft.TextField(
                    label="Idade",
                    keyboard_type=ft.KeyboardType.NUMBER,
                    on_blur=validate_required_text_field,
                ),
                ft.Text("Gênero:"),
                gender,
                ft.Divider(thickness=1),
                ft.Row(controls=[submit], alignment=ft.MainAxisAlignment.CENTER),
            ],
        ),
        expand=True,
    )


def main(page: ft.Page):
    page.title = "Formulário"
    page.window_width = 390
    page.window_height = 844
    page.add(example(main))


if __name__ == "__main__":
    ft.app(target=main)