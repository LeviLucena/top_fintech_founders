from typing import Dict

def compute_score(founder: Dict, base_score: float) -> float:
    """
    Calcula o score final do fundador com base no embedding (base_score)
    e outros critérios como número de funcionários, funding, menções, etc.
    """
    score = base_score

    # Ajuste por palavras-chave estratégicas
    keywords = ["open banking", "inclusão financeira", "pix", "blockchain", "embedded finance"]
    keyword_bonus = any(kw in founder["bio"].lower() for kw in keywords)
    if keyword_bonus:
        score += 0.1  # bonificação

    # Penalidade se faltar informações básicas
    if founder.get("name") == "Desconhecido" or founder.get("startup") == "Desconhecido":
        score -= 0.2

    # Exemplo de ajuste com base em quantidade de funcionários (se disponível futuramente)
    if "employees" in founder:
        if founder["employees"] > 100:
            score += 0.1
        elif founder["employees"] < 5:
            score -= 0.1

    return round(score, 4)
