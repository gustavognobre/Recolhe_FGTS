import os
import re
import pdfplumber
import shutil
import locale

# Defina a localização para tratar os valores decimais com vírgula
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Pasta onde os PDFs estão localizados
pasta_pdfs = "C:\\Users\\gusta\\Downloads\\Teste"

# Pasta para onde os PDFs renomeados serão copiados
pasta_destino = "C:\\Users\\gusta\\Downloads\\Teste_Renomeados"

# Expressão regular para encontrar o padrão "Valor Recolhido: R$ número"
padrao_valor_recolhido = re.compile(r'Valor Recolhido:\s*R\$\s*([\d.,]+)', re.IGNORECASE)

# Cria a pasta de destino se ela não existir
os.makedirs(pasta_destino, exist_ok=True)

# Abre cada arquivo PDF na pasta
for nome_arquivo in os.listdir(pasta_pdfs):
    if nome_arquivo.lower().endswith(".pdf"):
        caminho_completo = os.path.join(pasta_pdfs, nome_arquivo)
        
        # Abre o PDF
        with pdfplumber.open(caminho_completo) as pdf:
            valor_recolhido = None
            
            # Extrai o texto de todas as páginas e procura pelo padrão "Valor Recolhido"
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                match = padrao_valor_recolhido.search(texto)
                if match:
                    valor_recolhido = match.group(1)
                    break
            
            if valor_recolhido is not None:
                # Converte o valor para um número decimal
                valor_decimal = locale.atof(valor_recolhido)
                
                # Formata o valor para usar no nome do arquivo
                valor_formatado = f"{valor_decimal:.2f}".replace(".", ",")
                
                # Novo nome do arquivo PDF com base no valor
                novo_nome = f"{valor_formatado}.pdf"
                
                # Novo caminho do arquivo na pasta de destino
                novo_caminho_destino = os.path.join(pasta_destino, novo_nome)
                
                try:
                    # Copia o arquivo para a pasta de destino
                    shutil.copy2(caminho_completo, novo_caminho_destino)
                    print(f"Arquivo renomeado e copiado: {nome_arquivo} -> {novo_nome}")
                except Exception as e:
                    print(f"Erro ao copiar o arquivo {nome_arquivo}: {e}")
            else:
                print(f"Valor Recolhido não encontrado no arquivo: {nome_arquivo}")
