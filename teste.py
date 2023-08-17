import os
import PyPDF2

# Palavra específica que você deseja procurar
palavra_especifica = "FGTS"

# Caminho para o PDF de entrada
pdf_entrada = "C:\\Users\\gusta\\Downloads\\09-01 PGTOS.pdf"

# Pasta para salvar os arquivos PDF separados
pasta_saida = "C:\\Users\\gusta\\Downloads\\Teste"

# Função para verificar se a página contém a palavra específica
def pagina_contem_palavra(pagina, palavra):
    return palavra.lower() in pagina.lower()

# Abre o PDF de entrada
with open(pdf_entrada, "rb") as pdf_ent:
    leitor = PyPDF2.PdfReader(pdf_ent)

    for num_pagina in range(len(leitor.pages)):
        pagina = leitor.pages[num_pagina]
        texto = pagina.extract_text()

        if pagina_contem_palavra(texto, palavra_especifica):
            escritor = PyPDF2.PdfWriter()
            escritor.add_page(pagina)

            # Cria um nome de arquivo único para cada página
            nome_arquivo_saida = os.path.join(pasta_saida, f"pagina_{num_pagina + 1}.pdf")

            # Salva a página em um arquivo PDF separado
            with open(nome_arquivo_saida, "wb") as pdf_sai:
                escritor.write(pdf_sai)

print("Páginas com a palavra específica foram salvas em arquivos PDF separados na pasta especificada.")
