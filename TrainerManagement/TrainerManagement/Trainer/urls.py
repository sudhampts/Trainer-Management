from django.urls import path

from Trainer import views

urlpatterns = [
    path('',views.home,name='home'),
    path('logread',views.log_read),    # login credentials

    path('reg',views.reg_home,name='reg'),   # registeration home page
    path('regdata',views.reg_data),   # Trainer registration credentials
    path('trainerhome',views.trainer_home,name='trainerhome'),   # trainer home page
    path('batchdetails',views.batch_details,name='batchdet'),  # batch details

    path('adminhome',views.admin_home,name='adminhome'),   # admin home page
    path('assign',views.assign_page,name='assign'),  # batch assigning page
    path('trainerassign',views.trainer_assign,name='trainerassign'),   # assigning trainer for a batch
    path('trainerdetails',views.trainer_details,name='trainerdetails'),   # trainer details
    path('assignbatch',views.assigned_batch,name='assigned'),  # assigned batch details
    path('update/<int:id>',views.update_batch,name='update'),
    path('delete/<int:id>',views.delete_batch,name='delete')

]