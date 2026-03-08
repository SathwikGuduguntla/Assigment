# Library Management System - Testing Documentation

**Tester:** Guduguntla Sathwik
**Date:** 08-03-2026
**ERPNext Version:** v15
**Environment:** Ubuntu Linux (Frappe Bench)

---

# Test Summary

| Category         | Total Tests | Passed | Failed |
| ---------------- | ----------- | ------ | ------ |
| Library Member   | 5           | 5      | 0      |
| Book             | 5           | 5      | 0      |
| Book Transaction | 5           | 5      | 0      |
| Integration      | 2           | 2      | 0      |
| **Total**        | **17**      | **17** | **0**  |

---

# Section 1: Library Member Tests

## Test Case 1.1: Create New Member

**Objective:** Verify a new library member can be created successfully.

**Prerequisites**

* Library Management module installed
* User has permission to create members

**Steps**

1. Navigate to **Library Management → Library Member**
2. Click **New**
3. Fill all required fields
4. Click **Save**

**Expected Result**

* Member saves successfully
* `member_id` is auto-generated
* Member appears in list view

**Actual Result**

* Member created successfully
* `member_id` generated correctly

**Status:** ✅ Pass

**Screenshot**

![Create Member](image.png)

---

## Test Case 1.2: Edit Member Details

**Objective:** Verify member details can be edited.

**Steps**

1. Open an existing member
2. Change **membership_type**
3. Click **Save**

**Expected Result**

* Changes are saved successfully

**Actual Result**

* Membership type updated correctly

**Status:** ✅ Pass

**Screenshot**

![Edit Member](image-1.png)

---

## Test Case 1.3: Email Uniqueness Validation

**Objective:** Ensure duplicate emails are not allowed.

**Steps**

1. Create a new member
2. Enter an email already used by another member
3. Click **Save**

**Expected Result**

* System prevents duplicate email
* Error message displayed

**Actual Result**

* Validation error shown

**Status:** ✅ Pass

**Screenshot**

![Email Validation](image-2.png)

---

## Test Case 1.4: Member Status Change

**Objective:** Verify member status can be updated.

**Steps**

1. Open a member record
2. Change status from **Active → Inactive**
3. Click **Save**

**Expected Result**

* Status updated successfully

**Actual Result**

* Status changed correctly

**Status:** ✅ Pass

**Screenshot**

![Status Change](image-3.png)

---

## Test Case 1.5: Delete Member

**Objective:** Verify a member can be deleted.

**Steps**

1. Open a test member record
2. Click **Delete**

**Expected Result**

* Member removed from the system

**Actual Result**

* Member deleted successfully

**Status:** ✅ Pass

**Screenshot**

![Delete Member](image-4.png)

---

### Member List View

![Member List](image-5.png)

---

# Section 2: Book Tests

## Test Case 2.1: Create New Book

**Objective:** Verify book creation.

**Steps**

1. Navigate to **Library Management → Book**
2. Click **New**
3. Enter book details
4. Click **Save**

**Expected Result**

* `book_id` auto-generated
* `available_copies` equals `total_copies`

**Actual Result**

* Book created successfully

**Status:** ✅ Pass

![Create Book](image-6.png)

---

## Test Case 2.2: Available Copies Auto-Set

**Objective:** Ensure available copies auto-populate.

**Steps**

1. Create a book
2. Set `total_copies = 5`
3. Save

**Expected Result**

* `available_copies = 5`

**Actual Result**

* Available copies set correctly

**Status:** ✅ Pass

![Available Copies](image-7.png)

---

## Test Case 2.3: Edit Total Copies

**Objective:** Verify available copies update correctly.

**Steps**

1. Open an existing book
2. Change `total_copies` from 5 to 3
3. Save

**Expected Result**

* Available copies updated accordingly

**Actual Result**

* Available copies updated successfully

**Status:** ✅ Pass

![Edit Copies](image-8.png)

---

## Test Case 2.4: Negative Copies Validation

**Objective:** Prevent negative values.

**Steps**

