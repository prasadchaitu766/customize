# -*- coding: utf-8 -*-
from datetime import datetime



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
	name = fields.Char(string="StudentName") 
	age = fields.Integer(string="Age",help="enter age")
	date_of_birth = fields.Date(string="Date-Of-Birth")
	gender = fields.Selection([("male","Male"),("female","Female"),("others","Others")],string="Gender")
	address =fields.Text(string="Address")
	image = fields.Binary()
	email = fields.Char(string="Email",required=True)
	contact = fields.Char(string="Contact")
	qualification = fields.Many2one("qualification.qualification",string="Qualification")
	username = fields.Char(string="Username")
	password = fields.Char(string="Password")
	desc = fields.Html(string="Description")
 	

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
    
    employee_name=fields.Char(string="Employee-Name")
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




	


