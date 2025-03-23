# Resumo de Limites e Derivadas

## 1. Limites

### 1.1 Definição de Limite
- **Limite de uma função**: 
  \[
  \lim_{x \to a} f(x) = L
  \]
  Significa que, quando \(x\) se aproxima de \(a\), \(f(x)\) se aproxima de \(L\).

### 1.2 Propriedades Básicas
- **Soma/Diferença**:  
  \[
  \lim_{x \to a} [f(x) \pm g(x)] = \lim_{x \to a} f(x) \pm \lim_{x \to a} g(x)
  \]
- **Produto**:  
  \[
  \lim_{x \to a} [f(x) \cdot g(x)] = \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x)
  \]
- **Quociente** (se \( \lim_{x \to a} g(x) \neq 0\)):  
  \[
  \lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}
  \]

### 1.3 Limites Notáveis
- **\(\lim_{x \to 0} \frac{\sin x}{x} = 1\)**
- **\(\lim_{x \to \infty} \frac{1}{x^n} = 0\) (para \(n > 0\))**

### 1.4 Indeterminações Comuns
- \( \frac{0}{0} \)
- \( \infty - \infty \)
- \( \frac{\infty}{\infty} \)

### 1.5 Técnicas para Resolver Limites
- **Fatoração**: Simplificar expressões.
- **Racionalização**: Multiplicar pelo conjugado.
- **Substituição**: Usar identidades trigonométricas ou equivalências.

---

## 2. Derivadas

### 2.1 Definição de Derivada
- A derivada de \(f(x)\) em \(x = a\) é:  
  \[
  f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}
  \]

### 2.2 Regras Básicas
- **Constante**:  
  \[
  \frac{d}{dx}[c] = 0
  \]
- **Potência**:  
  \[
  \frac{d}{dx}[x^n] = n \cdot x^{n-1}
  \]
- **Soma/Diferença**:  
  \[
  \frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)
  \]
- **Produto**:  
  \[
  \frac{d}{dx}[f(x) \cdot g(x)] = f'(x) \cdot g(x) + f(x) \cdot g'(x)
  \]
- **Quociente**:  
  \[
  \frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}
  \]

### 2.3 Derivadas de Funções Comuns
- **Exponencial**:  
  \[
  \frac{d}{dx}[e^x] = e^x
  \]
- **Logarítmica**:  
  \[
  \frac{d}{dx}[\ln x] = \frac{1}{x}
  \]
- **Trigonométricas**:
  \[
  \frac{d}{dx}[\sin x] = \cos x, \quad \frac{d}{dx}[\cos x] = -\sin x
  \]
  \[
  \frac{d}{dx}[\tan x] = \sec^2 x
  \]

### 2.4 Regra da Cadeia
- Para \(y = f(g(x))\):  
  \[
  \frac{dy}{dx} = f'(g(x)) \cdot g'(x)
  \]

---

## 3. Exemplos Práticos

### 3.1 Limite
Resolva:
\[
\lim_{x \to 2} \frac{x^2 - 4}{x - 2}
\]
**Solução**: Fatoramos \(x^2 - 4\):  
\[
\frac{(x-2)(x+2)}{x-2} = x + 2
\]
Portanto:  
\[
\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = 2 + 2 = 4
\]

### 3.2 Derivada
Encontre \(\frac{d}{dx}[x^3 + 2x^2]\):  
\[
\frac{d}{dx}[x^3] + \frac{d}{dx}[2x^2] = 3x^2 + 4x
\]

---

**Boa sorte na prova!** 📘
