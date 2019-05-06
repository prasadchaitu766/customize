# -*- coding: utf-8 -*-

from odoo import models, fields, api

class student(models.Model):
    _name = 'student.student'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    contact = fields.Char()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

class teacher(models.Model):
	_name='student.teacher'

	name=fields.Char(string="Name", required=True)
	address=fields.Text(string="Address", required=True)
	contact=fields.Char(string="Contact",required=True)
	salary=fields.Integer()


class student_Addmission(models.Model):
	_name='student.admission'

	name = fields.Char(required=True)
	age = fields.Char(required=True)
	gender=fields.Char(required=True)
	contact=fields.Char(required=True)
	email=fields.Char(required=True)
	qualification = fields.Char(required=True)


class StudentRecord(models.Model):

    _name = "student.student_record"


    name = fields.Char(string='Name', required=True)
    middle_name = fields.Char(string='Middle Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    photo = fields.Binary(string='Photo')
    student_age = fields.Integer(string='Age')
    student_dob = fields.Date(string="Date of Birth")
    student_gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')
    student_blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nationality')
    State = fields.Many2one('res.users',string="User")
    
	

	
