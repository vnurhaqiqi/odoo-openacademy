# -*- coding: utf-8 -*-
{
    'name':        "OpenAcademy",

    'summary':
                   """
                   Openacademy
                   """,

    'description': """
        Manage course, classes, teachers, students, ...
    """,

    'author':      "Odoo",
    'website':     "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':    'OpenAcademy',
    'version':     '0.1',

    # any module necessary for this one to work correctly
    'depends':     ['base'],

    # always loaded
    'data':        [
        "security/ir.model.access.csv",
        "data/openacademy_data.xml",
        "views/menu.xml",
        "views/course.xml",
        "views/sequence.xml",
        "views/student.xml",
        "views/session.xml",
        "report/report_course_template.xml",
        "report/label_course_report.xml",
        "report/report_session_template.xml",
        "wizard/wiz_session_report.xml",
    ],
    # only loaded in demonstration mode
    'demo':        [],
    'license': 'AGPL-3',
}
