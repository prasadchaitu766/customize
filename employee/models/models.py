# -*- coding: utf-8 -*-
from datetime import datetime
import random

from odoo import models, fields, api,_

class Employee_Details(models.Model):
	_name = "employee.employee"



	name = fields.Char(string="Employee Name",help="this is for employee")
	emp_Id = fields.Integer(string="Employee_Id")
	image = fields.Binary(string="Photo")
	date_of_birth =fields.Date(string="Date of Birth", required= True)
	age=fields.Integer(string="Age")
	active=fields.Boolean(string="Active", default="True")
	join_date=fields.Date(string="Date of Joining")
	gender=fields.Selection([("male","Male"),("female","Female")])
	department=fields.Many2one("department.department",string="Department-Name",required=True)

	@api.onchange('date_of_birth')
	def onchange_age_calculation(self ):
		if not self.date_of_birth:
			self.age = 0
		else:
	 		today_date = datetime.now().year
			date_split = self.date_of_birth.split('-',1)
			birth_year = date_split[0]
			self.age = today_date -int(birth_year)
	@api.one
	def generateEmpId(self):
		for x in range(100):
			f=random.randint(101,300)
			self.emp_Id=f
			return True
	



class Department(models.Model):
	_name="department.department"

	

	
	dep_id=fields.Integer(string="Department Id")
	name = fields.Char(string="Department Name")
	note = fields.Text('Terms and conditions')

	@api.one
	def Departments_id(self): 
		for x in range(10):
			d=random.randint(1,100)
			self.dep_id=d
			return True



class SalaryDetails(models.Model):
	_inherit="employee.employee"

	basic_salary=fields.Integer(string="Basic  Salary")
	total_salary=fields.Float(string="Total-Salary", readonly=True)
	
	@api.one
	def calculate_salry(self):
		ba=self.basic_salary
		da=self.basic_salary*0.10
		total=ba+da
		self.total_salary=total
		


