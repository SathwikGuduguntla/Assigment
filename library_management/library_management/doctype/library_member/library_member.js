// Copyright (c) 2026, Sathwik and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Member", {
	validate : function (frm) {
        full_name = frm.doc.first_name + " " + frm.doc.last_name
        frm.set_value("full_name", full_name)
}
});
