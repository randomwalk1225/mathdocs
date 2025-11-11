좋아. 이제 그냥 **채팅창에서 읽기 쉽게 LaTeX 수식 그대로** 써줄게.

---

# “거의 정수(almost integer)”가 되는 ( a + b\sqrt{d} )의 조건

---

## 1️⃣ 문제 설정

우리가 찾고 싶은 건 다음과 같은 수입니다.

[
\alpha = a + b\sqrt{d}, \qquad \beta = a - b\sqrt{d}
]

이때 (\alpha^n)이 어떤 정수에 **지수적으로 가까워지는지** 알고 싶어요.
핵심은 다음 관계식입니다:

[
k_n = \alpha^n + \beta^n \in \mathbb{Z}
]
[
\alpha^n = k_n - \beta^n, \quad |\alpha^n - k_n| = |\beta|^n
]

즉, 만약 (|\beta| < 1)이고 (k_n)이 항상 정수라면,
(\alpha^n)은 정수에 지수적으로 가까워집니다.

---

## 2️⃣ 핵심 조건

[
\boxed{
\begin{aligned}
&\text{(1) } \alpha \text{는 대수적 정수이자 단위(unit)이다: } N(\alpha) = \alpha\beta = \pm1. \
&\text{(2) } \alpha > 1,\ |\beta| < 1.
\end{aligned}
}
]

이 두 조건이 성립하면,
[
k_n = \alpha^n + \beta^n \in \mathbb{Z}, \quad
|\alpha^n - k_n| = |\beta|^n.
]

또한 (|\beta| < \frac12)이면 **모든 (n)** 에서 (\alpha^n)의 반올림이 정확히 (k_n)이 됩니다.
((|\beta|^n < \frac12)일 때마다 반올림이 정확해지기 때문이에요.)

---

## 3️⃣ 왜 (k_n)이 정수인가?

(\alpha, \beta)가 이차방정식
[
x^2 - (\alpha + \beta)x + \alpha\beta = 0
]
의 근이므로, (\alpha + \beta = 2a,\ \alpha\beta = a^2 - db^2).

(\alpha)가 **대수적 정수**이면,
[
\mathrm{Tr}(\alpha) = \alpha + \beta, \quad N(\alpha) = \alpha\beta
]
가 항상 정수입니다.

따라서 (\mathrm{Tr}(\alpha^n) = \alpha^n + \beta^n = k_n)도 정수입니다.

---

## 4️⃣ 점화식으로 (k_n) 만들기

[
k_0 = 2,\quad k_1 = 2a,\quad k_{n+2} = (2a)k_{n+1} - (a^2 - db^2)k_n.
]

이 점화식으로 정수만 써서 (k_n)을 구할 수 있고,
(\alpha^n)의 근접 정수는 바로 이 (k_n)입니다.

---

## 5️⃣ Pell 방정식과의 연결

Pell 방정식
[
x^2 - d y^2 = \pm 1
]
에 정수해 ((x_1, y_1))가 있으면,
[
\alpha = x_1 + y_1\sqrt{d}
]
는 (\mathbb{Q}(\sqrt{d}))의 단위입니다.

그 켤레는 (\beta = x_1 - y_1\sqrt{d}),
(|\beta| = \frac{1}{\alpha} < 1) 이므로,
(\alpha^n + \beta^n \in \mathbb{Z}), (|\alpha^n - k_n| = |\beta|^n).

이게 바로 **거의 정수(almost integer)** 현상이에요.

---

## 6️⃣ 예시

| 예시 | (d) | (N(\alpha)) | (|\beta|) | almost integer 성질 |
|------|-------|---------------|-------------|--------------------|
| (3 + 2\sqrt{2}) | 2 | 1 | 0.1716 | 항상 정수 근접 |
| (2 + \sqrt{3}) | 3 | 1 | 0.2679 | 항상 정수 근접 |
| (5 + 2\sqrt{6}) | 6 | 1 | 0.1010 | 항상 정수 근접 |
| (6 + \sqrt{37}) | 37 | −1 | 0.0828 | 항상 정수 근접 |
| (1.98 = \frac{99}{50}) | — | — | — | 유리수, 구조 없음 |

---

## 7️⃣ 왜 (1.98)은 안 되는가?

* (1.98 = \frac{99}{50})은 **유리수**,
  즉 어떤 (\sqrt{d})와의 켤레 구조가 없음.
* (\alpha^n = (99/50)^n = 99^n / 50^n) 은 단순한 분수 형태이고
  분모가 절대 약분되지 않으므로 정수화될 수 없음.
