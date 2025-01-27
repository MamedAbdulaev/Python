from address import Address
from mailing import Mailing
to_address= Address ("344000","Ростов","ул.Комсомольская", "д.135", "141")
from_address= Address ("355000","Ставрополь", "ул.Чапаева","д.4","463")
mailing = Mailing (to_address,from_address,1000,"5qwer")
print (f"Отправление {mailing.track} из {from_address.city},{from_address.street},{from_address.home}-{from_address.flat} в {to_address.city},{to_address.street},{to_address.home}-{to_address.flat}.Стоимость {mailing.cost} рублей."
)