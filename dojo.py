from docopt import docopt

usage = '''
    Office Space Allocation

    Usage:
        dojo.py create_room <room_type> <room_name> ...
        dojo.py add_person <person_name> <position> [<wants_accommodation>] 
        dojo.py allocate_room <position> <person_name> <room_type> <room_name>
'''  

args = docopt(usage)
# print(args)

def output_created_rooms(room_type, room_names):
    if room_type == 'office':
        for room_name in room_names:
            print('An {} called {} has been created'.format(room_type, room_name))
    else:
        for room_name in room_names:
            print('A {} called {} has been created'.format(room_type, room_name))



if args ['create_room']:
   allowed_room_types = ['office', 'living_space']
   room_type = args['<room_type>'].lower()
   room_names = args['<room_name>']
   if room_type in allowed_room_types:
       output_created_rooms(room_type, room_names)
   else:
       print('{} is not a valid room type'. format(room_type))

def output_added_people(person_name, position):
    if position == 'fellow':
        print('{} {} has been successfully added'.format( position, person_name))
    else:
        print('{} {} has been successfully added'.format( position, person_name))

if args ['add_person']:
    person_name = args['<person_name>'].capitalize()
    position = args['<position>'].capitalize()    
    allowed_positions = ['Fellow', 'Staff']
    if position in allowed_positions:
        output_added_people(person_name, position)
    else:
        print('{} is not a valid position'. format(position))

# if args ['allocate_room']:
#     position = args['<position>'].capitalize()    
#     allowed_positions = ['Fellow', 'Staff']
#     if position in allowed_positions:
#         output_added_people(person_name, position)
#     else:
#         print('{} is not a valid position'. format(position))
#     if room_type in allowed_room_types:
#         output_created_rooms(room_type, room_names)
#     else:
#         print('{} is not a valid room type'. format(room_type))
# print('{} {} has been allocated {} {}'.format(position, person_name, room_type, room_name))