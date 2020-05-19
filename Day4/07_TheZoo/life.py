## refer to zoo1.jpg file for the tree

def get_yes_no():
    ret = input('yes/no? ')
    if ret == 'yes' or ret == 'no':
        return ret
    else:
        print('yes or no answer please')
        return(get_yes_no())

root_node = {
    'question' : 'does it live on land?',
    'no' : {
            'question' : 'does it have 8 arms?',
            'yes' : 'octopus',
             'no' : 'fish'
            },
    'yes' : {
            'question' : 'does it live on a farm?',
            'yes' : {
                'question' : 'can I milk that rascal?',
                'no' : 'rooster',
                'yes' : 'cow'
            },
            'no': 'lion'
            }
}

#root_node['no'] = node3
#print(root_node['no']['yes'])

current_node = root_node

while True:
    print(current_node['question'])
    ans = get_yes_no()

    next_node = current_node[ans]

    if isinstance(next_node,dict):
        current_node = current_node
    else:
        print('My guess is', next_node)
        break

    current_node = current_node[ans]