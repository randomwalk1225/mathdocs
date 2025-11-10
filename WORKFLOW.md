# PDF 문서 처리 워크플로우

## 개요
PDF 문서를 분할하고, OCR로 텍스트를 추출한 후, AI로 교정하여 마크다운과 LaTeX 형식으로 변환하는 자동화된 워크플로우입니다.

## 전체 워크플로우

```
PDF 원본
   ↓
1. 페이지 분할
   ↓
2. OCR/텍스트 추출
   ↓
3. AI 교정 및 마크다운 변환
   ↓
4. LaTeX 변환
   ↓
5. PDF 컴파일
   ↓
6. 파일 정리
```

---

## 1단계: PDF 페이지 분할

### 도구
- Python 스크립트: `split_pdf.py`
- 라이브러리: `pypdf`

### 프로세스
```python
from pypdf import PdfReader, PdfWriter

# 분할 설정
splits = [
    {"pages": (11, 20), "filename": "output1.pdf"},  # 페이지 12-20
    {"pages": (20, 27), "filename": "output2.pdf"},  # 페이지 21-27
]

# PDF 읽기 및 분할
reader = PdfReader("input.pdf")
for split in splits:
    writer = PdfWriter()
    start, end = split["pages"]
    for page_num in range(start, end):
        writer.add_page(reader.pages[page_num])

    with open(split["filename"], "wb") as output:
        writer.write(output)
```

### 실행
```bash
pip install pypdf
python split_pdf.py
```

---

## 2단계: OCR/텍스트 추출

### 도구
- Python 스크립트: `pdf_to_md.py`
- 라이브러리: `pypdf`, `pdf2image`, `pytesseract`

### 프로세스
```python
from pypdf import PdfReader
from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    # 먼저 일반 텍스트 추출 시도
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    # 텍스트가 충분하지 않으면 OCR 사용
    if len(text.strip()) < 100:
        images = convert_from_path(pdf_path, dpi=300)
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image, lang='eng') + "\n"

    return text
```

### 실행
```bash
pip install pypdf pdf2image pytesseract pillow
python pdf_to_md.py
```

---

## 3단계: AI 교정 및 마크다운 변환

### 프로세스
추출된 텍스트를 읽고 AI로 다음 작업 수행:

1. **텍스트 정리**
   - 줄바꿈 오류 수정
   - 중복 공백 제거
   - 특수 문자 정규화

2. **구조화**
   - 제목 계층 구조 생성
   - 문제 번호별 섹션 분리
   - 선택지 포맷팅

3. **마크다운 포맷팅**
   - 헤더: `#`, `##`, `###`
   - 볼드: `**텍스트**`
   - 리스트: `-`, `*`
   - 수식: 이탤릭체 `*x*`, `*y*`
   - 표: 마크다운 테이블 형식

### 출력 형식
```markdown
# 제목

**Source:** 출처
**Time Allowed:** 시간
**Number of Questions:** 문제 수
**Difficulty:** 난이도

---

## 섹션

### 문제 1
문제 내용

- (A) 선택지 1
- (B) 선택지 2
```

---

## 4단계: LaTeX 변환

### 템플릿 구조

```latex
\documentclass[12pt,a4paper]{article}
\usepackage{fontspec}          % XeLaTeX 폰트
\usepackage{amsmath,amssymb}   % 수학 기호
\usepackage{enumitem}          % 리스트 커스터마이징
\usepackage{geometry}          % 페이지 레이아웃
\usepackage{titlesec}          % 제목 포맷
\usepackage{booktabs}          % 표 스타일
\usepackage{hyperref}          % 하이퍼링크

\geometry{margin=2.5cm}

\setmainfont{Times New Roman}
\setsansfont{Arial}

\title{\textbf{제목}}
\author{저자}
\date{}

\begin{document}
\maketitle

% 내용...

\end{document}
```

### 마크다운 → LaTeX 변환 규칙

| 마크다운 | LaTeX |
|---------|-------|
| `# 제목` | `\section*{제목}` |
| `## 부제목` | `\subsection*{부제목}` |
| `**볼드**` | `\textbf{볼드}` |
| `*이탤릭*` | `$이탤릭$` (수식) |
| `- 리스트` | `\begin{enumerate}...\end{enumerate}` |
| 표 | `\begin{tabular}...\end{tabular}` |

### 수학 표현

| 마크다운/텍스트 | LaTeX |
|---------------|-------|
| `x`, `y` | `$x$`, `$y$` |
| `⅓`, `½` | `$\frac{1}{3}$`, `$\frac{1}{2}$` |
| `√450` | `$\sqrt{450}$` |
| `7⁵` | `$7^5$` |
| `Q₁`, `Q₂` | `$Q_1$`, `$Q_2$` |

---

## 5단계: PDF 컴파일

### XeLaTeX 사용

```bash
# 단일 컴파일
xelatex -interaction=nonstopmode filename.tex

# 참조 업데이트를 위한 두 번 컴파일 (선택사항)
xelatex -interaction=nonstopmode filename.tex
xelatex -interaction=nonstopmode filename.tex
```

### 출력 파일
- `filename.pdf` - 최종 PDF
- `filename.aux` - 보조 파일
- `filename.log` - 로그 파일
- `filename.out` - 하이퍼링크 정보

---

## 6단계: 파일 정리 및 구조화

