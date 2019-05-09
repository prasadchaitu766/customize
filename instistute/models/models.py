# -*- coding: utf-8 -*-
from datetime import datetime
from odoo.exceptions import UserError,ValidationError
import re




from odoo import api, fields, models
from odoo import tools, _



import random
import string
from random import randint
import smtplib


from odoo import models, fields, api

class StudentRegistaration(models.Model):
	_name = "student.register"
	# _inherit=['mail.thread']

	s_id  = fields.Char(string="Student_Id",readonly=True)
	name = fields.Char(string="Student Name") 
	age = fields.Integer(string="Age",help="enter age")
	date_of_birth = fields.Date(string="Date-Of-Birth")
	gender = fields.Selection([("male","Male"),("female","Female"),("others","Others")],string="Gender")
	address =fields.Text(string="Address")
	image = fields.Binary()
	email = fields.Char(string="Email",required=True)
	campus= fields.Many2one("student.campus",string="Campus")
	contact = fields.Char(string="Contact")
	qualification = fields.Many2one("qualification.qualification",string="Qualification")

	username = fields.Char(string="Username")
	password = fields.Char(string="Password")
	desc = fields.Html(string="Description")

	@api.constrains('age')
	def checking_age(self):
		for x in self:
			if x.age>=30 :
				raise UserError(_("Your  age not match please change your date of birth your age must be below 30"))
			elif x.age<=15:
				raise UserError(_("Your age must be more than 15 Years"))

	@api.constrains('email')
	def email_validating(self):
		for y in self:
			if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", y.email) == None:
				raise ValidationError("Please Provide valid Email Address: %s" % y.email)

			else:
				raise UserError(_("Your email is not correct"))




 #    @api.constrains('contact')
	# def contact_validaion(self):
	# 	for z in self:
	# 		if count(z.contact)!=10:
	# 			raise UserError(_("Mobile number must be 10 digits"))
	# 		elif re.compile("(0/91)?[7-9][0-9]{9}"):
	# 			raise UserError(_("please enter valid contact number"))


 	

	@api.onchange('date_of_birth')
	def Calculate_age(self):
		if not self.date_of_birth:
			self.age=0
		else:
			today_date = datetime.now().year
			date_split = self.date_of_birth.split('-',1)
			birth_year = date_split[0]
			self.age = today_date-int(birth_year)


	@api.multi
	def generate_record_name(self,values):
		# if 'username' in values.key:
		# 	print values['username'],"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

	
		f=({'name': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(9,15)))})
		

		self.username=f["name"]

	@api.multi
	def generate_record_password(self):
		self.ensure_one()
		g=({'password': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(12,15)))
})		
		self.password=g["password"]

	@api.multi
	def send_email(self):
		template = self.env.ref('instistute.send_email_process')

		self.env['mail.template'].browse(template.id).send_mail(self.id,force_send=True)

		# template_id = self.env.ref('instistute.send_email_process')

		# template_id.send_mail(self.ids[0], force_send=True)
		

	@api.one
	def auto_generated(self):
		if self.s_id ==False:
			next_id = self.env["ir.sequence"].next_by_code("test_seq_id")
			self.s_id =next_id
		else:
			pass
	# @api.multi
	# def report_coupon(self):

	# 	data={
	# 	'ids':self.ids,
	# 	'model':self._name,
	# 	'form':{},
	# 	}
	# 	print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
	# 	return self.env.ref['report'].get_action(self,'instistute.employee_report_advance',data=data)

	@api.multi
	def report_coupon(self):
			return self.env['report'].get_action(self,'instistute.employee_report_advance')

		
		
		
# class student_list_report(models.TransientModel):
# 	_name="student.list"

# 	stu_id = fields.Many2one('student.register',string="Student",required=True)
	

# 	@api.multi
# 	def student_reports(self):
# 		student_search = self.env['student.register'].search([('student_id','=',self.stu_id.id)])
# 		return self.env['report'].get_action(student_search,'instistute.student_layout_report')


# @api.multi
# def my_student(self,cr,uid,ids,context=None):
# 	pool_obj = pooler.get_pool(cr.ems)
# 	my_objects = pool_obj.get('project.myobject')



	


class qualification(models.Model):
	_name ="qualification.qualification"

	name=fields.Char(string="Qualification_Name")


class Daily_report(models.Model):
    _name='report.report'
    
    name=fields.Char(string="Employee-Name")
    Manager_name=fields.Char(string="Manager_name")
    task_date = fields.Datetime(string="Task-date")
    tasks = fields.One2many('task.task','report',string="Tasks")

class Tasks(models.Model):
    _name='task.task'
    

    task_no = fields.Integer(string="Task no")
    task_description = fields.Text(string="Description")
    started_date=fields.Date(string="Started-date")
    finished_date =fields.Date(string="Finished-date")
    status =fields.Char(string="Task Status") 
    report=fields.Many2one('report.report')

class student_extra_elemnet(models.Model):
    _inherit="student.register"

    blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string='Blood Group')
# class student_inherited_view(models.Model):
# 	_inherit ="report.report"

# 	@api.multi
# 	def student_records(self):
# 		return{
# 		  'type':'ir.actions.act_windoow',
# 		  'name':'Student Records',
# 		  'view_mode':'tree,form',
# 		  'res_model':'report.report',
# 		  'domain':[('name','=',self.name)]
# 		}
class campus(models.Model):
	_name="student.campus"

	name=fields.Char(string="Campus-Name",required=True)
	code = fields.Char(string="Campus-Code")
	address = fields.Text(string="Address")
	contact = fields.Char(string="Contact")
	email = fields.Char(string="Email")





	


