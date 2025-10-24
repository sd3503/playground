# 코딩테스트 연습

Python으로 코딩테스트 문제들을 연습하는 저장소입니다.

## 🛠️ 프로젝트 설정

### 1. 프로젝트 클론

```bash
git clone https://github.com/[사용자명]/coding-test-practice.git
cd coding-test-practice
```

### 2. 가상환경 생성 및 활성화

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source venv/bin/activate
```

### 3. 의존성 설치 (필요시)

```bash
pip install -r requirements.txt
```

### 4. 프로젝트 실행

```bash
# 전체 문제 실행
python main.py

# 개별 문제 실행
python problems/array/two_sum.py
```

## 📁 구조

```
playground/
├── main.py                    # 메인 실행 파일
└── problems/                  # 문제 카테고리별 폴더
    ├── array/                # 배열 문제
    ├── string/               # 문자열 문제
    ├── math/                 # 수학 문제
    ├── sorting/              # 정렬 문제
    ├── searching/            # 탐색 문제
    ├── dp/                   # 동적계획법 문제
    ├── graph/                # 그래프 문제
    └── greedy/               # 그리디 문제
```

## 🚀 실행 방법

### 전체 문제 실행

```bash
python main.py
```

### 개별 문제 실행

```bash
# Array 문제
python problems/array/two_sum.py

# String 문제
python problems/string/valid_parentheses.py

# Math 문제
python problems/math/fibonacci.py
```

## 📝 문제 목록

### Array

- [x] Two Sum (LeetCode 1)

### String

- [x] Valid Parentheses (LeetCode 20)

### Math

- [x] Fibonacci

## 🔧 환경 설정

- Python 3.x
- UTF-8 인코딩 지원

## 📋 요구사항

- Python 3.7 이상
- Git (프로젝트 클론용)

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.
