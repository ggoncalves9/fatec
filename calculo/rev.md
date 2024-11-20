# Passo a Passo e Dicas: Limites, Derivadas e Integrais

## 1. Limites

### **1.1 O que é um limite?**
O limite descreve o comportamento de uma função \(f(x)\) quando \(x\) se aproxima de um valor específico.

---

### **1.2 Passos para Resolver Limites**
1. **Substitua diretamente o valor de \(x\)**:
   - Exemplo: \(\lim_{x \to 2} (x^2 + 3) = 2^2 + 3 = 7\).
2. **Identifique indeterminações (\(\frac{0}{0}\), etc.)**:
   - Caso ocorra, use as técnicas abaixo.

3. **Fatoração**:
   - Quando houver polinômios:
     \[
     \lim_{x \to 2} \frac{x^2 - 4}{x - 2} \to \frac{(x-2)(x+2)}{x-2} = x+2.
     \]
     Substituindo: \(2 + 2 = 4\).

4. **Racionalização**:
   - Use em raízes:
     \[
     \lim_{x \to 0} \frac{\sqrt{x+1} - 1}{x}.
     \]
     Multiplique pelo conjugado:
     \[
     \frac{\sqrt{x+1} - 1}{x} \cdot \frac{\sqrt{x+1} + 1}{\sqrt{x+1} + 1} = \frac{(x+1) - 1}{x (\sqrt{x+1} + 1)}.
     \]
     Resultado: \(\frac{1}{\sqrt{x+1} + 1}\).

5. **Limites Notáveis**:
   - Memorize:
     \[
     \lim_{x \to 0} \frac{\sin x}{x} = 1, \quad \lim_{x \to 0} (1 + x)^{\frac{1}{x}} = e.
     \]

---

### **1.3 Dicas para Limites**
- **Se \(x \to \infty\)**: Compare o crescimento dos termos (ex.: graus de \(x\)).
- **Se há raízes ou logaritmos**, considere substituições que simplifiquem.

---

## 2. Derivadas

### **2.1 O que é uma derivada?**
A derivada mede a **taxa de variação** de uma função. Basicamente, é a inclinação da curva em um ponto.

---

### **2.2 Passos para Calcular Derivadas**
1. **Identifique o formato da função**.
   - Se é uma soma, produto, quociente ou função composta.

2. **Aplique as Regras Básicas**:
   - Constante:
     \[
     \frac{d}{dx}[c] = 0
     \]
   - Potência:
     \[
     \frac{d}{dx}[x^n] = n \cdot x^{n-1}.
     \]
   - Exemplo: \(f(x) = x^3 + 2x^2\).
     \[
     f'(x) = 3x^2 + 4x.
     \]

3. **Use a Regra da Cadeia**:
   - Se \(y = f(g(x))\):  
     \[
     \frac{dy}{dx} = f'(g(x)) \cdot g'(x).
     \]

4. **Para produtos e quocientes**, use:
   - Produto:
     \[
     \frac{d}{dx}[u \cdot v] = u'v + uv'.
     \]
   - Quociente:
     \[
     \frac{d}{dx}\left[\frac{u}{v}\right] = \frac{u'v - uv'}{v^2}.
     \]

---

### **2.3 Dicas para Derivadas**
- Para funções trigonométricas:
  \[
  \frac{d}{dx}[\sin x] = \cos x, \quad \frac{d}{dx}[\cos x] = -\sin x.
  \]
- Logaritmos e exponenciais:
  \[
  \frac{d}{dx}[e^x] = e^x, \quad \frac{d}{dx}[\ln x] = \frac{1}{x}.
  \]

---

## 3. Integrais

### **3.1 O que é uma integral?**
A integral representa a **área sob a curva** de uma função. Pode ser:
- **Indefinida**: Sem limites (gera uma família de funções).
- **Definida**: Calcula a área entre dois valores.

---

### **3.2 Passos para Calcular Integrais**
1. **Identifique o formato da função**.
   - Se é uma potência, trigonométrica ou composta.

2. **Use as Regras Básicas**:
   - Potência:
     \[
     \int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1).
     \]
     Exemplo: \(\int x^2 \, dx = \frac{x^3}{3} + C\).

   - Constantes:
     \[
     \int c \, dx = c \cdot x + C.
     \]

   - Exponenciais:
     \[
     \int e^x \, dx = e^x + C.
     \]

   - Logarítmica:
     \[
     \int \frac{1}{x} \, dx = \ln|x| + C.
     \]

3. **Para funções compostas**, use substituição:
   - Se \(\int f(g(x))g'(x) \, dx\), faça \(u = g(x)\).

4. **Para produtos**, use integração por partes:
   - Fórmula:
     \[
     \int u \, dv = uv - \int v \, du.
     \]

5. **Para integrais definidas**:
   - Calcule:
     \[
     \int_a^b f(x) \, dx = F(b) - F(a),
     \]
     onde \(F(x)\) é a primitiva de \(f(x)\).

---

### **3.3 Dicas para Integrais**
- **Verifique sempre a regra correta antes de aplicar**.
- Em integrais definidas, substitua corretamente os limites após integrar.
- Para integrais trigonométricas, lembre-se:
  \[
  \int \sin x \, dx = -\cos x + C, \quad \int \cos x \, dx = \sin x + C.
  \]

---

## 4. Exemplos Práticos

### **4.1 Limites**
Resolva:
\[
\lim_{x \to 1} \frac{x^2 - 1}{x - 1}.
\]
1. Fatoramos \(x^2 - 1\):  
   \[
   \frac{(x-1)(x+1)}{x-1} = x + 1.
   \]
2. Substituímos \(x = 1\):  
   \[
   1 + 1 = 2.
   \]

---

### **4.2 Derivadas**
Calcule a derivada de \(f(x) = x^2 + 3x + 1\):
\[
f'(x) = 2x + 3.
\]

---

### **4.3 Integrais**
Resolva \(\int (3x^2 + 2x) \, dx\):
\[
\int 3x^2 \, dx + \int 2x \, dx = x^3 + x^2 + C.
\]

---

**Boa sorte nos estudos!**
