
```markdown
# 📊 Asymptotic Analysis (Made Simple)

When we study algorithms, we care about **how fast they run** when the input size (`n`) becomes very large.  
This is called **asymptotic analysis**.

Think of it like this:  
👉 Small numbers don’t matter much.  
👉 Big numbers (like thousands, millions) show us the *real speed* of an algorithm.  

---

## 🔑 Main Idea
- **Asymptotic** means "what happens when `n` grows very large."
- We use math symbols to describe how an algorithm grows:
  - **Big O (O)** → Upper bound (worst case, maximum growth).  
  - **Omega (Ω)** → Lower bound (best case, minimum growth).  
  - **Theta (Θ)** → Tight bound (exact growth).

---

## 🧮 Example
Take a function:  
```

f(n) = n² + 6n

```

- If `n = 1,000`:  
  - `n² = 1,000,000`  
  - `6n = 6,000`

Here, **1,000,000 is much bigger than 6,000**, so the `6n` part hardly matters.  
We only care about the **biggest part** (`n²`).  

👉 So, we say:  
```

f(n) \~ n²  (asymptotically)

```

---

## ⚙️ Algorithm Analysis
- We measure algorithms with **functions of n** (input size).  
- Small constants don’t matter.  
- Only the **growth rate** matters when `n → ∞` (n gets very large).  

---

## 🚦 Common Time Complexities
From fastest to slowest:

1. **Constant:** `O(1)` → Same time, no matter the input.  
2. **Logarithmic:** `O(log n)` → Grows very slowly.  
3. **Linear:** `O(n)` → Grows directly with input.  
4. **Linearithmic:** `O(n log n)` → A bit more than linear.  
5. **Quadratic:** `O(n²)` → Double loops (slow for big n).  
6. **Cubic:** `O(n³)` → Triple loops (even slower).  
7. **Exponential:** `O(2^n)` → Extremely slow for big n.  

👉 Always remember:  
```

O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2^n)

```

---

## 📝 Notations Explained

### 1. Big-O (O)
**Definition:**  
```

f(n) ≤ C \* g(n)   for n ≥ n₀

```
- Describes the **upper bound** (worst case).  
- Example: `f(n) = n² + 6n` is **O(n²)**.

---

### 2. Omega (Ω)
**Definition:**  
```

f(n) ≥ C \* g(n)   for n ≥ n₀

```
- Describes the **lower bound** (best case).  

---

### 3. Theta (Θ)
**Definition:**  
```

C₁ \* g(n) ≤ f(n) ≤ C₂ \* g(n)   for n ≥ n₀

```
- Describes the **tight bound** (exact growth).  

---

## 🎯 Quick Recap
- **Big-O (O):** Upper bound (worst case).  
- **Omega (Ω):** Lower bound (best case).  
- **Theta (Θ):** Tight bound (exact case).  

👉 If an algorithm has time `n²`, we usually say:  
```

Time complexity = O(n²)

```
because we mostly care about the **upper bound**.

---
```


## 🚦 Common Time Complexities (with Real-World Analogies)

1. **Constant Time → O(1)**  
   - 🎲 No matter how big `n` is, the work is the same.  
   - Example: Picking the first toy from your toy box.  

---

2. **Logarithmic Time → O(log n)**  
   - 📚 Work shrinks as the problem gets smaller each step.  
   - Example: Looking up a word in a dictionary by splitting pages in half each time.  

---

3. **Linear Time → O(n)**  
   - 🍽️ Work grows directly with input.  
   - Example: Washing `n` dishes, one by one.  

---

4. **Linearithmic Time → O(n log n)**  
   - 🧩 A bit more than linear, often splitting + combining work.  
   - Example: Sorting Lego bricks by size using a "divide and conquer" method.  

---

5. **Quadratic Time → O(n²)**  
   - 🔁 Double loops = work inside work.  
   - Example: For every student in a class, you shake hands with every other student.  

---

6. **Cubic Time → O(n³)**  
   - 🔁🔁 Triple loops = even more work.  
   - Example: Comparing every cube in a box with every other cube in 3 dimensions.  

---

7. **Exponential Time → O(2^n)**  
   - 💥 Explodes very fast. Impossible for big `n`.  
   - Example: Trying every possible key on a giant lock. Each new key doubles the possibilities.  

---

👉 Always remember the order (fastest to slowest):  