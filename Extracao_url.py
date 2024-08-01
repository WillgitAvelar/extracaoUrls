import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_urls(base_url):
    # Envia uma solicitação para o site
    response = requests.get(base_url)
    # Analisa o conteúdo HTML do site
    soup = BeautifulSoup(response.text, 'html.parser')
    # Coleta todas as tags de link
    links = soup.find_all('a', href=True)
    
    # Extrai URLs completas
    urls = [urljoin(base_url, link['href']) for link in links]
    return urls

def generate_html(urls):
    # Gera o conteúdo HTML
    html_content = "<html><body><h1>Lista de URLs</h1><ul>"
    for url in urls:
        html_content += f'<li><a href="{url}">{url}</a></li>'
    html_content += "</ul></body></html>"
    return html_content

def save_to_html(content, filename="urls.html"):
    # Salva o conteúdo HTML em um arquivo
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    base_url = "cole aqui a url do site"  # Substitua pelo URL do site desejado
    urls = extract_urls(base_url)
    html_content = generate_html(urls)
    save_to_html(html_content)
    print(f"URLs extraídas e salvas em {base_url}")
