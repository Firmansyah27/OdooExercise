from odoo import models, fields, api, _

class MataPelajaran(models.Model):
    _name = "mata.pelajaran"
    _description = "Data Pelajaran"

    name = fields.Char(required=True, string="Nama Pelajaran")