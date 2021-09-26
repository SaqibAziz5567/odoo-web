from odoo import http, models, fields


class Academy(http.Controller):

    @http.route('/academy/test/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('Teachers.index', {
            'teachers': Teachers.search([])
        })
