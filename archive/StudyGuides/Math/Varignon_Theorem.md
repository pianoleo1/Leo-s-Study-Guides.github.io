# Varignon's Theorem and the Midpoint Quadrilateral

A well-known result called **Varignon’s Theorem** states that if you connect the midpoints of 
the sides of any quadrilateral in order, you get a **parallelogram** whose area is **exactly half** the 
area of the original quadrilateral.

---

## 1. State the Setup

Let **ABCD** be any quadrilateral. Denote:
- **E** as the midpoint of **AB**,
- **F** as the midpoint of **BC**,
- **G** as the midpoint of **CD**,
- **H** as the midpoint of **DA**.

We want to show that the quadrilateral **EFGH** is a **parallelogram** with area **\( rac{1}{2} \)** of the area of **ABCD**.

---

## 2. Show EFGH is a Parallelogram

- Since **E** and **F** are midpoints, **EF** is a mid-segment of triangle **ABC**, meaning **EF \parallel AC**.
- Similarly, **HG** is a mid-segment in triangle **ADC**, so **HG \parallel AC** as well.
- Therefore, **EF \parallel HG**.
- Using similar reasoning, **EH \parallel FG**.

Thus, **EFGH is a parallelogram**.

---

## 3. Show the Area is Half

### **Method A: Decompose into Triangles**

1. Draw diagonal **AC** in quadrilateral **ABCD**. This splits **ABCD** into two triangles: **ABC** and **ADC**.
2. In **triangle ABC**, the segment **EF** is a mid-segment. It divides the triangle into two equal areas.
3. Similarly, **HG** divides **triangle ADC** into two equal areas.
4. Thus, the parallelogram **EFGH** has **exactly half** the area of **ABCD**.

### **Method B: Vector Approach**

1. Assign coordinates to **A, B, C, D** as vectors.
2. Compute midpoints **E, F, G, H**.
3. Using **vector cross products**, verify that **Area(EFGH) = \( rac{1}{2} \) Area(ABCD)**.

---

## Key Takeaways

- **Varignon’s Theorem**: Connecting the midpoints of consecutive sides of any quadrilateral produces a **parallelogram**.
- **Half-Area Property**: That parallelogram has exactly **half** the area of the original quadrilateral.