1. Open a book
2. Set `total_copies = -1`
3. Save

**Expected Result**

* Validation error displayed

**Actual Result**

* Error message shown

**Status:** ✅ Pass

![Negative Validation](image-9.png)

---

## Test Case 2.5: ISBN Uniqueness

**Objective:** Ensure duplicate ISBN numbers are prevented.

**Steps**

1. Create a book
2. Use an existing ISBN
3. Save

**Expected Result**

* System prevents duplicate ISBN

**Actual Result**

* Validation error displayed

**Status:** ✅ Pass

![ISBN Validation](image-10.png)

---

# Section 3: Book Transaction Tests

## Test Case 3.1: Create Issue Transaction

**Objective:** Verify book issue transaction.

**Steps**

1. Create transaction
2. Set type **Issue**
3. Enter due date
4. Save

**Expected Result**

* Transaction saved successfully

**Actual Result**

* Issue transaction created successfully

**Status:** ✅ Pass

![Issue Transaction](image-11.png)

---

## Test Case 3.2: Issue Without Due Date

**Objective:** Validate due date requirement.

**Steps**

1. Create issue transaction
2. Leave `due_date` empty
3. Save

**Expected Result**

* Validation error displayed

**Actual Result**

* Error message shown

**Status:** ✅ Pass

![Issue Validation](image-12.png)

---

## Test Case 3.3: Create Return Transaction

**Objective:** Verify return transaction.

**Steps**

1. Create transaction
2. Set type **Return**
3. Enter return date
4. Save

**Expected Result**

* Transaction saved successfully

**Actual Result**

* Return transaction created successfully

**Status:** ✅ Pass

![Return Transaction](image-15.png)

---

## Test Case 3.4: Return Without Return Date

**Objective:** Ensure return date is mandatory.

**Steps**

1. Create return transaction
2. Leave return date empty
3. Save

**Expected Result**

* Validation error displayed

**Actual Result**

* Error message shown

**Status:** ✅ Pass

![Return Validation](image-16.png)

---

## Test Case 3.5: Invalid Return Date

**Objective:** Prevent return date earlier than transaction date.

**Steps**

1. Create return transaction
2. Set return date earlier than transaction date
3. Save

**Expected Result**

* Validation error displayed

**Actual Result**

* Error message shown

**Status:** ✅ Pass

![Invalid Return](image-17.png)

---

# Section 4: Integration Tests

## Test Case 4.1: Complete Checkout Flow

**Objective:** Verify full library workflow.

**Steps**

1. Create member
2. Create book
3. Issue book to member

**Expected Result**

* All data linked correctly

**Actual Result**

* Checkout flow completed successfully

**Status:** ✅ Pass

Screenshots

![Create Member](image-18.png)

![Create Book](image-19.png)

![Issue Book](image-20.png)

---

## Test Case 4.2: Link Field Functionality

**Objective:** Verify link fields populate correctly.

**Steps**

1. Open Book Transaction
2. Click Member field
3. Select member
4. Click Book field
5. Select book

**Expected Result**

* Member list visible
* Book list visible
* Selected records populate correctly

**Actual Result**

* Link fields working correctly

**Status:** ✅ Pass

Screenshots

![Member List](image-22.png)

![Book List](image-23.png)

![Link Field](image-21.png)

---

# Issues Found

1. Some validation rules initially did not trigger correctly during early testing.
2. Available copies sometimes did not update when total copies were modified.

---

# Recommendations

1. Improve validation rules for date fields and transaction logic.
2. Automatically update available copies when transactions occur.
3. Provide clearer validation messages to guide users.

---

# Acceptance Criteria

✅ TESTING.md file created
✅ All 17 test cases documented
✅ All tests executed
✅ Actual results recorded
✅ Pass/Fail status marked
✅ Professional formatting

---

# Next Steps

1. Commit and push documentation

```bash
git add .
git commit -m "docs(testing): add comprehensive test documentation"
git push origin main
```

2. Verify repository is public
3. Submit repository link for evaluation

---

🎉 **All testing tasks completed successfully.**
