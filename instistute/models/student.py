from odoo import api, fields, models



class student_leave_request(models.Model):
	_name="student.leave"

	student = fields.Many2one('student.register',string="Student-Id")
	campus = fields.Char(string='Campus')
	address = fields.Char(string="Address")
	start_date = fields.Date(string="Start-Date")
	ending_date = fields.Date(string="Ending-Date")
	desc=fields.Text(string="Description")

	@api.onchange('student')
	def student_onchange(self):
		campus = self.env['student.register'].search([])
		for names in campus:
			if self.student.name == names.name:
				self.campus = names.campus.name
				self.address = names.address