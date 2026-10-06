
import spacy
import re
import fitz
import time
from collections import Counter

TARGET_LABELS = {
    "COUNTRY",
    "FINANCIAL YEAR",
    "GDP GROWTH %",
    "GDP VALUE",
}

nlp = spacy.load("./EconomicReportModel")
nlp.max_length = 20_000_000

def extract_text_from_pdf(pdf_path: str) -> str | None:
    full_text_parts = []
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text = page.get_text()
            if text:
                full_text_parts.append(clean_and_normalize_text(text) + "\n")
        doc.close()
        return clean_and_normalize_text(" ".join(full_text_parts))
    except Exception as e:
        print(f"Could not process PDF '{pdf_path}': {e}")
        return None

def clean_and_normalize_text(text: str) -> str:
    return re.sub(r'\s+', ' ', text or '').strip()

def extract_fields(text: str, nlp):
    doc = nlp(text)
    
    country_candidates = []
    year_candidates = []
    gdp_growth_candidates = []
    gdp_value_candidates = []

    for ent in doc.ents:
        label = ent.label_
        value = ent.text.strip()

        if label in ["GPE", "LOC"]:
            country_candidates.append(value)

        elif label == "DATE":
            if re.search(r'(20\d{2}[-/–]\d{2})|(FY ?\d{2,4}[-/–]?\d{2,4})', value, re.I):
                year_candidates.append(value)
            elif re.search(r'20\d{2}', value):
                year_candidates.append(value)

        elif label == "PERCENT" and "gdp" in text.lower():
            gdp_growth_candidates.append(value)
        elif label == "PERCENT":
            gdp_growth_candidates.append(value)

        elif label in ["MONEY", "QUANTITY"]:
            if "gdp" in text.lower() or re.search(r'\bUSD\b|\$|trillion|billion|crore', value, re.I):
                gdp_value_candidates.append(value)

    # Fallback regex
    if not year_candidates:
        year_candidates = re.findall(r'FY ?\d{2,4}[-/–]?\d{2,4}|20\d{2}[-/–]\d{2,4}', text)
    if not gdp_growth_candidates:
        gdp_growth_candidates = re.findall(r'\b\d+(\.\d+)?\s?%\b', text)
    if not gdp_value_candidates:
        gdp_value_candidates = re.findall(r'(?:USD|Rs\.?|₹|\$)\s?\d+[.,]?\d*\s?(?:billion|million|crore|trillion)?', text, re.I)

    # Pick one of each
    country = Counter(country_candidates).most_common(1)[0][0] if country_candidates else None
    fin_year = year_candidates[0] if year_candidates else None
    gdp_growth = gdp_growth_candidates[0] if gdp_growth_candidates else None
    gdp_value = gdp_value_candidates[0] if gdp_value_candidates else None

    if fin_year:
        fin_year = re.sub(r'[A-Za-z]', '', fin_year).strip()
        # also clean multiple spaces or punctuation at ends
        fin_year = re.sub(r'[^0-9\-–/]', '', fin_year)

    results = {
        "COUNTRY": country,
        "FINANCIAL YEAR": fin_year,
        "GDP GROWTH %": gdp_growth,
        "GDP VALUE": gdp_value,
    }

    return results


if __name__ == "__main__":
    pdf_file = input("Enter the full path of the pdf : ").strip()
    inference_start_time = time.time()
    pdf_text = extract_text_from_pdf(pdf_file)
    cleaned_text = clean_and_normalize_text(pdf_text)
    output = extract_fields(cleaned_text, nlp)
    inference_end_time = time.time()

    print(f"\nTotal time taken for inference {inference_end_time - inference_start_time:.2f} seconds")
    print("\nApproximate extracted values:\n")
    for k, v in output.items():
        print(f"{k}: {v}")