* 소수부 ((1.98)^n \bmod 1)은 **거의 균등분포(equidistributed)** 로 퍼짐.
  정수 근접은 단지 “우연”일 뿐 구조적 이유가 없습니다.

---

## 8️⃣ 요약

1. (\alpha = a + b\sqrt{d})가 정수에 근접하려면
   (\alpha\beta = \pm 1,\ \alpha > 1,\ |\beta| < 1.)
2. 이 조건을 만족하면 (\alpha^n + \beta^n)은 항상 정수이고,
   (\alpha^n)은 그 정수에 지수적으로 가까움.
3. 특히 (|\beta| < 1/2)이면 **모든 n**에서 반올림이 정확함.
4. 유리수(예: 1.98)는 이런 구조가 없으므로 “almost integer”가 될 수 없음.

---




예시 (d\in{2,3,6,37})에 대해
[
\alpha=a+b\sqrt d,\quad \beta=a-b\sqrt d,\quad
k_n=\alpha^n+\beta^n\in\mathbb{Z},\quad
\alpha^n=k_n-\beta^n,\quad |\alpha^n-k_n|=|\beta|^n
]
을 실제로 “보여줄”게. 아래 수들 모두 (|\beta|<\tfrac12)라서 **모든 (n\ge1)** 에서 (\mathrm{round}(\alpha^n)=k_n)가 성립한다.

---

## 1) (d=2,\ \alpha=3+2\sqrt2)

[
a=3,\ b=2,\ \beta=3-2\sqrt2\approx 0.17157288,\quad
k_{n+2}=6k_{n+1}-k_n,\ k_0=2,\ k_1=6.
]

[
\begin{array}{c|cc}
n & k_n & |\beta|^n \
\hline
1 & 6 & 1.7157\times 10^{-1}\
2 & 34 & 2.944\times 10^{-2}\
3 & 198 & 5.05\times 10^{-3}\
4 & 1154 & 8.67\times 10^{-4}\
5 & 6726 & 1.49\times 10^{-4}
\end{array}
]

---

## 2) (d=3,\ \alpha=2+\sqrt3)

[
a=2,\ b=1,\ \beta=2-\sqrt3\approx 0.26794919,\quad
k_{n+2}=4k_{n+1}-k_n,\ k_0=2,\ k_1=4.
]

[
\begin{array}{c|cc}
n & k_n & |\beta|^n \
\hline
1 & 4 & 2.6795\times 10^{-1}\
2 & 14 & 7.18\times 10^{-2}\
3 & 52 & 1.92\times 10^{-2}\
4 & 194 & 5.16\times 10^{-3}\
5 & 724 & 1.39\times 10^{-3}
\end{array}
]

---

## 3) (d=6,\ \alpha=5+2\sqrt6)

[
a=5,\ b=2,\ \beta=5-2\sqrt6\approx 0.10102051,\quad
k_{n+2}=10k_{n+1}-k_n,\ k_0=2,\ k_1=10.
]

[
\begin{array}{c|cc}
n & k_n & |\beta|^n \
\hline
1 & 10 & 1.0102\times 10^{-1}\
2 & 98 & 1.020\times 10^{-2}\
3 & 970 & 1.03\times 10^{-3}\
4 & 9602 & 1.05\times 10^{-4}\
5 & 95150 & 1.06\times 10^{-5}
\end{array}
]

---

## 4) (d=37,\ \alpha=6+\sqrt{37})

[
a=6,\ b=1,\ \beta=6-\sqrt{37}\approx -0.08276253\ (\ |\beta|=0.08276253),\quad
k_{n+2}=12k_{n+1}+k_n,\ k_0=2,\ k_1=12.
]

[
\begin{array}{c|cc}
n & k_n & |\beta|^n \
\hline
1 & 12 & 8.276\times 10^{-2}\
2 & 146 & 6.85\times 10^{-3}\
3 & 1764 & 5.67\times 10^{-4}\
4 & 21314 & 4.69\times 10^{-5}\
5 & 257532 & 3.87\times 10^{-6}
\end{array}
]

---

### 해설 요약

* 위 네 케이스는 모두 (N(\alpha)=a^2-db^2=\pm1) (단위)이고 (\alpha>1\Rightarrow |\beta|<1).
* 따라서 (k_n=\alpha^n+\beta^n\in\mathbb{Z})이며, (\alpha^n)의 최근접 정수는 (k_n).
* 오차는 정확히 (|\beta|^n)로 **지수적**으로 감소. 위 표의 (|\beta|^n) 열이 그 수치다.

원하면 특정 (d)를 지정해서, 그 (d)의 **기본 단위**(Pell 해)부터 잡고 (k_n)과 (|\beta|^n)을 더 길게 (n)까지 전개해 줄게.




