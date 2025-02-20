{
    'name': 'Manage University',
    'version': '15.0.1.0.0',
    'summary': 'مدیریت دانشگاه و کلاس ها',
    'description': 'ماژول مدیریت دانشگاه و کلاس و دانشجویان',
    'category': '/myself',
    'author': 'AliReza',
    'website': 'http://pasargaddev.ir',
    'depends': ['mail', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/class_view.xml',
        'views/session_view.xml',
        'views/student_view.xml',
        'views/assignment_view.xml',
        'views/grade_view.xml',
        'views/menu.xml',
    ],
    'sequence': -200,
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