### 폴더 구조
```
project/
├── CH1-statistics/
│   ├── TMUA-CH1-Quiz1.md
│   ├── TMUA-CH1-Quiz1.tex
│   ├── TMUA-CH1-Quiz1.pdf
│   ├── TMUA-CH1-Quiz2.md
│   ├── TMUA-CH1-Quiz2.tex
│   ├── TMUA-CH1-Quiz2.pdf
│   ├── TMUA-CH1-Quiz3.md
│   ├── TMUA-CH1-Quiz3.tex
│   └── TMUA-CH1-Quiz3.pdf
├── split_pdf.py
├── pdf_to_md.py
├── WORKFLOW.md
├── README.md
└── TMUA-Workbook-2024-5th-Edition.pdf (원본)
```

### 정리 명령어
```bash
# 폴더 생성
mkdir -p CH1-statistics

# 파일 이동
mv TMUA-CH1-Quiz*.md CH1-statistics/
mv TMUA-CH1-Quiz*.tex CH1-statistics/
mv TMUA-CH1-Quiz*.pdf CH1-statistics/

# 불필요한 파일 삭제
rm -f *.aux *.log *.out *_raw.txt
```

---

## 품질 관리 체크리스트

### 텍스트 추출 후
- [ ] 모든 텍스트가 올바르게 추출되었는가?
- [ ] 특수 문자 (수학 기호 등)가 제대로 인식되었는가?
- [ ] 페이지 번호가 올바른가?

### 마크다운 변환 후
- [ ] 제목 계층 구조가 일관적인가?
- [ ] 모든 문제 번호가 올바른가?
- [ ] 선택지 레이블 (A, B, C...)이 정확한가?
- [ ] 표가 제대로 포맷팅되었는가?

### LaTeX 변환 후
- [ ] 모든 수식이 올바르게 변환되었는가?
- [ ] 특수 문자가 이스케이프 처리되었는가? (`%`, `&`, `$`, `#`)
- [ ] 폰트 설정이 올바른가?
- [ ] 페이지 레이아웃이 적절한가?

### PDF 컴파일 후
- [ ] PDF가 정상적으로 생성되었는가?
- [ ] 모든 페이지가 올바르게 렌더링되었는가?
- [ ] 수식과 기호가 제대로 표시되는가?
- [ ] 하이퍼링크가 작동하는가?

---

## 재사용 가능한 스크립트

### 빠른 시작 스크립트
```bash
#!/bin/bash
# quick_process.sh

# 1. PDF 분할
echo "1단계: PDF 분할 중..."
python split_pdf.py

# 2. 텍스트 추출
echo "2단계: 텍스트 추출 중..."
python pdf_to_md.py

# 3. LaTeX 컴파일
echo "3단계: PDF 컴파일 중..."
for texfile in *.tex; do
    xelatex -interaction=nonstopmode "$texfile"
done

# 4. 정리
echo "4단계: 파일 정리 중..."
rm -f *.aux *.log *.out *_raw.txt

echo "완료!"
```

---

## 트러블슈팅

### 문제: PDF 파일이 열려있어서 덮어쓸 수 없음
**해결방법:**
```bash
# 다른 이름으로 컴파일
xelatex -interaction=nonstopmode -jobname=filename-new filename.tex

# 또는 PDF 뷰어 닫기
```

### 문제: OCR 정확도가 낮음
**해결방법:**
- DPI 증가: `convert_from_path(pdf_path, dpi=600)`
- 이미지 전처리 (대비, 밝기 조정)
- 다른 OCR 엔진 사용 (Tesseract 언어 팩 업데이트)

### 문제: XeLaTeX 컴파일 오류
**해결방법:**
- 로그 파일 확인: `*.log`
- 패키지 업데이트: MiKTeX Console 사용
- 폰트 문제: 설치된 폰트 확인

### 문제: 한글 깨짐 (Windows)
**해결방법:**
- 파일 인코딩을 UTF-8로 저장
- Python 스크립트에서 `encoding='utf-8'` 명시

---

## 도구 및 요구사항

### Python 라이브러리
```bash
pip install pypdf pdf2image pytesseract pillow
```

### LaTeX 배포판
- **Windows**: MiKTeX
- **Mac**: MacTeX
- **Linux**: TeX Live

### 추가 도구
- **Tesseract OCR**: OCR 엔진
- **Poppler**: PDF 이미지 변환 (`pdf2image` 의존성)

---

## 참고 자료

- [pypdf Documentation](https://pypdf.readthedocs.io/)
- [pdf2image Documentation](https://github.com/Belval/pdf2image)
- [LaTeX Documentation](https://www.latex-project.org/)
- [XeLaTeX Guide](https://www.overleaf.com/learn/latex/XeLaTeX)
- [Markdown Guide](https://www.markdownguide.org/)

---

## 버전 관리

### Git 워크플로우
```bash
# 변경사항 추가
git add .

# 커밋
git commit -m "Add CH1 Statistics quizzes"

# 푸시 (원격 저장소가 있는 경우)
git push origin main
```

### 커밋 메시지 컨벤션
- `Add`: 새로운 파일/기능 추가
- `Update`: 기존 파일 수정
- `Fix`: 버그 수정
- `Remove`: 파일 삭제
- `Refactor`: 코드 리팩토링
- `Docs`: 문서 업데이트

---

## 라이선스 및 저작권

문서 처리 과정에서 저작권을 준수하세요:
- 원본 PDF의 저작권 확인
- 개인 학습 목적으로만 사용
- 재배포 시 원저작자 명시
