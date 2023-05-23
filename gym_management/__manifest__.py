{
    'name': 'Gym Management',
    'version': '1.0',
    'website':"https://www.diracerp.com",
    'image':[],
    'depends': ['base','mail','sale','hr','purchase'],
    'author':"DiracErp",
    'description': "this is Gym Management module",
    'data': [
            "security/ir.model.access.csv",
            "security/user_role_group.xml",
             "data/sq_number.xml",
             "data/invite_mail.xml",
             "data/diet_mail.xml",
             "data/join_mail.xml",
             "data/alert_mail.xml",
             "data/payment_receive_mail.xml",
             "report/report_recod.xml",
             "wizard/assign_workout_plan_view.xml",
             "wizard/assign_diet_plan.xml",
             "wizard/cancel_resion_view.xml",
             "wizard/invoice_membership_view.xml",
             "view/member_view.xml",
             "view/menu_list.xml",
             "view/res_partner_view.xml",
             "view/trainer_view.xml",
             "view/body_part_view.xml",
             "view/gym_equipment_view.xml",
             "view/gym_activity_view.xml",
             "view/workout_day_view.xml",
             "view/diet_food_view.xml",
             "view/consume_at_view.xml",
             "view/membership_view.xml",
             "view/exercise_view.xml",
             "view/workout_plan_view.xml",
             "view/diet_plan_view.xml",
             "view/trainer_skills_view.xml",
             "view/special_session_view.xml",
             "view/user_role_view.xml",
             "view/trainer_card_report.xml",
             "view/member_card_report.xml",
             "view/member_details_report.xml",
             "view/trainer_details_report.xml",
             "view/diet_plan_report.xml",
             "view/scheduler.xml",
             "view/member_analysis_view.xml",
            ],
            'license': 'LGPL-3',
    
    'installable': True,
    'auto_install': False,
    'active':False,
}
