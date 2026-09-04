booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

######### EXPECTED OUTPUT #########
""" Event code: EVT-2026
Name: Alice_Wong
Room: ROOM-305
Time: 14:30
Email domain: unimail.edu
VIP tag count: 2
Valid event code: True
Valid username: True
Valid room: True
Valid time: True
Valid email: True """


booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

parts = booking.strip().split(' | ')

event_code = parts[0]
name = parts[1]
room = parts[2]
time = parts[3]
email = parts[4]
vip_tag = parts[5]


name_parts = name.split('_')
name_formatted = '_'.join([part.capitalize() for part in name_parts])

room_formatted = room.upper()
email_domain = email.split('@')[1].lower()
vip_count = vip_tag.count('VIP')


valid_event = event_code.startswith('EVT-') and len(event_code.split('-')[1]) == 4 and event_code.split('-')[1].isdigit()
valid_username = '_' in name and name.replace('_', '').isalpha()
valid_room = room.startswith('Room-') and room.split('-')[1].isdigit()
valid_time = ':' in time and len(time.split(':')) == 2 and all(part.isdigit() for part in time.split(':'))
valid_email = '@' in email and '.' in email.split('@')[1]

print(f'Event code: {event_code}')
print(f'Name: {name_formatted}')
print(f'Room: {room_formatted}')
print(f'Time: {time}')
print(f'Email domain: {email_domain}')
print(f'VIP tag count: {vip_count}')
print(f'Valid event code: {valid_event}')
print(f'Valid username: {valid_username}')
print(f'Valid room: {valid_room}')
print(f'Valid time: {valid_time}')
print(f'Valid email: {valid_email}')

print('\n' + '='*50 + '\n')