"""Demonstrates how to import a module and use its classes."""

import users

my_admin = users.Admin('jim', 'crow', 'jcrew', 'jcrow@laws.com', 'texas')
my_admin.privileges.show_privileges()
