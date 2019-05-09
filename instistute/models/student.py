
import datetime
from datetime import datetime,timedelta

from odoo.exceptions import UserError


from odoo import api, fields, models, _



class student_leave_request(models.Model):
	_name="student.leave"
	_inherit = ["mail.thread", "ir.needaction_mixin"]


	student = fields.Many2one('student.register',string="Student-Id")
	campus = fields.Char(string='Campus',readonly=True)
	address = fields.Char(string="Address",readonly=True)
	start_date = fields.Date(string="Start-Date")
	ending_date = fields.Date(string="Ending-Date")
	desc=fields.Text(string="Description")
	state = fields.Selection([('draft','Draft'),('rejected','Rejected'),('approved','Approved'),('request','Request')],default='draft',track_visibility='onchange',copy=False,index=True,)
	approve_date = fields.Datetime(string="Approved-Date&Time",readonly=True)

	@api.onchange('student')
	def student_onchange(self):
		campus = self.env['student.register'].search([])
		for names in campus:
			if self.student.name == names.name:
				self.campus = names.campus.name
				self.address = names.address
	@api.multi
	def to_approve(self):

		self.write({
			'approve_date':fields.datetime.now(),
			'state':'approved'})
		
	@api.multi
	def to_reject(self):
		self.write({'state':"rejected"})
	@api.multi
	def request(self):
		self.write({'state':'request'})

	@api.constrains('ending_date')
	def startdate(self):
		if not self.start_date <= self.ending_date:
			raise UserError(_("you need to select more than Starting date"))
class student_result(models.Model):
	_name = 'student.result'

	student_name = fields.Many2one('student.register',string='Student-Name')
	subject1 = fields.Float(string="Telugu")
	subject2 = fields.Float(string="English")
	total = fields.Float(compute="_student_results_view",string="Total",store=True)
	percentage =fields.Float(compute="_student_results_view",string="Percentage",store=True)
	grade = fields.Char(compute="_student_results_view",string="Grade",store=True)

	@api.depends('subject1','subject2')
	def _student_results_view(self):
		for x in self:
			x.total=x.subject1+x.subject2
			x.percentage=x.total/200*100
			if x.percentage>=80:
				x.grade="A Grade"
			elif x.percentage>=70:
				x.grade="B Grade"
			else:
				x.grade="C Grade"

			









