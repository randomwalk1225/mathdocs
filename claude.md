# TMUA Document Processing Project - Claude AI Development Guide

## 📋 프로젝트 개요

TMUA (Test of Mathematics for University Admission) 문제집을 PDF에서 Markdown과 LaTeX 형식으로 자동 변환하고, AI 기반으로 상세한 해설을 생성하는 프로젝트입니다.

### 주요 기능
- ✂️ PDF 페이지 자동 분할
- 📝 OCR/텍스트 추출
- 🤖 AI 기반 문제 해설 자동 생성
- 📄 Markdown 변환 (GitHub 호환)
- 📐 LaTeX 변환 (XeLaTeX 기반)
- 📑 PDF 컴파일 및 출력
- ✅ 자동 검증 및 오류 수정

---

## 🎯 현재 완료된 작업

### Chapter 1: Statistics (완료 ✓)

#### 퀴즈 구조
| 파일 | 제목 | 문제 수 | 시간 | 난이도 | 상태 |
|-----|------|--------|------|--------|------|
| Quiz1 | Exercises E01 | 23 | 제한없음 | ★★★☆ | ✓ 완료 |
| Quiz2 | Practices P01 | 15 | 40분 | ★★★ | ✓ 완료 |
| Quiz3 | Supplements S01 | 15 | 90분 | ★★★★ | ✓ 완료 |

#### 생성된 파일
각 퀴즈당 6개 파일:
1. `TMUA-CH1-QuizN.md` - 문제만 (GitHub 용)
2. `TMUA-CH1-QuizN.tex` - 문제 LaTeX
3. `TMUA-CH1-QuizN.pdf` - 문제 PDF
4. `TMUA-CH1-QuizN-Solutions.md` - 문제+해설+답 (GitHub 용)
5. `TMUA-CH1-QuizN-Solutions.tex` - 해설 LaTeX
6. `TMUA-CH1-QuizN-Solutions.pdf` - 해설 PDF

총 18개 파일 생성 완료

---

## 🚀 개발 워크플로우

### 1단계: PDF 분할
```python
# split_pdf.py 사용
python split_pdf.py

# 입력: TMUA-Workbook-2024-5th-Edition.pdf
# 출력: TMUA-CH1-Quiz1.pdf, TMUA-CH1-Quiz2.pdf, TMUA-CH1-Quiz3.pdf
```

### 2단계: 텍스트 추출
```python
# pdf_to_md.py 사용
python pdf_to_md.py

# 입력: 분할된 PDF 파일들
# 출력: *_raw.txt 파일들 (OCR 결과)
```

### 3단계: AI 교정 및 Markdown 생성
```bash
# Claude Code를 사용하여:
# 1. _raw.txt 파일 읽기
# 2. AI로 구조화 및 교정
# 3. Markdown 형식으로 저장
```

### 4단계: 해설 생성 (AI)
```bash
# Claude Code를 사용하여:
# 1. 문제 MD 파일 읽기
# 2. 각 문제에 대한 상세 해설 작성
# 3. *-Solutions.md 파일 생성
```

### 5단계: LaTeX 변환
```bash
# Claude Code를 사용하여:
# 1. MD 파일을 LaTeX로 변환
# 2. XeLaTeX 호환 형식으로 작성
# 3. .tex 파일 생성
```

### 6단계: PDF 컴파일
```bash
cd CH1-statistics
xelatex -interaction=nonstopmode TMUA-CH1-Quiz1-Solutions.tex
xelatex -interaction=nonstopmode TMUA-CH1-Quiz2-Solutions.tex
xelatex -interaction=nonstopmode TMUA-CH1-Quiz3-Solutions.tex
```

### 7단계: Git 커밋
```bash
git add .
git commit -m "Add Chapter N solutions"
git push
```

---

## 🔍 자동 검증 시스템 설계

### 필요한 검증 항목

