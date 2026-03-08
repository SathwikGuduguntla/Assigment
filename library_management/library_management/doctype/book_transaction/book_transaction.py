# Copyright (c) 2026, Sathwik and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate

class BookTransaction(Document):

    def validate(self):

        if self.transaction_type == "Issue":
            if not self.due_date:
                frappe.throw("Due Date is mandatory for Issue transactions")

        if self.transaction_type == "Return":
            if not self.return_date:
                frappe.throw("Return Date is mandatory for Return transactions")

    
        if self.return_date and self.transaction_date:
            if getdate(self.return_date) < getdate(self.transaction_date):
                frappe.throw("Return Date cannot be before Transaction Date")

        if self.transaction_type == "Return":
            self.status = "Returned"