import os
from pypdf import PdfReader
from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(pdf_path):
    """PDF에서 텍스트를 추출. 텍스트가 없으면 OCR 사용"""
    reader = PdfReader(pdf_path)
    text = ""

    # 먼저 일반 텍스트 추출 시도
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    # 텍스트가 충분하지 않으면 OCR 사용
    if len(text.strip()) < 100:
        print(f"  OCR 사용 중 (텍스트가 충분하지 않음)...")
        try:
            images = convert_from_path(pdf_path, dpi=300)
            text = ""
            for i, image in enumerate(images):
                print(f"  페이지 {i+1} OCR 처리 중...")
                page_text = pytesseract.image_to_string(image, lang='eng')
                text += page_text + "\n"
        except Exception as e:
            print(f"  OCR 실패: {e}")

    return text

# 처리할 PDF 파일 목록
pdf_files = [
    "CH3-BasisOfLogic/TMUAworkbook-CH3-BasisOfLogic-quiz1.pdf",
    "CH3-BasisOfLogic/TMUAworkbook-CH3-BasisOfLogic-quiz2.pdf",
    "CH3-BasisOfLogic/TMUAworkbook-CH3-BasisOfLogic-quiz3.pdf"
]

# 각 PDF 파일 처리
for pdf_file in pdf_files:
    print(f"\n처리 중: {pdf_file}")

    # 텍스트 추출
    text = extract_text_from_pdf(pdf_file)

    # 임시 텍스트 파일로 저장 (AI 교정 전)
    txt_filename = pdf_file.replace(".pdf", "_raw.txt")
    # 출력 디렉토리 생성
    output_dir = os.path.dirname(txt_filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(txt_filename, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"  추출 완료: {len(text)} 문자")
    print(f"  저장됨: {txt_filename}")

print("\n\nCH3 텍스트 추출 완료! 이제 AI로 마크다운 변환을 진행합니다...")