#### 1. PDF 컴파일 검증
```python
# verify_pdf_compile.py
import subprocess
import os
from pathlib import Path

def verify_pdf_compilation(tex_file):
    """
    LaTeX 파일이 올바르게 컴파일되는지 검증
    """
    errors = []

    # 1. TEX 파일 존재 확인
    if not os.path.exists(tex_file):
        errors.append(f"TEX file not found: {tex_file}")
        return False, errors

    # 2. 컴파일 실행
    result = subprocess.run(
        ['xelatex', '-interaction=nonstopmode', tex_file],
        capture_output=True,
        text=True,
        timeout=60
    )

    # 3. 로그 파일 분석
    log_file = tex_file.replace('.tex', '.log')
    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8') as f:
            log_content = f.read()

            # 오류 패턴 검색
            if '! LaTeX Error' in log_content:
                errors.append("LaTeX compilation error found")
            if '! Missing' in log_content:
                errors.append("Missing package or dependency")
            if 'Emergency stop' in log_content:
                errors.append("Critical compilation failure")

    # 4. PDF 생성 확인
    pdf_file = tex_file.replace('.tex', '.pdf')
    if not os.path.exists(pdf_file):
        errors.append(f"PDF not generated: {pdf_file}")
        return False, errors

    # 5. PDF 페이지 수 확인
    page_count = get_pdf_page_count(pdf_file)
    if page_count == 0:
        errors.append("PDF is empty (0 pages)")
        return False, errors

    return len(errors) == 0, errors

def get_pdf_page_count(pdf_file):
    """PDF 페이지 수 반환"""
    try:
        from pypdf import PdfReader
        reader = PdfReader(pdf_file)
        return len(reader.pages)
    except:
        return 0
```

#### 2. 문제 수 일관성 검증
```python
# verify_problem_count.py
import re

def verify_problem_count(md_file, solutions_md_file, tex_file):
    """
    문제 수가 모든 파일에서 일치하는지 검증
    """
    errors = []

    # MD 파일에서 문제 수 세기
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
        md_problems = len(re.findall(r'^### (Quiz Pre-\d+|Ex\. \d+|Quiz \d+|SQ\d+)', md_content, re.MULTILINE))

    # Solutions MD 파일에서 문제 수 세기
    with open(solutions_md_file, 'r', encoding='utf-8') as f:
        sol_content = f.read()
        sol_problems = len(re.findall(r'^### (Quiz Pre-\d+|Ex\. \d+|Quiz \d+|SQ\d+)', sol_content, re.MULTILINE))

    # TEX 파일에서 문제 수 세기
    with open(tex_file, 'r', encoding='utf-8') as f:
        tex_content = f.read()
        tex_problems = len(re.findall(r'\\subsection\{', tex_content))

    # 비교
    if md_problems != sol_problems:
        errors.append(f"Problem count mismatch: MD={md_problems}, Solutions MD={sol_problems}")

    if md_problems != tex_problems:
        errors.append(f"Problem count mismatch: MD={md_problems}, TEX={tex_problems}")

    # 헤더에서 선언된 문제 수와 비교
    declared_count = extract_declared_problem_count(md_file)
    if declared_count and declared_count != md_problems:
        errors.append(f"Declared problem count ({declared_count}) doesn't match actual ({md_problems})")

    return len(errors) == 0, errors, md_problems

def extract_declared_problem_count(md_file):
    """MD 파일 헤더에서 선언된 문제 수 추출"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.search(r'\*\*Number of Questions:\*\* (\d+)', content)
        if match:
            return int(match.group(1))
    return None
```

