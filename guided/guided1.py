#Este es el primer ejercicio guiado
 
who = str(input('Who is asking? '))
cause = str(input('Cause? '))
cuantity =  str(input('Cuantity? '))
years = str(input('years? '))
percentage = str(input('What is the percentage? '))
ngoldcoins = str(input('What is the number of gold coins? '))
 
 
text = (f'\n\n\nDear Governor of the Iron Bank,\n' +
'Given the current situation that King’s Landing is facing, the House {who} is asking for your economic services because\n' +
'of the following cause {cause}.\n' +
'The estimated total quantity is {cauntity} gold coins. The loan will be returned during the {years} following years with\n' +
'{percentage} % of bank interest. Thus, the money recovered from the bank, once the loan is completely returned, will be {ngoldcoins}\n' +
'gold coins.\n' +
'I hope the bank will consider this proposal because the House {who} always pays its debts.\n' +
'Signed:\n' +
'Lord Mace Tyrell\n' +
'Lannister’s Master of Coin\n' +
'Lord of Highgarden and Warden of the South\n')
print(text)