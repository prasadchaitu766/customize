import datetime
import random
from random import randint
import string
from datetime import datetime
from openerp import models,api,fields
from odoo import models, fields, api



class student(models.Model):
	_name = "student.student"

	@api.onchange('dob','age')
	def onchange_age_calculation(self ):
		if not self.dob:
			self.age = 0
		else:
	 		today_date = datetime.now().year
	 		
			date_split = self.dob.split('-',1)
			birth_year = date_split[0]
			
			self.age = today_date -int(birth_year)
			
	

	

	name = fields.Char(string="Name Of The Student")
	email = fields.Char(string="Email",required=True)
	contact = fields.Char(string="Contact",required=True)
	dob = fields.Date(string="Date Of Birth")
	reg_date = fields.Date(string="Registration-Date",required=True)
	is_pysically_disabled = fields.Boolean(string="Is Pysycally Disabled")
	image = fields.Binary(string="Image")
	gender = fields.Selection([("male","Male"),("female","Female")],string="Gender")

	#Relation Fields

	course_id = fields.Many2one('course.course',string="Course")
	hobby_id = fields.Many2many('hobby.hobby', string="Hobby")
	qualification = fields.Many2one('qualification.qualification',string="Qualification")

	#custome Fields
	age = fields.Integer(string="Age",store=True)

	





	
class qualificaion_qualification(models.Model):
	_name = 'qualification.qualification'

	course_name=fields.Char(string="Course_name")

class course_course(models.Model):
    _name = 'course.course'
 
    
    name = fields.Char('Course Name')
    
class hobby_hobby(models.Model):
    _name = 'hobby.hobby'
 
    name = fields.Char('Hobby Name')

class teacher_transfer(models.Model):
	_name = 'teacher.teacher'

	teacher = fields.Many2one('register.register',string="Teacher")
	reg_date = fields.Date(string="Registration-Date")
	message = fields.Char(string="Message")

class teacher_register(models.Model):
	_name = 'register.register'

	name = fields.Char(string="Teacher Name")
	contact = fields.Char(string="Contact")
	email = fields.Char(string="Email")
	designation = fields.Char(string="Designation")






class button_action_demo(models.Model):
    _name = 'button.demo'
    name = fields.Char(required=True,default='Click on generate name!')
    password = fields.Char()
    
    @api.multi
    def generate_record_name(self):
	self.ensure_one()
	#Generates a random name between 9 and 15 characters long and writes it to the record.
	self.write({'name': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(9,15)))})

    @api.multi
    def generate_record_password(self):
	self.ensure_one()
	#Generates a random password between 12 and 15 characters long and writes it to the record.
	self.write({
	    'password': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(randint(12,15)))
	})

    @api.multi
    def clear_record_data(self):
	self.ensure_one()
	self.write({
	    'name': '',
	    'password': ''
})