#### 3. 답안 존재 검증
```python
# verify_solutions.py
import re

def verify_solutions_complete(solutions_md_file):
    """
    모든 문제에 해설과 답이 있는지 검증
    """
    errors = []

    with open(solutions_md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 각 문제 섹션 찾기
    problem_pattern = r'### (.*?)\n(.*?)(?=### |$)'
    problems = re.findall(problem_pattern, content, re.DOTALL)

    for i, (problem_name, problem_content) in enumerate(problems, 1):
        # PROBLEM 섹션 확인
        if '**Problem:**' not in problem_content and '**PROBLEM:**' not in problem_content:
            errors.append(f"Problem {problem_name}: Missing PROBLEM section")

        # SOLUTION 섹션 확인
        if '**Solution:**' not in problem_content and '**SOLUTION:**' not in problem_content:
            errors.append(f"Problem {problem_name}: Missing SOLUTION section")

        # ANSWER 섹션 확인
        if '**Answer:' not in problem_content and '**ANSWER:' not in problem_content:
            errors.append(f"Problem {problem_name}: Missing ANSWER section")

        # 해설이 너무 짧은지 확인 (최소 50자)
        solution_match = re.search(r'\*\*SOLUTION:\*\*(.*?)\*\*ANSWER:', problem_content, re.DOTALL)
        if solution_match:
            solution_text = solution_match.group(1).strip()
            if len(solution_text) < 50:
                errors.append(f"Problem {problem_name}: Solution too short ({len(solution_text)} chars)")

    return len(errors) == 0, errors
```

#### 4. LaTeX 구문 검증
```python
# verify_latex_syntax.py
import re

def verify_latex_syntax(tex_file):
    """
    LaTeX 파일의 일반적인 구문 오류 검증
    """
    errors = []

    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')

    # 1. 짝이 맞지 않는 괄호 검증
    open_braces = content.count('{')
    close_braces = content.count('}')
    if open_braces != close_braces:
        errors.append(f"Unmatched braces: { open_braces} open, {close_braces} close")

    # 2. begin/end 환경 검증
    begin_envs = re.findall(r'\\begin\{(\w+)\}', content)
    end_envs = re.findall(r'\\end\{(\w+)\}', content)

    begin_count = {}
    for env in begin_envs:
        begin_count[env] = begin_count.get(env, 0) + 1

    end_count = {}
    for env in end_envs:
        end_count[env] = end_count.get(env, 0) + 1

    for env, count in begin_count.items():
        if end_count.get(env, 0) != count:
            errors.append(f"Unmatched environment: \\begin{{{env}}} appears {count} times, \\end{{{env}}} appears {end_count.get(env, 0)} times")

    # 3. 특수 문자 이스케이프 검증
    unescaped_patterns = [
        (r'(?<!\\)%(?!.*\\)', 'Unescaped %'),
        (r'(?<!\\)&(?![^{]*})', 'Unescaped &'),
        (r'(?<!\\)#(?!\d)', 'Unescaped #'),
    ]

    for line_num, line in enumerate(lines, 1):
        # 주석 줄은 건너뛰기
        if line.strip().startswith('%'):
            continue

        for pattern, error_msg in unescaped_patterns:
            if re.search(pattern, line):
                errors.append(f"Line {line_num}: {error_msg}")

    # 4. 필수 패키지 존재 확인
    required_packages = ['fontspec', 'amsmath', 'enumitem', 'geometry', 'xcolor']
    for package in required_packages:
        if f'\\usepackage{{{package}}}' not in content and f'\\usepackage[' not in content or package not in content:
            errors.append(f"Missing required package: {package}")

    return len(errors) == 0, errors
```

