from django.urls import path 
from . import views 




urlpatterns = [
    path('', views.Login_User, name="Login"),
    path('logout/', views.logout_user, name="logout"),
    path('patron/', views.patron_user, name="patron"),
    path('Accountant/', views.burser_user, name="burser"),
    path('Trainer/CST/', views.cst_class_teacher, name="cst_trainer"),
    path('Trainer/RCPO/L3/', views.rcpo_l3_class_teacher, name="rcpo_l3_trainer"),
    path('Trainer/RCPO/L4/', views.rcpo_l4_class_teacher, name="rcpo_l4_trainer"),
    path('Trainer/RCPO/L5/', views.rcpo_l5_class_teacher, name="rcpo_l5_trainer"),
    path('Trainer/LS/L3/', views.ls_l3_class_teacher, name="ls_l3_trainer"),
    path('Trainer/LS/L4/', views.ls_l4_class_teacher, name="ls_l4_trainer"),
    path('Trainer/LS/L5/', views.ls_l5_class_teacher, name="ls_l5_trainer"),
    path('Trainer/ELEC/L3/', views.elec_l3_class_teacher, name="elec_l3_trainer"),
    path('Trainer/ELEC/L4/', views.elec_l4_class_teacher, name="elec_l4_trainer"),
    path('Trainer/ELEC/L5/', views.elec_l5_class_teacher, name="elec_l5_trainer"),
    path('Trainer/SOD/L4/', views.sod_l4_class_teacher, name="sod_l4_trainer"),
    path('Trainer/SOD/L5/', views.sod_l5_class_teacher, name="sod_l5_trainer"),
    

    
    
    path('Dos/', views.dos_user, name="dos" ),
    
    path('Error_Message/', views.Error_login, name="Error"),
    
    
    
    # All Students in Patrons View
    path('patron/AllStudents/', views.all_p_students, name='all_p'),
    
    # Add, Edit and Delete All Students 
    path('patron/AllStudents/<int:id>/', views.view_cst_l3_p, name='patron_view_cst_l3'),
    path('patron/AllStudents/register/', views.add_all_p, name='patron_register_all'),
    path('patron/AllStudents/edit/<int:id>/', views.edit_all_p, name='patron_edit_all'),
    path('patron/AllStudents/delete/<int:id>/', views.delete_all_p, name='patron_delete_all'),
    
    
    #  Begining of Computer Systems technology URLS -> Patron
    path('patron/cst/l3/', views.cst_l3_p, name="patron_cst_l3"),
    
    # CST ADD, UPDATE AND DELETE URLS
    # Level 3
    path('patron/cst/l3/<int:id>/', views.view_cst_l3_p, name='patron_view_cst_l3'),
    path('patron/register/', views.add_cst_l3_p, name='patron_register_students'),
    path('patron/cst/l3/edit/<int:id>/', views.edit_cst, name='patron_edit_cst_l3'),
    path('patron/cst/l3/delete/<int:id>/', views.delete_cst_l3_p, name='patron_delete_cst_l3'),

    #  End of Computer Systems technology URLS





    #  Begining of Road Construction & Plant Operation URLS -> Patron
    path('patron/rcpo/l3/', views.rcpo_l3_p, name="patron_rcpo_l3"),
    path('patron/rcpo/l4/', views.rcpo_l4_p, name="patron_rcpo_l4"),
    path('patron/rcpo/l5/', views.rcpo_l5_p, name="patron_rcpo_l5"),
    
        # CST ADD, UPDATE AND DELETE URLS
    # Level 3

    
    

    
        
    # RCPO ADD, UPDATE AND DELETE URLS
    # Level 3
    path('patron/rcpo/l3/<int:id>/', views.view_cst_l3_p, name='patron_view_rcpo_l3'),
    path('patron/register/rcpo/l3/', views.add_rcpo_l3_p, name='patron_rcpo_l3_students'),
    path('patron/rcpo/l3/edit/<int:id>/', views.edit_rcpo_l3_p, name='patron_edit_rcpo_l3'),
    path('patron/rcpo/l3/delete/<int:id>/', views.delete_rcpo_l3_p, name='patron_delete_rcpo_l3'),
    
    # Level 4
    path('patron/rcpo/l3/<int:id>/', views.view_cst_l3_p, name='patron_view_rcpo_l3'),
    path('patron/register/rcpo/l4/', views.add_rcpo_l4_p, name='patron_rcpo_l4_students'),
    path('patron/rcpo/l4/edit/<int:id>/', views.edit_rcpo_l4_p, name='patron_edit_rcpo_l4'),
    path('patron/rcpo/l4/delete/<int:id>/', views.delete_rcpo_l4_p, name='patron_delete_rcpo_l4'),
    
    # Level 5
    path('patron/rcpo/l3/<int:id>/', views.view_cst_l3_p, name='patron_view_rcpo_l3'),
    path('patron/register/rcpo/l5/', views.add_rcpo_l5_p, name='patron_rcpo_l5_students'),
    path('patron/rcpo/l5/edit/<int:id>/', views.edit_rcpo_l5_p, name='patron_edit_rcpo_l5'),
    path('patron/rcpo/l5/delete/<int:id>/', views.delete_rcpo_l5_p, name='patron_delete_rcpo_l5'),
    

    #  End of Road Construction & Plant Operation
    
    
    
    
    
    

    #  Begining of Land Surveying URLS -> Patron
    path('patron/ls/l3/', views.ls_l3_p, name="patron_ls_l3"),
    path('patron/ls/l4/', views.ls_l4_p, name="patron_ls_l4"),
    path('patron/ls/l5/', views.ls_l5_p, name="patron_ls_l5"),
    
    
    
        # LS ADD, UPDATE AND DELETE URLS
    # Level 3
    path('patron/ls/l3/<int:id>/', views.view_cst_l3_p, name='patron_view_rcpo_l3'),
    path('patron/register/ls/l3/', views.add_ls_l3_p, name='patron_ls_l3_students'),
    path('patron/ls/l3/edit/<int:id>/', views.edit_ls_l3_p, name='patron_edit_ls_l3'),
    path('patron/ls/l3/delete/<int:id>/', views.delete_ls_l3_p, name='patron_delete_ls_l3'),
    
    # Level 4
    path('patron/ls/l3/<int:id>/', views.view_cst_l3_p, name='patron_view_rcpo_l3'),
    path('patron/register/ls/l4/', views.add_ls_l4_p, name='patron_ls_l4_students'),
    path('patron/ls/l4/edit/<int:id>/', views.edit_ls_l4_p, name='patron_edit_ls_l4'),
    path('patron/ls/l4/delete/<int:id>/', views.delete_ls_l4_p, name='patron_delete_ls_l4'),
    
    # Level 5
    path('patron/ls/l3/<int:id>/', views.view_cst_l3_p, name='patron_view_rcpo_l3'),
    path('patron/register/ls/l5/', views.add_ls_l5_p, name='patron_ls_l5_students'),
    path('patron/ls/l5/edit/<int:id>/', views.edit_ls_l5_p, name='patron_edit_ls_l5'),
    path('patron/ls/l5/delete/<int:id>/', views.delete_ls_l5_p, name='patron_delete_ls_l5'),
    
    
    
    #  End of Land Surveying URLS
    
    
    
    
    
    
    
    #  Begining of Electricity URLS -> Patron
    path('patron/elec/l3/', views.elec_l3_p, name="patron_elec_l3"),
    path('patron/elec/l4/', views.elec_l4_p, name="patron_elec_l4"),
    path('patron/elec/l5/', views.elec_l5_p, name="patron_elec_l5"),
    
            # ELEC ADD, UPDATE AND DELETE URLS
    # Level 3
    path('patron/elec/l3/<int:id>/', views.view_cst_l3_p, name='patron_view_rcpo_l3'),
    path('patron/register/elec/l3/', views.add_elec_l3_p, name='patron_elec_l3_students'),
    path('patron/elec/l3/edit/<int:id>/', views.edit_elec_l3_p, name='patron_edit_elec_l3'),
    path('patron/elec/l3/delete/<int:id>/', views.delete_elec_l3_p, name='patron_delete_elec_l3'),
    
    # Level 4
    path('patron/elec/l4/<int:id>/', views.view_cst_l3_p, name='patron_view_rcpo_l3'),
    path('patron/register/elec/l4/', views.add_elec_l4_p, name='patron_elec_l4_students'),
    path('patron/elec/l4/edit/<int:id>/', views.edit_elec_l4_p, name='patron_edit_elec_l4'),
    path('patron/elec/l4/delete/<int:id>/', views.delete_elec_l4_p, name='patron_delete_elec_l4'),
    
    # Level 5
    path('patron/elec/l5/<int:id>/', views.view_cst_l3_p, name='patron_view_rcpo_l3'),
    path('patron/register/elec/l5/', views.add_elec_l5_p, name='patron_elec_l5_students'),
    path('patron/elec/l5/edit/<int:id>/', views.edit_elec_l5_p, name='patron_edit_elec_l5'),
    path('patron/elec/l5/delete/<int:id>/', views.delete_elec_l5_p, name='patron_delete_elec_l5'),
    
    
    
    
    #  End of Electricity URLS
    
    
    
    
     
    
    #  Begining of Software Development URLS -> Patron
    path('patron/sod/l4/', views.sod_l4_p, name="patron_sod_l4"),
    path('patron/sod/l5/', views.sod_l5_p, name="patron_sod_l5"),
    
    
                # SOD ADD, UPDATE AND DELETE URLS

    # Level 4
    path('patron/sod/l4/<int:id>/', views.view_cst_l3_p, name='patron_view_rcpo_l3'),
    path('patron/register/sod/l4/', views.add_sod_l4_p, name='patron_sod_l4_students'),
    path('patron/sod/l4/edit/<int:id>/', views.edit_sod_l4_p, name='patron_edit_sod_l4'),
    path('patron/sod/l4/delete/<int:id>/', views.delete_sod_l4_p, name='patron_delete_sod_l4'),
    
    # Level 5
    path('patron/sod/l5/<int:id>/', views.view_cst_l3_p, name='patron_view_rcpo_l3'),
    path('patron/register/sod/l5/', views.add_sod_l5_p, name='patron_sod_l5_students'),
    path('patron/sod/l5/edit/<int:id>/', views.edit_sod_l5_p, name='patron_edit_sod_l5'),
    path('patron/sod/l5/delete/<int:id>/', views.delete_sod_l5_p, name='patron_delete_sod_l5'),
    
    #  End of Electricity URLS
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    # THIS IS THE DOS URLS
 
 
     # All Students in Patrons View
    path('dos/AllStudents/', views.all_d_students, name='all_d'),
    
    # Add, Edit and Delete All Students 
    path('Dos/AllStudents/<int:id>/', views.view_cst_l3_p, name='dos_view_cst_l3'),
    path('Dos/AllStudents/register/', views.add_all_d, name='dos_register_all'),
    path('Dos/AllStudents/edit/<int:id>/', views.edit_all_d, name='dos_edit_all'),
    path('Dos/AllStudents/delete/<int:id>/', views.delete_all_d, name='dos_delete_all'),
    
    
    #  Begining of Computer Systems technology URLS -> Patron
    path('Dos/cst/l3/', views.cst_l3_d, name="dos_cst_l3"),
    
    # CST ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Dos/cst/l3/<int:id>/', views.view_cst_l3_d, name='dos_view_cst_l3'),
    path('Dos/register/', views.add_cst_l3_d, name='dos_register_students'),
    path('Dos/cst/l3/edit/<int:id>/', views.edit_cst_d, name='dos_edit_cst_l3'),
    path('Dos/cst/l3/delete/<int:id>/', views.delete_cst_l3_d, name='dos_delete_cst_l3'),
    path('Dos/cst/l3/promote/<int:id>/', views.promote_cst_l3_d, name='dos_promote_cst_l3'),
    path('Dos/cst/l3/change/<int:id>/', views.change_cst_l3_d, name='dos_change_cst_l3'),

    #  End of Computer Systems technology URLS





    #  Begining of Road Construction & Plant Operation URLS -> Patron
    path('Dos/rcpo/l3/', views.rcpo_l3_d, name="dos_rcpo_l3"),
    path('Dos/rcpo/l4/', views.rcpo_l4_d, name="dos_rcpo_l4"),
    path('Dos/rcpo/l5/', views.rcpo_l5_d, name="dos_rcpo_l5"),
    
        # CST ADD, UPDATE AND DELETE URLS
    # Level 3

    
    

    
        
    # RCPO ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Dos/rcpo/l3/<int:id>/', views.view_cst_l3_d, name='dos_view_rcpo_l3'),
    path('Dos/register/rcpo/l3/', views.add_rcpo_l3_d, name='dos_rcpo_l3_students'),
    path('Dos/rcpo/l3/edit/<int:id>/', views.edit_rcpo_l3_d, name='dos_edit_rcpo_l3'),
    path('Dos/rcpo/l3/delete/<int:id>/', views.delete_rcpo_l3_d, name='dos_delete_rcpo_l3'),
    path('Dos/rcpo/l3/change/<int:id>/', views.change_rcpo_l3_d, name='dos_change_rcpo_l3'),
    path('Dos/rcpo/l3/promote/<int:id>/', views.promote_rcpo_l3_d, name='dos_promote_rcpo_l3'),


    
    # Level 4
    path('Dos/rcpo/l4/<int:id>/', views.view_cst_l3_d, name='dos_view_rcpo_l3'),
    path('Dos/register/rcpo/l4/', views.add_rcpo_l4_d, name='dos_rcpo_l4_students'),
    path('Dos/rcpo/l4/edit/<int:id>/', views.edit_rcpo_l4_d, name='dos_edit_rcpo_l4'),
    path('Dos/rcpo/l4/delete/<int:id>/', views.delete_rcpo_l4_d, name='dos_delete_rcpo_l4'),
    path('Dos/rcpo/l4/promote/<int:id>/', views.promote_rcpo_l4_d, name='dos_promote_rcpo_l4'),

    
    # Level 5
    path('Dos/rcpo/l3/<int:id>/', views.view_cst_l3_d, name='dos_view_rcpo_l3'),
    path('Dos/register/rcpo/l5/', views.add_rcpo_l5_d, name='dos_rcpo_l5_students'),
    path('Dos/rcpo/l5/edit/<int:id>/', views.edit_rcpo_l5_d, name='dos_edit_rcpo_l5'),
    path('Dos/rcpo/l5/delete/<int:id>/', views.delete_rcpo_l5_d, name='dos_delete_rcpo_l5'), 
    path('Dos/rcpo/l5/Graduates/<int:id>/', views.graduate_rcpo_l5_d, name='dos_graduate_rcpo_l5'), 
    

    #  End of Road Construction & Plant Operation
    
    
    
    
    
    

    #  Begining of Land Surveying URLS -> Patron
    path('Dos/ls/l3/', views.ls_l3_d, name="dos_ls_l3"),
    path('Dos/ls/l4/', views.ls_l4_d, name="dos_ls_l4"),
    path('Dos/ls/l5/', views.ls_l5_d, name="dos_ls_l5"),
    
    
    
        # LS ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Dos/ls/l3/<int:id>/', views.view_cst_l3_d, name='dos_view_rcpo_l3'),
    path('Dos/register/ls/l3/', views.add_ls_l3_d, name='dos_ls_l3_students'),
    path('Dos/ls/l3/edit/<int:id>/', views.edit_ls_l3_d, name='dos_edit_ls_l3'),
    path('Dos/ls/l3/delete/<int:id>/', views.delete_ls_l3_d, name='dos_delete_ls_l3'),
    path('Dos/ls/l3/change/<int:id>/', views.change_ls_l3_d, name='dos_change_ls_l3'),
    path('Dos/ls/l3/promote/<int:id>/', views.promote_ls_l3_d, name='dos_promote_ls_l3'),
    
    
    # Level 4
    path('Dos/ls/l4/<int:id>/', views.view_cst_l3_d, name='dos_view_rcpo_l3'),
    path('Dos/register/ls/l4/', views.add_ls_l4_d, name='dos_ls_l4_students'),
    path('Dos/ls/l4/edit/<int:id>/', views.edit_ls_l4_d, name='dos_edit_ls_l4'),
    path('Dos/ls/l4/delete/<int:id>/', views.delete_ls_l4_d, name='dos_delete_ls_l4'),
    path('Dos/ls/l4/promote/<int:id>/', views.promote_ls_l4_d, name='dos_promote_ls_l4'),
    
    # Level 5
    path('Dos/ls/l3/<int:id>/', views.view_cst_l3_d, name='dos_view_rcpo_l3'),
    path('Dos/register/ls/l5/', views.add_ls_l5_d, name='dos_ls_l5_students'),
    path('Dos/ls/l5/edit/<int:id>/', views.edit_ls_l5_d, name='dos_edit_ls_l5'),
    path('Dos/ls/l5/delete/<int:id>/', views.delete_ls_l5_d, name='dos_delete_ls_l5'),
    path('Dos/ls/l5/Graduates/<int:id>/', views.graduate_ls_l5_d, name='dos_graduate_ls_l5'), 
    
    
    
    #  End of Land Surveying URLS
    
    
    
    
    
    
    
    #  Begining of Electricity URLS -> Patron
    path('Dos/elec/l3/', views.elec_l3_d, name="dos_elec_l3"),
    path('Dos/elec/l4/', views.elec_l4_d, name="dos_elec_l4"),
    path('Dos/elec/l5/', views.elec_l5_d, name="dos_elec_l5"),
    
            # ELEC ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Dos/elec/l3/<int:id>/', views.view_cst_l3_d, name='dos_view_rcpo_l3'),
    path('Dos/register/elec/l3/', views.add_elec_l3_d, name='dos_elec_l3_students'),
    path('Dos/elec/l3/edit/<int:id>/', views.edit_elec_l3_d, name='dos_edit_elec_l3'),
    path('Dos/elec/l3/delete/<int:id>/', views.delete_elec_l3_d, name='dos_delete_elec_l3'),
    path('Dos/elec/l3/change/<int:id>/', views.change_elec_l3_d, name='dos_change_elec_l3'),
    path('Dos/elec/l3/promote/<int:id>/', views.promote_elec_l3_d, name='dos_promote_elec_l3'),
    
    # Level 4
    path('Dos/elec/l4/<int:id>/', views.view_cst_l3_d, name='dos_view_rcpo_l3'),
    path('Dos/register/elec/l4/', views.add_elec_l4_d, name='dos_elec_l4_students'),
    path('Dos/elec/l4/edit/<int:id>/', views.edit_elec_l4_d, name='dos_edit_elec_l4'),
    path('Dos/elec/l4/delete/<int:id>/', views.delete_elec_l4_d, name='dos_delete_elec_l4'),
    path('Dos/elec/l4/promote/<int:id>/', views.promote_elec_l4_d, name='dos_promote_elec_l4'),
    
    # Level 5
    path('Dos/elec/l5/<int:id>/', views.view_cst_l3_d, name='dos_view_rcpo_l3'),
    path('Dos/register/elec/l5/', views.add_elec_l5_d, name='dos_elec_l5_students'),
    path('Dos/elec/l5/edit/<int:id>/', views.edit_elec_l5_d, name='dos_edit_elec_l5'),
    path('Dos/elec/l5/delete/<int:id>/', views.delete_elec_l5_d, name='dos_delete_elec_l5'),
    path('Dos/elec/l5/Graduates/<int:id>/', views.graduate_elec_l5_d, name='dos_graduate_elec_l5'), 
    
    
    
    
    #  End of Electricity URLS
    
    
    
    
     
    
    #  Begining of Software Development URLS -> Patron
    path('Dos/sod/l4/', views.sod_l4_d, name="dos_sod_l4"),
    path('Dos/sod/l5/', views.sod_l5_d, name="dos_sod_l5"),
    
    
                # SOD ADD, UPDATE AND DELETE URLS

    # Level 4
    path('Dos/sod/l4/<int:id>/', views.view_cst_l3_d, name='dos_view_rcpo_l3'),
    path('Dos/register/sod/l4/', views.add_sod_l4_d, name='dos_sod_l4_students'),
    path('Dos/sod/l4/edit/<int:id>/', views.edit_sod_l4_d, name='dos_edit_sod_l4'),
    path('Dos/sod/l4/delete/<int:id>/', views.delete_sod_l4_d, name='dos_delete_sod_l4'),
    path('Dos/sod/l4/promote/<int:id>/', views.promote_sod_l4_d, name='dos_promote_sod_l4'),
    
    # Level 5
    path('Dos/sod/l5/<int:id>/', views.view_cst_l3_d, name='dos_view_rcpo_l3'),
    path('Dos/register/sod/l5/', views.add_sod_l5_d, name='dos_sod_l5_students'),
    path('Dos/sod/l5/edit/<int:id>/', views.edit_sod_l5_d, name='dos_edit_sod_l5'),
    path('Dos/sod/l5/delete/<int:id>/', views.delete_sod_l5_d, name='dos_delete_sod_l5'),
    path('Dos/sod/l5/Graduates/<int:id>/', views.graduate_sod_l5_d, name='dos_graduate_sod_l5'), 
    
    #  End of Electricity URLS
    
    # Start The GRADUATES
    
    path('Dos/Graduates/', views.graduates_d, name='graduates_d'),
    # End The GRADUATES
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Burser URLS 
    
    
    
        # All Students in Patrons View
    path('Accountant/AllStudents/', views.all_b_students, name='all_b'),
    
    # Add, Edit and Delete All Students 
    path('Accountant/AllStudents/<int:id>/', views.view_cst_l3_p, name='burser_view_cst_l3'),
    path('Accountant/AllStudents/register_new/', views.add_all_b, name='burser_register_all'),
    path('Accountant/Payement/<int:id>/', views.add_all_payement, name='burser_Fee_payment_through_all_students'),
    path('Accountant/AllStudents/edit/<int:id>/', views.edit_all_b, name='burser_edit_all'),
    path('Accountant/AllStudents/delete/<int:id>/', views.delete_all_b, name='burser_delete_all'),
    
    

    # Student Status -> 

    # Boarding Scholars
    path('Accountant/Boarding Scholars/', views.boarding_students, name='Boarding_Scholar'),
    path('Accountant/Boarding Scholars/Payement/<int:id>/', views.boarding_payement, name='Fee_payment_students_bording'),
    path('Accountant/Boarding Scholars/Payement/Verification/', views.fee_payement_verification, name='fee_payement_verification'),
    path('Accountant/Boarding Scholars/edit/<int:id>/', views.edit_boarding_b, name='burser_edit_boarding'),
    path('Accountant/Boarding Scholars/Payement/Verification/<int:id>/', views.financial_boarding, name='financial_verification_boarding'),

    # Day Scholars

    path('Accountant/Day Scholars/', views.day_students, name='day_Scholar'),
    path('Accountant/Day Scholars/Payement/<int:id>/', views.day_payement, name='Fee_payment_students_day'),
    path('Accountant/Day Scholars/Payement/Verification/', views.fee_payement_verification, name='fee_payement_verification'),
    path('Accountant/Day Scholars/Payement/Verification/<int:id>/', views.financial_day, name='financial_verification_day'),

    # Boarding_fixed_fee
    path('Accountant/Boarding/fixed_fee/', views.boarding_fix_fee, name='boarding_fix'),
    path('Accountant/Day/fixed_fee/', views.day_fix_fee, name='day_fix'),


# edit_boarding_b
    #  Begining of Computer Systems technology URLS -> Patron
    path('Accountant/cst/l3/', views.cst_l3_b, name="burser_cst_l3"),
    
    # CST ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Accountant/cst/l3/<int:id>/', views.view_cst_l3_b, name='burser_view_cst_l3'),
    path('Accountant/register/', views.add_cst_l3_b, name='burser_register_students'),
    path('Accountant/Payement/cst/<int:id>/', views.add_cst_l3_payement, name='burser_Fee_payment_students'),
    path('Accountant/Payement/Verification/', views.fee_payement_verification, name='fee_payement_verification'),
    path('Accountant/Payement/Verification/Boarding/<int:id>/', views.financial_cst, name='financial_payement_verification'),
    path('Accountant/Payement/Verification/Day/<int:id>/', views.financial_day, name='financial_payement_verification_day'),
    path('Accountant/cst/l3/edit/<int:id>/', views.edit_cst_b, name='burser_edit_cst_l3'),
    path('Accountant/cst/l3/delete/<int:id>/', views.delete_cst_l3_b, name='burser_delete_cst_l3'),

    #  End of Computer Systems technology URLS





    #  Begining of Road Construction & Plant Operation URLS -> Patron
    path('Accountant/rcpo/l3/', views.rcpo_l3_b, name="burser_rcpo_l3"),
    path('Accountant/rcpo/l4/', views.rcpo_l4_b, name="burser_rcpo_l4"),
    path('Accountant/rcpo/l5/', views.rcpo_l5_b, name="burser_rcpo_l5"),
    
        # CST ADD, UPDATE AND DELETE URLS
    # Level 3

    
    

    
        
    # RCPO ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Accountant/rcpo/l3/<int:id>/', views.view_cst_l3_b, name='burser_view_rcpo_l3'),
    path('Accountant/register/rcpo/l3/', views.add_rcpo_l3_b, name='burser_rcpo_l3_students'),
    path('Accountant/Payement/rcpo/l3/<int:id>/', views.add_rcpo_l3_payement, name='burser_Fee_payment_rcpo_l3_students'),
    path('Accountant/rcpo/l3/edit/<int:id>/', views.edit_rcpo_l3_b, name='burser_edit_rcpo_l3'),
    path('Accountant/rcpo/l3/delete/<int:id>/', views.delete_rcpo_l3_b, name='burser_delete_rcpo_l3'),
    
    # Level 4
    path('Accountant/rcpo/l3/<int:id>/', views.view_cst_l3_b, name='burser_view_rcpo_l3'),
    path('Accountant/register/rcpo/l4/', views.add_rcpo_l4_b, name='burser_rcpo_l4_students'),
    path('Accountant/rcpo/l4/edit/<int:id>/', views.edit_rcpo_l4_b, name='burser_edit_rcpo_l4'),
    path('Accountant/Payement/rcpo/l4/<int:id>/', views.add_rcpo_l4_payement, name='burser_Fee_payment_rcpo_l4_students'),
    path('Accountant/rcpo/l4/delete/<int:id>/', views.delete_rcpo_l4_b, name='burser_delete_rcpo_l4'),
    
    # Level 5
    path('Accountant/rcpo/l3/<int:id>/', views.view_cst_l3_b, name='burser_view_rcpo_l3'),
    path('Accountant/register/rcpo/l5/', views.add_rcpo_l5_b, name='burser_rcpo_l5_students'),
    path('Accountant/Payement/rcpos/l5/<int:id>/', views.add_rcpo_l5_payement, name='burser_Fee_payment_rcpo_l5_students'),
    path('Accountant/rcpo/l5/edit/<int:id>/', views.edit_rcpo_l5_b, name='burser_edit_rcpo_l5'),
    path('Accountant/rcpo/l5/delete/<int:id>/', views.delete_rcpo_l5_b, name='burser_delete_rcpo_l5'),
    

    #  End of Road Construction & Plant Operation
    
    
    
    
    
    

    #  Begining of Land Surveying URLS -> Patron
    path('Accountant/ls/l3/', views.ls_l3_b, name="burser_ls_l3"),
    path('Accountant/ls/l4/', views.ls_l4_b, name="burser_ls_l4"),
    path('Accountant/ls/l5/', views.ls_l5_b, name="burser_ls_l5"),
    
    
    
        # LS ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Accountant/ls/l3/<int:id>/', views.view_cst_l3_b, name='burser_view_rcpo_l3'),
    path('Accountant/register/ls/l3/', views.add_ls_l3_b, name='burser_ls_l3_students'),
    path('Accountant/ls/l3/edit/<int:id>/', views.edit_ls_l3_b, name='burser_edit_ls_l3'),
    path('Accountant/Payement/ls/l3/<int:id>/', views.add_ls_l3_payement, name='burser_Fee_payment_ls_l3_students'),
    path('Accountant/ls/l3/delete/<int:id>/', views.delete_ls_l3_b, name='burser_delete_ls_l3'),
    
    # Level 4
    path('Accountant/ls/l3/<int:id>/', views.view_cst_l3_b, name='burser_view_rcpo_l3'),
    path('Accountant/register/ls/l4/', views.add_ls_l4_b, name='burser_ls_l4_students'),
    path('Accountant/ls/l4/edit/<int:id>/', views.edit_ls_l4_b, name='burser_edit_ls_l4'),
    path('Accountant/Payement/ls/l4/<int:id>/', views.add_ls_l4_payement, name='burser_Fee_payment_ls_l4_students'),
    path('Accountant/ls/l4/delete/<int:id>/', views.delete_ls_l4_b, name='burser_delete_ls_l4'),
    
    # Level 5
    path('Accountant/ls/l3/<int:id>/', views.view_cst_l3_b, name='burser_view_rcpo_l3'),
    path('Accountant/register/ls/l5/', views.add_ls_l5_b, name='burser_ls_l5_students'),
    path('Accountant/ls/l5/edit/<int:id>/', views.edit_ls_l5_b, name='burser_edit_ls_l5'),
    path('Accountant/Payement/ls/l5/<int:id>/', views.add_ls_l5_payement, name='burser_Fee_payment_ls_l5_students'),
    path('Accountant/ls/l5/delete/<int:id>/', views.delete_ls_l5_b, name='burser_delete_ls_l5'),
    
    
    
    #  End of Land Surveying URLS
    
    
    
    
    
    
    
    #  Begining of Electricity URLS -> Patron
    path('Accontant/elec/l3/', views.elec_l3_b, name="burser_elec_l3"),
    path('Accontant/elec/l4/', views.elec_l4_b, name="burser_elec_l4"),
    path('Accontant/elec/l5/', views.elec_l5_b, name="burser_elec_l5"),
    
            # ELEC ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Accontant/elec/l3/<int:id>/', views.view_cst_l3_b, name='burser_view_rcpo_l3'),
    path('Accontant/register/elec/l3/', views.add_elec_l3_b, name='burser_elec_l3_students'),
    path('Accontant/elec/l3/edit/<int:id>/', views.edit_elec_l3_b, name='burser_edit_elec_l3'),
    path('Accountant/Payement/elec/l3/<int:id>/', views.add_elec_l3_payement, name='burser_Fee_payment_elec_l3_students'),
    path('Accontant/elec/l3/delete/<int:id>/', views.delete_elec_l3_b, name='burser_delete_elec_l3'),
    
    # Level 4
    path('Accontant/elec/l4/<int:id>/', views.view_cst_l3_b, name='burser_view_rcpo_l3'),
    path('Accontant/register/elec/l4/', views.add_elec_l4_b, name='burser_elec_l4_students'),
    path('Accontant/elec/l4/edit/<int:id>/', views.edit_elec_l4_b, name='burser_edit_elec_l4'),
    path('Accountant/Payement/elec/l4/<int:id>/', views.add_elec_l4_payement, name='burser_Fee_payment_elec_l4_students'),
    path('Accontant/elec/l4/delete/<int:id>/', views.delete_elec_l4_b, name='burser_delete_elec_l4'),
    
    # Level 5
    path('Accontant/elec/l5/<int:id>/', views.view_cst_l3_b, name='burser_view_rcpo_l3'),
    path('Accontant/register/elec/l5/', views.add_elec_l5_b, name='burser_elec_l5_students'),
    path('Accontant/elec/l5/edit/<int:id>/', views.edit_elec_l5_b, name='burser_edit_elec_l5'),
    path('Accountant/Payement/elec/l5/<int:id>/', views.add_elec_l5_payement, name='burser_Fee_payment_elec_l5_students'),
    path('Accontant/elec/l5/delete/<int:id>/', views.delete_elec_l5_b, name='burser_delete_elec_l5'),
    
    
    
    
    #  End of Electricity URLS
    
    
    
    
     
    
    #  Begining of Software Development URLS -> Patron
    path('Accountant/sod/l4/', views.sod_l4_b, name="burser_sod_l4"),
    path('Accountant/sod/l5/', views.sod_l5_b, name="burser_sod_l5"),
    
    
                # SOD ADD, UPDATE AND DELETE URLS

    # Level 4
    path('Accountant/sod/l4/<int:id>/', views.view_cst_l3_b, name='burser_view_rcpo_l3'),
    path('Accountant/register/sod/l4/', views.add_sod_l4_b, name='burser_sod_l4_students'),
    path('Accountant/sod/l4/edit/<int:id>/', views.edit_sod_l4_b, name='burser_edit_sod_l4'),
    path('Accountant/Payement/sod/l4/<int:id>/', views.add_sod_l4_payement, name='burser_Fee_payment_sod_l4_students'),
    path('Accountant/sod/l4/delete/<int:id>/', views.delete_sod_l4_b, name='burser_delete_sod_l4'),
    
    # Level 5
    path('Accountant/sod/l5/<int:id>/', views.view_cst_l3_b, name='burser_view_rcpo_l3'),
    path('Accountant/register/sod/l5/', views.add_sod_l5_b, name='burser_sod_l5_students'),
    path('Accountant/sod/l5/edit/<int:id>/', views.edit_sod_l5_b, name='burser_edit_sod_l5'),
    path('Accountant/Payement/sod/l5/<int:id>/', views.add_sod_l5_payement, name='burser_Fee_payment_sod_l5_students'),
    path('Accountant/sod/l5/delete/<int:id>/', views.delete_sod_l5_b, name='burser_delete_sod_l5'),
    
    #  End of Electricity URLS
 
 











    # Start of Teachers URLS 

    # CST Class Teacher

       
    #  Begining of Computer Systems technology URLS -> Patron
    path('Trainer/CST/List', views.cst_l3_teacher, name="cst_l3_teacher"),
    
    # CST ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Dos/cst/l3/<int:id>/', views.view_cst_l3_d, name='dos_view_cst_l3'),
    path('Trainer/CST/List/<int:id>/', views.promote_cst_l3_teacher, name='promote_cst_l3_teacher'),
    path('Trainer/CST/day/', views.day_students_for_cst, name='day_Scholar_cst_teacher'),
    path('Trainer/CST/boarding/', views.boarding_students_for_cst, name='boarding_students_for_cst'),


    # RCPO Class Teacher

       
    #  Begining of Computer Systems technology URLS -> Patron
    path('Trainer/RCPO/L3/List', views.rcpo_l3_teacher, name="rcpo_l3_teacher"),
    
    # RCPO ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Dos/RCPO/l3/<int:id>/', views.view_cst_l3_d, name='dos_view_cst_l3'),
    path('Trainer/RCPO/L3/List/<int:id>/', views.promote_rcpo_l3_teacher, name='promote_rcpo_l3_teacher'),
    path('Trainer/RCPO/L3/day/', views.day_students_for_rcpo, name='day_Scholar_rcpo_l3_teacher'),
    path('Trainer/RCPO/L3/boarding/', views.boarding_students_for_rcpo, name='boarding_students_for_rcpo_l3'),



    path('Trainer/RCPO/L4/List', views.rcpo_l4_teacher, name="rcpo_l4_teacher"),
    # Level 4
    path('Dos/RCPO/l4/<int:id>/', views.view_cst_l3_d, name='dos_view_cst_l4'),
    path('Trainer/RCPO/L4/List/<int:id>/', views.promote_rcpo_l4_teacher, name='promote_rcpo_l4_teacher'),
    path('Trainer/RCPO/L4/day/', views.day_students_for_rcpo_l4, name='day_Scholar_rcpo_l4_teacher'),
    path('Trainer/RCPO/L4/boarding/', views.boarding_students_for_rcpo_l4, name='boarding_students_for_rcpo_l4'),


    path('Trainer/RCPO/L5/List', views.rcpo_l5_teacher, name="rcpo_l5_teacher"),
    # Level 5
    path('Dos/RCPO/l5/<int:id>/', views.view_cst_l3_d, name='dos_view_cst_l5'),
    path('Trainer/RCPO/L5/List/<int:id>/', views.promote_rcpo_l5_teacher, name='promote_rcpo_l5_teacher'),
    path('Trainer/RCPO/L5/day/', views.day_students_for_rcpo_l5, name='day_Scholar_rcpo_l5_teacher'),
    path('Trainer/RCPO/L5/boarding/', views.boarding_students_for_rcpo_l5, name='boarding_students_for_rcpo_l5'),
    path('Trainer/RCPO/L5/Graduates/<int:id>/', views.graduate_rcpo_l5_t, name='trainer_graduate_rcpo_l5'), 
    




    #  Begining of Land Surveying URLS -> Trainer
    path('Trainer/LS/L3/List', views.ls_l3_teacher, name="ls_l3_teacher"),
    
    # RCPO ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Dos/LS/l3/<int:id>/', views.view_cst_l3_d, name='dos_view_cst_l3'),
    path('Trainer/LS/L3/List/<int:id>/', views.promote_ls_l3_teacher, name='promote_ls_l3_teacher'),
    path('Trainer/LS/L3/day/', views.day_students_for_ls_l3, name='day_Scholar_ls_l3_teacher'),
    path('Trainer/LS/L3/boarding/', views.boarding_students_for_ls_l3, name='boarding_students_for_ls_l3'),



    #  Begining of Land Surveying URLS -> Trainer
    path('Trainer/LS/L4/List', views.ls_l4_teacher, name="ls_l4_teacher"),
    
    # RCPO ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Trainer/LS/L4/<int:id>/', views.view_cst_l3_d, name='dos_view_cst_l3'),
    path('Trainer/LS/L4/List/<int:id>/', views.promote_ls_l4_teacher, name='promote_ls_l4_teacher'),
    path('Trainer/LS/L4/day/', views.day_students_for_ls_l4, name='day_Scholar_ls_l4_teacher'),
    path('Trainer/LS/L4/boarding/', views.boarding_students_for_ls_l4, name='boarding_students_for_ls_l4'),


    #  End of Computer Systems technology URLS

    #  Begining of Land Surveying URLS -> Trainer
    path('Trainer/LS/L5/List', views.ls_l5_teacher, name="ls_l5_teacher"),
    
    # RCPO ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Trainer/LS/L5/<int:id>/', views.view_cst_l3_d, name='dos_view_cst_l3'),
    path('Trainer/LS/L5/day/', views.day_students_for_ls_l5, name='day_Scholar_ls_l5_teacher'),
    path('Trainer/LS/L5/boarding/', views.boarding_students_for_ls_l5, name='boarding_students_for_ls_l5'),
    path('Trainer/LS/L5/Graduates/<int:id>/', views.graduate_ls_l5_t, name='trainer_graduate_ls_l5'), 


    #  End of Computer Systems technology URLS
    



    #  Begining of Land Surveying URLS -> Trainer
    path('Trainer/ELEC/L3/List', views.elec_l3_teacher, name="elec_l3_teacher"),
    
    # RCPO ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Trainer/ELEC/l3/<int:id>/', views.view_cst_l3_d, name='dos_view_cst_l3'),
    path('Trainer/ELEC/L3/List/<int:id>/', views.promote_elec_l3_teacher, name='promote_elec_l3_teacher'),
    path('Trainer/ELEC/L3/day/', views.day_students_for_elec_l3, name='day_Scholar_elec_l3_teacher'),
    path('Trainer/ELEC/L3/boarding/', views.boarding_students_for_elec_l3, name='boarding_students_for_elec_l3'),



    #  Begining of Land Surveying URLS -> Trainer
    path('Trainer/ELEC/L4/List', views.elec_l4_teacher, name="elec_l4_teacher"),
    
    # RCPO ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Trainer/ELEC/l4/<int:id>/', views.view_cst_l3_d, name='dos_view_cst_l3'),
    path('Trainer/ELEC/L4/List/<int:id>/', views.promote_elec_l4_teacher, name='promote_elec_l4_teacher'),
    path('Trainer/ELEC/L4/day/', views.day_students_for_elec_l4, name='day_Scholar_elec_l4_teacher'),
    path('Trainer/ELEC/L4/boarding/', views.boarding_students_for_elec_l4, name='boarding_students_for_elec_l4'),


    #  Begining of Land Surveying URLS -> Trainer
    path('Trainer/ELEC/L5/List', views.elec_l5_teacher, name="elec_l5_teacher"),
    
    # RCPO ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Trainer/ELEC/l5/<int:id>/', views.view_cst_l3_d, name='dos_view_cst_l3'),
    path('Trainer/ELEC/L5/day/', views.day_students_for_elec_l5, name='day_Scholar_elec_l5_teacher'),
    path('Trainer/ELEC/L5/boarding/', views.boarding_students_for_elec_l5, name='boarding_students_for_elec_l5'),
    path('Trainer/ELEC/L5/Graduates/<int:id>/', views.graduate_elec_l5_t, name='trainer_graduate_elec_l5'), 




 

    #  Begining of Land Surveying URLS -> Trainer
    path('Trainer/SOD/L4/List', views.sod_l4_teacher, name="sod_l4_teacher"),
    
    # RCPO ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Trainer/SOD/l4/<int:id>/', views.view_cst_l3_d, name='dos_view_cst_l3'),
    path('Trainer/SOD/L4/List/<int:id>/', views.promote_sod_l4_teacher, name='promote_sod_l4_teacher'),
    path('Trainer/SOD/L4/day/', views.day_students_for_sod_l4, name='day_Scholar_sod_l4_teacher'),
    path('Trainer/SOD/L4/boarding/', views.boarding_students_for_sod_l4, name='boarding_students_for_sod_l4'),




 

    #  Begining of Land Surveying URLS -> Trainer
    path('Trainer/SOD/L5/List', views.sod_l5_teacher, name="sod_l5_teacher"),
    
    # RCPO ADD, UPDATE AND DELETE URLS
    # Level 3
    path('Trainer/SOD/l5/<int:id>/', views.view_cst_l3_d, name='dos_view_cst_l3'),

    path('Trainer/SOD/L5/day/', views.day_students_for_sod_l5, name='day_Scholar_sod_l5_teacher'),
    path('Trainer/SOD/L5/boarding/', views.boarding_students_for_sod_l5, name='boarding_students_for_sod_l5'),
    path('Trainer/SOD/L5/Graduates/<int:id>/', views.graduate_sod_l5_t, name='trainer_graduate_sod_l5'), 


 
 
 

]