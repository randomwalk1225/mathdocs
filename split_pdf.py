from pypdf import PdfReader, PdfWriter

# PDF 파일 경로
input_pdf = "TMUA-Workbook-2024-5th-Edition.pdf"

# 분할 설정 (페이지 번호는 0부터 시작하므로 -1)
splits = [
    {"pages": (11, 20), "filename": "TMUA-CH1-Quiz1.pdf"},  # 12-20
    {"pages": (20, 27), "filename": "TMUA-CH1-Quiz2.pdf"},  # 21-27
    {"pages": (27, 33), "filename": "TMUA-CH1-Quiz3.pdf"},  # 28-33
]

# PDF 읽기
reader = PdfReader(input_pdf)

# 각 분할 작업 수행
for split in splits:
    writer = PdfWriter()
    start, end = split["pages"]

    # 페이지 추가 (start는 포함, end는 포함)
    for page_num in range(start, end):
        writer.add_page(reader.pages[page_num])

    # 파일 저장
    output_filename = split["filename"]
    with open(output_filename, "wb") as output_file:
        writer.write(output_file)

    print(f"[OK] {output_filename} 생성 완료 (페이지 {start+1}-{end})")

print("\nPDF 분할 작업이 완료되었습니다!")
