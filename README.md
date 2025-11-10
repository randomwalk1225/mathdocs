# TMUA 문서 처리 프로젝트

TMUA (Test of Mathematics for University Admission) 워크북 PDF를 분할, OCR, 교정하여 마크다운과 LaTeX 형식으로 변환하는 자동화 프로젝트입니다.

## 프로젝트 개요

이 프로젝트는 다음과 같은 작업을 자동화합니다:

1. ✂️ **PDF 페이지 분할** - 큰 PDF를 챕터/섹션별로 분할
2. 📝 **OCR/텍스트 추출** - PDF에서 텍스트 추출
3. 🤖 **AI 교정** - 추출된 텍스트를 정리하고 포맷팅
4. 📄 **마크다운 변환** - 구조화된 마크다운 문서 생성
5. 📐 **LaTeX 변환** - 전문적인 수학 문서 포맷으로 변환
6. 📑 **PDF 컴파일** - 최종 PDF 문서 생성

## 디렉토리 구조

```
dodcs/
├── CH1-statistics/              # Chapter 1: Statistics
│   ├── TMUA-CH1-Quiz1.md       # Exercises E01 (23문제)
│   ├── TMUA-CH1-Quiz1.tex
│   ├── TMUA-CH1-Quiz1.pdf
│   ├── TMUA-CH1-Quiz2.md       # Practices P01 (15문제)
│   ├── TMUA-CH1-Quiz2.tex
│   ├── TMUA-CH1-Quiz2.pdf
│   ├── TMUA-CH1-Quiz3.md       # Supplements S01 (15문제)
│   ├── TMUA-CH1-Quiz3.tex
│   └── TMUA-CH1-Quiz3.pdf
├── split_pdf.py                 # PDF 분할 스크립트
├── pdf_to_md.py                # PDF → 텍스트 추출 스크립트
├── WORKFLOW.md                 # 상세 워크플로우 문서
├── README.md                   # 이 파일
└── TMUA-Workbook-2024-5th-Edition.pdf  # 원본 워크북
```

## 빠른 시작

### 필수 요구사항

1. **Python 3.7+**
2. **Python 패키지**
   ```bash
   pip install pypdf pdf2image pytesseract pillow
   ```

3. **LaTeX 배포판**
   - Windows: [MiKTeX](https://miktex.org/)
   - Mac: [MacTeX](https://www.tug.org/mactex/)
   - Linux: TeX Live

4. **Tesseract OCR** (OCR이 필요한 경우)
   - Windows: [Tesseract Installer](https://github.com/UB-Mannheim/tesseract/wiki)
   - Mac: `brew install tesseract`
   - Linux: `apt-get install tesseract-ocr`

5. **Poppler** (pdf2image 의존성)
   - Windows: [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/)
   - Mac: `brew install poppler`
   - Linux: `apt-get install poppler-utils`

### 사용 방법

#### 1. PDF 분할
```bash
python split_pdf.py
```

#### 2. 텍스트 추출
```bash
python pdf_to_md.py
```

#### 3. LaTeX → PDF 컴파일
```bash
cd CH1-statistics
xelatex -interaction=nonstopmode TMUA-CH1-Quiz1.tex
xelatex -interaction=nonstopmode TMUA-CH1-Quiz2.tex
xelatex -interaction=nonstopmode TMUA-CH1-Quiz3.tex
```

## 챕터별 내용

### Chapter 1: Statistics

| 파일 | 제목 | 문제 수 | 시간 | 난이도 |
|-----|------|--------|------|--------|
| Quiz1 | Exercises E01 | 23 | 제한없음 | ★★★☆ |
| Quiz2 | Practices P01 | 15 | 40분 | ★★★ |
| Quiz3 | Supplements S01 | 15 | 90분 | ★★★★ |

## 주요 기능

### 📝 마크다운 출력
- 깔끔한 계층 구조
- 일관된 포맷팅
- 표 및 리스트 지원
- 수식 표현 (이탤릭체)

### 📐 LaTeX 출력
- XeLaTeX 호환
- Times New Roman 폰트
- 전문적인 수학 표기
- 하이퍼링크 지원
- A4 용지 최적화

### 🎯 품질 보증
- AI 기반 텍스트 교정
- 일관된 포맷팅
- 오타 및 구조 오류 수정
- 수식 및 특수 문자 처리

## 상세 문서

더 자세한 워크플로우는 [WORKFLOW.md](WORKFLOW.md)를 참조하세요:

- 단계별 상세 프로세스
- 코드 예제
- 트러블슈팅 가이드
- 품질 관리 체크리스트

## 개발 히스토리

### 2025-01-10
- ✅ Chapter 1 Statistics 완료 (3개 퀴즈)
- ✅ PDF 분할 자동화
- ✅ OCR 텍스트 추출
- ✅ 마크다운 및 LaTeX 변환
- ✅ 워크플로우 문서화

## 향후 계획

- [ ] Chapter 2-10 처리
- [ ] 웹 인터페이스 개발
- [ ] 자동 답안 체크 기능
- [ ] 난이도별 문제 분류
- [ ] 진도 추적 기능

## 기여

이 프로젝트는 개인 학습 목적으로 제작되었습니다.

## 라이선스

원본 TMUA Workbook은 Xie Tao의 저작물입니다 (2024 5th Edition).
이 프로젝트는 개인 학습 목적으로만 사용되어야 합니다.

## 문의

문제가 발생하거나 제안사항이 있으면 Issue를 생성해주세요.

---

**Source:** Xie Tao TMUA Workbook 2024 (5th Edition)
**Last Updated:** 2025-01-10
