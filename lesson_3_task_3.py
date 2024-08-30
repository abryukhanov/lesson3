from mailing import Mailing
from address import Address

mailing = Mailing(
    to_address=Address("12345", "Москва", "Ленинский проспект", "12", "34"),
    from_address=Address("54321", "Санкт-Петербург", "Невский проспект", "21", "12"),
    cost=1000,
    track="1234567890"
)

print(mailing)