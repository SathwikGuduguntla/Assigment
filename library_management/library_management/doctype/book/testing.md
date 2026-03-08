## 📚 Book Module – Test Cases

### Test Case 1: Create New Book

**Steps:**

1. Navigate to **Library Management → Book → New**
2. Enter the following details:

   * **Title:** The Great Gatsby
   * **Author:** F. Scott Fitzgerald
   * **ISBN:** 978-0-7432-7356-5
   * **Category:** Fiction
   * **Total Copies:** 5
3. Click **Save**

**Expected Result:**

* The book record is saved successfully.
* **available_copies** is automatically set to **5**.
* **book_id** is automatically generated (e.g., `BOOK-00001`).

**Screenshot:**

![Create Book](image.png)

---

### Test Case 2: Edit Total Copies

**Steps:**

1. Open an existing **Book** record.
2. Change **Total Copies** from **5** to **3**.
3. Click **Save**.

**Expected Result:**

* If **available_copies** was previously **5**, it automatically updates to **3**.
* Validation ensures **available_copies never exceeds total_copies**.

**Screenshot:**

![Edit Total Copies](image-1.png)

---

### Test Case 3: Negative Copies Validation

**Steps:**

1. Open a **Book** record.
2. Set **Total Copies** to **-1**.
3. Click **Save**.

**Expected Result:**

* The system displays an error message:
  **"Total copies cannot be negative"**
* The record is **not saved**.

**Screenshot:**

![Negative Copies Validation](image-2.png)

---

## 📊 Sample Data

The following sample books were created to test the Book module.

| Title                     | Author            | Category    | Total Copies |
| ------------------------- | ----------------- | ----------- | ------------ |
| 1984                      | George Orwell     | Fiction     | 3            |
| Sapiens                   | Yuval Noah Harari | Non-Fiction | 2            |
| A Brief History of Time   | Stephen Hawking   | Science     | 1            |
| Clean Code                | Robert C. Martin  | Technology  | 4            |
| The Diary of a Young Girl | Anne Frank        | Biography   | 2            |

---


## 📋 List View

The list view provides an overview of all book records and supports filtering, searching, and sorting.

**Screenshot:**

![List View](image-5.png)
