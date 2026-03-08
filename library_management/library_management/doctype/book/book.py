# Copyright (c) 2026, Sathwik and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Book(Document):

    def before_save(self):
        self.total_copies = self.total_copies or 0
        self.available_copies = self.available_copies or 0

        # Always keep available copies equal to total copies
        self.available_copies = self.total_copies


    def validate(self):

        total = self.total_copies or 0
        available = self.available_copies or 0

        if total < 0:
            frappe.throw("Total copies cannot be negative")

        if available < 0:
            frappe.throw("Available copies cannot be negative")