"""Download a PDF (if URL) or read a local PDF, extract text with PyMuPDF."""
import sys, os

def extract(pdf_path, output_dir):
    import fitz
    os.makedirs(output_dir, exist_ok=True)

    if pdf_path.startswith(('http://', 'https://')):
        import urllib.request
        filename = os.path.basename(pdf_path.split('?')[0])
        local_path = os.path.join(output_dir, filename)
        print(f'Downloading {pdf_path}')
        urllib.request.urlretrieve(pdf_path, local_path)
        pdf_path = local_path

    doc = fitz.open(pdf_path)
    text = ''
    for page in doc:
        text += f'\n--- PAGE {page.number + 1} ---\n'
        text += page.get_text()

    basename = os.path.splitext(os.path.basename(pdf_path))[0]
    txt_path = os.path.join(output_dir, basename + '.txt')
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f'Extracted {len(doc)} pages, {len(text)} chars -> {txt_path}')
    doc.close()
    return txt_path

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python extract_pdf.py <pdf-path-or-url> <output-dir>')
        print('Requires: pip install pymupdf')
        sys.exit(1)
    extract(sys.argv[1], sys.argv[2])
