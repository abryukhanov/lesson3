from user import User

my_user = User("Андрей", "Брюханов")
method_names = dir(my_user)
my_user.print_first_name()
my_user.print_last_name()
my_user.print_full_name()