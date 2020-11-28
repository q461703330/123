from have_money import saved_money
from send_money import send_money
from select_money import select_money


print(saved_money)
saved_money = send_money(saved_money)
select_money(saved_money)


print(saved_money)