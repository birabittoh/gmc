from pypdf import PdfReader

def get_value(page_lines):
    for line in page_lines:
        if "EUR" in line:
            return int(line.split(" ")[2].replace(".00", ""))
        
def get_code(page_lines):
    for i, line in enumerate(page_lines):
        if "PIN:" in line:
            return page_lines[i + 1]

def get_website(page_lines: list[str]):
    for line in page_lines:
        if "Tipologia Ricarica:" in line:
            return line.split(" ")[3]

def get_codes(stream):
    codes = []
    for i, page in enumerate(PdfReader(stream).pages):
        if i % 2 == 1:
            continue

        page_text = page.extract_text()
        page_lines = page_text.split("\n")

        code = {
            "value": get_value(page_lines),
            "code": get_code(page_lines),
            "website": get_website(page_lines),
        }
        codes.append(code)
    return codes

def get_codes_working(stream):
    codes = []
    for i, page in enumerate(PdfReader(stream).pages):
        if i % 2 == 1:
            continue

        page_text = page.extract_text()
        page_lines = page_text.split("\n")

        code = {
            "value": int(page_lines[7].split(" ")[2].replace(".00", "")),
            "code": page_lines[6],
            "website": page_lines[8]
        }
        codes.append(code)
    return codes