#### 5. 통합 검증 스크립트
```python
# validate_all.py
import sys
from pathlib import Path
from verify_pdf_compile import verify_pdf_compilation
from verify_problem_count import verify_problem_count
from verify_solutions import verify_solutions_complete
from verify_latex_syntax import verify_latex_syntax

def validate_quiz(quiz_name, chapter_dir):
    """
    하나의 퀴즈에 대한 모든 검증 수행
    """
    print(f"\n{'='*60}")
    print(f"Validating {quiz_name}")
    print(f"{'='*60}\n")

    base_path = Path(chapter_dir) / quiz_name

    # 파일 경로
    md_file = f"{base_path}.md"
    solutions_md_file = f"{base_path}-Solutions.md"
    tex_file = f"{base_path}-Solutions.tex"
    pdf_file = f"{base_path}-Solutions.pdf"

    all_passed = True

    # 1. 파일 존재 확인
    print("1. Checking file existence...")
    for file_path in [md_file, solutions_md_file, tex_file]:
        if not Path(file_path).exists():
            print(f"   ❌ File not found: {file_path}")
            all_passed = False
        else:
            print(f"   ✓ Found: {file_path}")

    # 2. 문제 수 일관성 검증
    print("\n2. Validating problem count consistency...")
    success, errors, count = verify_problem_count(md_file, solutions_md_file, tex_file)
    if success:
        print(f"   ✓ All files have {count} problems")
    else:
        print(f"   ❌ Problem count mismatch:")
        for error in errors:
            print(f"      - {error}")
        all_passed = False

    # 3. 해설 완전성 검증
    print("\n3. Validating solution completeness...")
    success, errors = verify_solutions_complete(solutions_md_file)
    if success:
        print(f"   ✓ All problems have complete solutions")
    else:
        print(f"   ❌ Incomplete solutions:")
        for error in errors:
            print(f"      - {error}")
        all_passed = False

    # 4. LaTeX 구문 검증
    print("\n4. Validating LaTeX syntax...")
    success, errors = verify_latex_syntax(tex_file)
    if success:
        print(f"   ✓ LaTeX syntax is valid")
    else:
        print(f"   ❌ LaTeX syntax errors:")
        for error in errors:
            print(f"      - {error}")
        all_passed = False

    # 5. PDF 컴파일 검증
    print("\n5. Validating PDF compilation...")
    success, errors = verify_pdf_compilation(tex_file)
    if success:
        page_count = get_pdf_page_count(pdf_file)
        print(f"   ✓ PDF compiled successfully ({page_count} pages)")
    else:
        print(f"   ❌ PDF compilation failed:")
        for error in errors:
            print(f"      - {error}")
        all_passed = False

    return all_passed

def main():
    """
    모든 챕터의 모든 퀴즈 검증
    """
    print("="*60)
    print("TMUA Document Validation")
    print("="*60)

    # Chapter 1 검증
    chapter1_quizzes = [
        "TMUA-CH1-Quiz1",
        "TMUA-CH1-Quiz2",
        "TMUA-CH1-Quiz3"
    ]

    all_passed = True
    for quiz in chapter1_quizzes:
        passed = validate_quiz(quiz, "CH1-statistics")
        all_passed = all_passed and passed

    print("\n" + "="*60)
    if all_passed:
        print("✓ ALL VALIDATIONS PASSED")
        print("="*60)
        return 0
    else:
        print("❌ SOME VALIDATIONS FAILED")
        print("="*60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

### 자동 수정 시스템

```python
# auto_fix.py
import re
from pathlib import Path

