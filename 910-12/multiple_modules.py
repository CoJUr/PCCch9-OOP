import user
import users

my_user = user.User('jim', 'crow', 'jcrew', 'jc@email.com', 'texas')

my_admin = users.Admin('becky', 'crow', 'bcrew', 'becky@email.com', 'texas')
my_admin.privileges.show_privileges()
