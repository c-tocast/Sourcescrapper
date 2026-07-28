import requests
from bs4 import BeautifulSoup
import os
import re

# Configuración de los archivos base
URLS_FILE = 'urls.txt'
KNOWLEDGE_DIR = 'knowledge'

def clean_filename(url):
    # Transforma la URL en un nombre de archivo válido
    name = re.sub(r'^https?://', '', url)
    name = re.sub(r'[^a-zA-Z0-9]', '_', name)
    return name.strip('_') + '.md'

def extract_clean_text(html_content):
    # Parseamos el HTML con BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 1. Eliminamos elementos que no contienen texto útil para el Gem
    for element in soup(["script", "style", "nav", "footer", "header", "aside"]):
        element.extract()
        
    # 2. Extraemos el texto separando los bloques con saltos de línea
    text = soup.get_text(separator='\n\n')
    
    # 3. Limpiamos los espacios en blanco excesivos para que el Markdown quede ordenado
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    clean_text = '\n'.join(chunk for chunk in chunks if chunk)
    
    return clean_text

def main():
    # Crea la carpeta knowledge si no existe
    os.makedirs(KNOWLEDGE_DIR, exist_ok=True)

    # Lee las URLs del archivo de texto
    with open(URLS_FILE, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]

    # Usamos un User-Agent (simulamos ser un navegador) para que Google no nos bloquee
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for url in urls:
        print(f"Procesando: {url}")
        
        try:
            # Hacemos la petición a la URL real
            response = requests.get(url, headers=headers)
            response.raise_for_status() 
            
            # Limpiamos el HTML usando nuestra función con BeautifulSoup
            content = extract_clean_text(response.text)
            
            # Generamos el archivo
            filename = clean_filename(url)
            filepath = os.path.join(KNOWLEDGE_DIR, filename)
            
            with open(filepath, 'w', encoding='utf-8') as md_file:
                # Añadimos un encabezado indicando de dónde salió la información
                md_file.write(f"# Fuente original: {url}\n\n")
                md_file.write(content)
                
            print(f"✅ Guardado con éxito en: {filepath}")
            
        except Exception as e:
            print(f"❌ Error al procesar {url}: {e}")

if __name__ == "__main__":
    main()
