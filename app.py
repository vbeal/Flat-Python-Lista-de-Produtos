import flet as ft

def main(page: ft.Page):
    page.title = "Flat-Python-estudo1"


    def cadastrar(e):
        page.add(ft.Text(f"Produto: {produto.value} - Preço: {preco.value}"))

    txt_titulo = ft.Text("Título da página")
    produto = ft.TextField(
        label="Digite o titulo do Produto", 
        text_align=ft.TextAlign.LEFT
        )
    preco = ft.TextField(
        label="Digite o preço do Produto", 
        text_align=ft.TextAlign.LEFT
        )
    btn_produto = ft.ElevatedButton("Adicionar Produto", on_click=cadastrar)
    page.add(
        txt_titulo,
        produto,
        preco,
        btn_produto
        )

ft.app(target=main)