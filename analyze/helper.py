import re, uuid, os
import pymupdf as fitz
from models.analysis import Analysis

def read_uploaded_file(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_data_analysis(resum_cv, job_id, resum_id, score) -> Analysis:
    secoes_dict = {
        "id": str(uuid.uuid4()),
        "job_id": job_id,
        "resum_id": resum_id,
        "name": "",
        "skills": [],
        "education": [],
        "languages": [],
        "score": score
    }

    patterns = {
        "name": r"(?:## Nome Completo\s*|Nome Completo\s*\|\s*Valor\s*\|\s*\S*\s*\|\s*)(.*)",
        "skills": r"## Habilidades\s*([\s\S]*?)(?=##|$)",
        "education": r"## Educação\s*([\s\S]*?)(?=##|$)",
        "languages": r"## Idiomas\s*([\s\S]*?)(?=##|$)",
        "salary_expectation": r"## Pretensão Salarial\s*([\s\S]*?)(?=##|$)"
    }

    def clean_string(string: str) -> str:
        return re.sub(r"[\*\-]+", "", string).strip()

    for secao, pattern in patterns.items():
        match = re.search(pattern, resum_cv)
        if match:
            if secao == "name":
                secoes_dict[secao] = clean_string(match.group(1))
            else:
                secoes_dict[secao] = [clean_string(item) for item in match.group(1).split('\n') if item.strip()]

    # Validação para garantir que nenhuma seção obrigatória esteja vazia
    for key in ["name", "education", "skills"]:
        if not secoes_dict[key] or (isinstance(secoes_dict[key], list) and not any(secoes_dict[key])):
            print(f"Erro: A seção '{key}' está vazia. Conteúdo atual: {secoes_dict[key]}")
            raise ValueError(f"A seção '{key}' não pode ser vazia ou uma string vazia.")

    return Analysis(**secoes_dict)

def get_pdf_paths(directory):
    pdf_files = []

    # Verifica se o diretório existe
    if not os.path.exists(directory):
        print(f"O diretório {directory} não existe.")
        return pdf_files

    # Percorre todos os arquivos no diretório especificado
    for filename in os.listdir(directory):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(directory, filename)
            pdf_files.append(file_path)

    # Se nenhum arquivo PDF for encontrado, imprime uma mensagem
    if not pdf_files:
        print(f"Nenhum arquivo PDF encontrado em {directory}")
    else:
        print(f"Encontrados {len(pdf_files)} arquivos PDF em {directory}")

    return pdf_files