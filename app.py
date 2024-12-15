import flet as ft
from models import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = 'sqlite:///database.db'

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def main(page: ft.Page):
    page.title = "Flat-Python [Cadastro de Produtos]"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.ALWAYS

    # Definindo o tamanho da janela do app 
    page.window_width = 400 
    page.window_height = 600

    page.appbar = ft.AppBar(
        title=ft.Text("Flat-Python [Cadastro de Produtos]", color=ft.colors.WHITE),
        center_title=True,
        bgcolor=ft.colors.GREY_700,
    )
    lista_produtos = ft.ListView()



    def cadastrar(e):
        try:
            novo_produto = Produto(produto.value, preco.value)
            session.add(novo_produto)
            session.commit()
            lista_produtos.controls.append(
                ft.Container(
                    bgcolor=ft.colors.GREY_700,
                    padding=15,
                    margin=15,
                    border_radius=ft.border_radius.all(5),
                    content=ft.Text(f"{novo_produto.produto} - R$ {novo_produto.preco}"),
                )
            )
            txt_acerto.visible = True
            txt_erro.visible = False
            page.update()
            print("Produto cadastrado com sucesso")

        except:
            txt_erro.visible = True
            txt_acerto.visible = False
            print("Ocorreu um erro")
        
        # Limpar campos do formulário 
        produto.value = "" 
        preco.value = "" 
        produto.update() 
        preco.update()

            

    txt_titulo = ft.Text("Título da página")
    produto = ft.TextField(
        label="Digite o titulo do Produto", 
        text_align=ft.TextAlign.LEFT
        )
    preco = ft.TextField(
        label="Digite o preço do Produto", 
        text_align=ft.TextAlign.LEFT
        )
    btn_produto = ft.ElevatedButton(
        text="Adicionar Produto", 
        on_click=cadastrar, 
        icon=ft.icons.ADD,
        bgcolor=ft.colors.GREY_500,
        animate_scale=300
        )
    
    txt_erro = ft.Container(
        ft.Text("Ocorreu um erro"), 
        visible=False,
        bgcolor=ft.colors.RED,
        padding=10,
        )
    txt_acerto = ft.Container(
        ft.Text("Produto cadastrado com sucesso"), 
        visible=False,
        bgcolor=ft.colors.GREEN,
        padding=10,
    )
    page.add(
        txt_titulo,
        produto,
        preco,
        btn_produto,
        txt_erro,
        txt_acerto
        )
    
    for p in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                bgcolor=ft.colors.GREY_700,
                padding=15,
                margin=15,
                border_radius=ft.border_radius.all(5),
                content=ft.Text(f"{p.produto} - R$ {p.preco}"),
            )
        )
            #ft.Text(f"{p.produto} - R$ {p.preco}"))
    
    page.add(
        lista_produtos
    )

ft.app(target=main)