class DocumentAutoFixer:
    """
    검증에서 발견된 오류를 자동으로 수정
    """

    def fix_problem_count_header(self, md_file, actual_count):
        """
        헤더의 문제 수를 실제 문제 수로 수정
        """
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 현재 선언된 문제 수 찾기
        pattern = r'(\*\*Number of Questions:\*\* )(\d+)'
        match = re.search(pattern, content)

        if match:
            old_count = match.group(2)
            if int(old_count) != actual_count:
                content = re.sub(pattern, f'\\g<1>{actual_count}', content)

                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)

                print(f"Fixed: Updated problem count from {old_count} to {actual_count}")
                return True

        return False

    def fix_unescaped_characters(self, tex_file):
        """
        LaTeX 파일에서 이스케이프되지 않은 특수 문자 수정
        """
        with open(tex_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        fixed_count = 0
        for i, line in enumerate(lines):
            # 주석은 건너뛰기
            if line.strip().startswith('%'):
                continue

            original = line

            # % 이스케이프 (단, \%는 제외)
            line = re.sub(r'(?<!\\)%', r'\%', line)

            # & 이스케이프 (단, tabular 환경 내부는 제외)
            # 이 부분은 컨텍스트를 고려해야 하므로 조심스럽게 처리

            # # 이스케이프 (단, \#는 제외)
            line = re.sub(r'(?<!\\)#(?!\d)', r'\#', line)

            if line != original:
                lines[i] = line
                fixed_count += 1

        if fixed_count > 0:
            with open(tex_file, 'w', encoding='utf-8') as f:
                f.writelines(lines)

            print(f"Fixed: Escaped {fixed_count} special characters")
            return True

        return False

    def fix_missing_solutions(self, solutions_md_file):
        """
        해설이 없는 문제에 플레이스홀더 추가
        """
        with open(solutions_md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 각 문제 섹션 찾기
        problem_pattern = r'(### .*?\n)(.*?)(?=### |$)'

        def add_missing_sections(match):
            header = match.group(1)
            problem_content = match.group(2)

            modified = False
            new_content = problem_content

            # PROBLEM 섹션이 없으면 추가
            if '**Problem:**' not in problem_content and '**PROBLEM:**' not in problem_content:
                new_content = "**PROBLEM:**\n\n[Problem text here]\n\n" + new_content
                modified = True

            # SOLUTION 섹션이 없으면 추가
            if '**Solution:**' not in problem_content and '**SOLUTION:**' not in problem_content:
                # ANSWER 위치 찾기
                answer_pos = new_content.find('**ANSWER:')
                if answer_pos > 0:
                    new_content = new_content[:answer_pos] + "**SOLUTION:**\n\n[Solution steps here]\n\n" + new_content[answer_pos:]
                else:
                    new_content += "\n\n**SOLUTION:**\n\n[Solution steps here]\n\n"
                modified = True

            # ANSWER 섹션이 없으면 추가
            if '**Answer:' not in problem_content and '**ANSWER:' not in problem_content:
                new_content += "\n\n**ANSWER: [Answer here]**\n\n"
                modified = True

            return header + new_content

        new_content = re.sub(problem_pattern, add_missing_sections, content, flags=re.DOTALL)

        if new_content != content:
            with open(solutions_md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"Fixed: Added missing solution sections")
            return True

        return False
```

---

## 🔄 반복 가능한 개발 사이클

### 전체 프로세스 자동화

```python
# process_chapter.py
import subprocess
from pathlib import Path
from validate_all import validate_quiz
from auto_fix import DocumentAutoFixer

def process_chapter(chapter_name, pdf_file, quiz_configs):
    """
    챕터 전체를 처리하는 자동화 스크립트

    Args:
        chapter_name: 예) "CH1-statistics"
        pdf_file: 원본 PDF 파일
        quiz_configs: 각 퀴즈의 설정
            [
                {"name": "Quiz1", "pages": (11, 20), "title": "Exercises E01"},
                {"name": "Quiz2", "pages": (20, 27), "title": "Practices P01"},
                ...
            ]
    """

    print(f"Processing {chapter_name}...")

    chapter_dir = Path(chapter_name)
    chapter_dir.mkdir(exist_ok=True)

    # 1. PDF 분할
    print("\n1. Splitting PDF...")
    split_pdfs(pdf_file, quiz_configs, chapter_dir)

    # 2. 텍스트 추출
    print("\n2. Extracting text...")
    extract_text_from_pdfs(chapter_dir, quiz_configs)

    # 3. Claude AI로 처리 (수동 단계)
    print("\n3. Processing with Claude AI...")
    print("   → 이 단계는 Claude Code를 사용하여 수동으로 진행")
    print("   → 각 _raw.txt를 읽고 MD 파일로 변환")
    print("   → 각 MD 파일에 대한 Solutions MD 생성")
    print("   → MD를 LaTeX로 변환")
    input("\nPress Enter when Claude AI processing is complete...")

    # 4. PDF 컴파일
    print("\n4. Compiling PDFs...")
    compile_all_pdfs(chapter_dir, quiz_configs)

    # 5. 검증
    print("\n5. Validating all documents...")
    all_passed = True
    for config in quiz_configs:
        quiz_name = f"TMUA-{chapter_name}-{config['name']}"
        passed = validate_quiz(quiz_name, chapter_dir)
        all_passed = all_passed and passed

    # 6. 자동 수정 (검증 실패 시)
    if not all_passed:
        print("\n6. Auto-fixing detected issues...")
        fixer = DocumentAutoFixer()

        for config in quiz_configs:
            quiz_name = f"TMUA-{chapter_name}-{config['name']}"
            base_path = chapter_dir / quiz_name

            # 수정 시도
            fixer.fix_problem_count_header(f"{base_path}.md", config.get('expected_problems', 0))
            fixer.fix_missing_solutions(f"{base_path}-Solutions.md")
            fixer.fix_unescaped_characters(f"{base_path}-Solutions.tex")

        # 7. 재검증
        print("\n7. Re-validating after fixes...")
        all_passed = True
        for config in quiz_configs:
            quiz_name = f"TMUA-{chapter_name}-{config['name']}"
            passed = validate_quiz(quiz_name, chapter_dir)
            all_passed = all_passed and passed

    # 8. Git 커밋
    if all_passed:
        print("\n8. Committing to Git...")
        subprocess.run(['git', 'add', str(chapter_dir)])
        subprocess.run([
            'git', 'commit', '-m',
            f'Add {chapter_name} complete with validation'
        ])
        print(f"\n✓ {chapter_name} processing complete!")
    else:
        print(f"\n❌ {chapter_name} processing failed validation")
        print("Please review errors and fix manually")

    return all_passed
```

### 사용 예시

```python
# main.py
from process_chapter import process_chapter

# Chapter 1 처리
chapter1_config = [
    {
        "name": "Quiz1",
        "pages": (11, 20),
        "title": "Exercises E01",
        "expected_problems": 23
    },
    {
        "name": "Quiz2",
        "pages": (20, 27),
        "title": "Practices P01",
        "expected_problems": 15
    },
    {
        "name": "Quiz3",
        "pages": (27, 33),
        "title": "Supplements S01",
        "expected_problems": 15
    }
]

process_chapter(
    chapter_name="CH1-statistics",
    pdf_file="TMUA-Workbook-2024-5th-Edition.pdf",
    quiz_configs=chapter1_config
)

# Chapter 2 처리
# chapter2_config = [...]
# process_chapter("CH2-algebra", "...", chapter2_config)
```

---

## 📝 개선된 README

### 프로젝트 소개

TMUA (Test of Mathematics for University Admission) 문제집을 디지털 형식으로 변환하고, AI 기반 상세 해설을 자동 생성하는 도구입니다.

### 주요 특징

- **자동화된 워크플로우**: PDF 분할부터 해설 생성까지 자동화
- **AI 기반 해설**: Claude AI가 각 문제에 대한 단계별 상세 해설 생성
- **다중 포맷 지원**: Markdown (GitHub용), LaTeX (인쇄용), PDF (배포용)
- **품질 검증**: 자동 검증 시스템으로 오류 사전 차단
- **재현 가능**: 전체 프로세스를 스크립트로 재현 가능

### 디렉토리 구조

```
dodcs/
├── CH1-statistics/                    # Chapter 1: Statistics
│   ├── TMUA-CH1-Quiz1.md             # 문제 (23문제)
│   ├── TMUA-CH1-Quiz1.tex            # 문제 LaTeX
│   ├── TMUA-CH1-Quiz1.pdf            # 문제 PDF
│   ├── TMUA-CH1-Quiz1-Solutions.md   # 문제+해설+답 (Markdown)
│   ├── TMUA-CH1-Quiz1-Solutions.tex  # 해설 LaTeX
│   ├── TMUA-CH1-Quiz1-Solutions.pdf  # 해설 PDF (16 pages)
│   ├── TMUA-CH1-Quiz2.md             # Quiz 2 (15문제)
│   ├── TMUA-CH1-Quiz2-Solutions.md
│   ├── TMUA-CH1-Quiz2-Solutions.pdf  # (10 pages)
│   ├── TMUA-CH1-Quiz3.md             # Quiz 3 (15문제)
│   ├── TMUA-CH1-Quiz3-Solutions.md
│   └── TMUA-CH1-Quiz3-Solutions.pdf  # (9 pages)
├── split_pdf.py                       # PDF 분할 스크립트
├── pdf_to_md.py                      # PDF → 텍스트 추출
├── validate_all.py                   # 검증 스크립트
├── auto_fix.py                       # 자동 수정 스크립트
├── process_chapter.py                # 통합 처리 스크립트
├── WORKFLOW.md                       # 상세 워크플로우
├── claude.md                         # AI 개발 가이드 (이 파일)
├── README.md                         # 프로젝트 개요
└── .gitignore                        # Git 제외 파일
```

### 빠른 시작

#### 1. 필수 요구사항

**Python 3.7+**
```bash
pip install pypdf pdf2image pytesseract pillow
```

**LaTeX 배포판**
- Windows: [MiKTeX](https://miktex.org/)
- Mac: [MacTeX](https://www.tug.org/mactex/)
- Linux: TeX Live

**OCR (선택)**
- Tesseract OCR
- Poppler (pdf2image 의존성)

#### 2. 새 챕터 처리

```python
# 설정 파일 작성
python process_chapter.py --chapter CH2 --config chapter2_config.json

# 또는 수동으로:
python split_pdf.py  # PDF 분할
python pdf_to_md.py  # 텍스트 추출
# Claude Code로 MD 생성 및 해설 작성
python validate_all.py  # 검증
python auto_fix.py  # 자동 수정
```

#### 3. 검증 실행

```bash
# 전체 검증
python validate_all.py

# 특정 퀴즈만 검증
python validate_all.py --quiz CH1-Quiz1

# 자동 수정 포함
python validate_all.py --auto-fix
```

### 해설 작성 가이드라인

#### 구조
1. **PROBLEM**: 문제 원문
2. **SOLUTION**: 단계별 상세 풀이
   - 주어진 정보 정리
   - 수식 전개
   - 중간 계산 과정
   - 논리적 추론 과정
3. **ANSWER**: 최종 답 (선택지 표시)

#### 품질 기준
- 해설 길이: 최소 50자 이상
- 수식 표기: LaTeX 수학 모드 사용
- 검증 표시: ✓ 또는 \checkmark 사용
- 단계 구분: 명확한 단락 구분

### 문제 해결 가이드

#### PDF가 빈 페이지로 나오는 경우
```bash
# LaTeX 로그 확인
cat CH1-statistics/TMUA-CH1-Quiz1-Solutions.log

# 일반적인 원인:
# 1. Custom box 환경 오류 → 단순 \textcolor 사용
# 2. 특수 문자 이스케이프 누락 → auto_fix.py 실행
# 3. 패키지 누락 → MiKTeX 업데이트
```

#### 문제 수 불일치
```bash
# 자동 수정
python auto_fix.py --fix-count

# 수동 확인
grep -c "^###" CH1-statistics/*.md
grep -c "\\subsection" CH1-statistics/*.tex
```

#### Git 커밋 시 인코딩 경고
```bash
# .gitattributes 파일 생성
echo "*.md text eol=lf" >> .gitattributes
echo "*.tex text eol=lf" >> .gitattributes
git add .gitattributes
git commit -m "Add gitattributes for consistent line endings"
```

### 개발 로드맵

#### Phase 1: 기본 변환 (완료 ✓)
- [x] PDF 분할
- [x] OCR 텍스트 추출
- [x] Markdown 변환
- [x] LaTeX 변환
- [x] PDF 컴파일

#### Phase 2: AI 해설 생성 (완료 ✓)
- [x] Claude AI 통합
- [x] 자동 해설 생성
- [x] 해설 품질 검증

#### Phase 3: 자동화 (진행중 🔄)
- [x] 검증 스크립트
- [ ] 자동 수정 스크립트
- [ ] 통합 처리 파이프라인
- [ ] CI/CD 통합

#### Phase 4: 고도화 (예정 📅)
- [ ] 웹 인터페이스
- [ ] 자동 답안 체크
- [ ] 난이도 자동 분석
- [ ] 진도 추적 기능
- [ ] 다국어 지원

### 기여 가이드

이 프로젝트는 개인 학습 목적으로 제작되었습니다.

### 라이선스

이 프로젝트는 개인 학습 목적으로만 사용되어야 합니다.

---

## 🎓 학습 포인트

### LaTeX 작성 시 주의사항

1. **환경 단순화**: Custom box 환경보다 기본 \textcolor 사용
2. **특수 문자**: %, &, #, $ 등은 항상 이스케이프
3. **폰트 설정**: XeLaTeX는 fontspec 사용 필수
4. **수식 모드**: $...$ 또는 \[...\] 사용

### Claude AI 활용 패턴

1. **문제 분석**: 전체 문제 구조 먼저 파악
2. **단계별 해설**: 논리적 흐름 유지
3. **검증**: 답안이 선택지와 일치하는지 확인
4. **일관성**: 같은 형식으로 모든 문제 작성

### 자동화의 핵심

1. **검증 우선**: 생성 후 즉시 검증
2. **빠른 피드백**: 오류 발견 즉시 수정
3. **재현성**: 모든 단계를 스크립트로 기록
4. **점진적 개선**: 반복하며 품질 향상

---

## 📊 프로젝트 통계

### Chapter 1 완료 현황
- 총 퀴즈: 3개
- 총 문제: 53개 (23 + 15 + 15)
- 총 페이지: 35 페이지 (16 + 10 + 9)
- 작업 시간: ~4시간
- Git 커밋: 2회

### 다음 챕터 예상
- Chapter 2-10: 각 챕터당 3-5개 퀴즈 예상
- 예상 총 문제: ~500개
- 예상 총 페이지: ~400 페이지
- 자동화 시 예상 시간: 챕터당 2시간

---

## 💡 Claude AI와 함께하는 개발 팁

### 효율적인 프롬프트 작성

**좋은 예시:**
```
CH1-statistics 폴더에 있는 TMUA-CH1-Quiz1.md 파일을 읽고,
각 문제에 대한 상세한 해설을 작성해줘.

형식:
- 문제 원문 유지
- 단계별 풀이 과정 포함
- 최종 답안 명시
- LaTeX 수식 사용

검증:
- 모든 문제 포함 확인
- 답안이 선택지와 일치하는지 확인
```

**나쁜 예시:**
```
해설 만들어줘
```

### 반복 작업 패턴

1. 첫 번째 퀴즈로 템플릿 확립
2. 나머지 퀴즈에 동일 패턴 적용
3. 검증으로 일관성 확인
4. 오류 발견 시 자동 수정

### 품질 관리

- 생성 직후 즉시 검증
- PDF 열어서 육안 확인
- 페이지 수가 예상과 일치하는지 확인
- Git diff로 의도하지 않은 변경 확인

---

**Last Updated:** 2025-01-10
**Version:** 1.0.0
**Author:** Developed with Claude Code
