from playwright.sync_api import sync_playwright
import csv

def coleta():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        page = browser.new_page()
        page.goto("https://books.toscrape.com")

        lista_de_liros = list()
        while True:
            livros = page.locator("article.product_pod")
            for l in range(livros.count()):
                livro = livros.nth(l)

                nome = livro.locator('h3 a').get_attribute('title')
                preco = livro.locator('.price_color').inner_text()
                preco_arrumado = preco.replace('£', '')
                preco = float(preco_arrumado)
                aval = livro.locator('.star-rating').get_attribute('class')
                parte = aval.split()
                ava = parte[1]
                mapa = {
                    'One':1,
                    'Two':2,
                    'Three':3,
                    'Four':4,
                    'Five':5,

                }
                avaliacao = mapa[ava]

                categorias = {'nome':nome , 'preço':preco_arrumado , 'avaliação':avaliacao}
                lista_de_liros.append(categorias)

            if page.locator('li.next a').count() == 1:
                page.click('li.next a')
                page.wait_for_load_state('load')

            else:
                break

    arquivo = open('projeto_automação_livros.csv', 'w')
    writer = csv.DictWriter(arquivo, fieldnames=['nome', 'preço', 'avaliação'])
    writer.writeheader()
    for livro in lista_de_liros:
        writer.writerow(livro)
