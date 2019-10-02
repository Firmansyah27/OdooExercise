from odoo import models, fields, api, _

class Siswa(models.Model):
    _name = "siswa"
    _description = "data siswa"

    name = fields.Char(required=True, string="Nama")
    kelas = fields.Selection([
        ('i','I'),
        ('ii','II'),
        ('iii','III'),
    ], default='i')
