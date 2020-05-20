## refer to zoo1.jpg file for the tree

def get_yes_no():
    ret = input('yes/no? ')
    if ret == 'yes' or ret == 'no':
        return ret
    else:
        print('yes or no answer please')
        return(get_yes_no())

def add_new_node(current_node,ans_to_change,new_animal,new_question,ans_for_new_animal):
    node = {'question' : new_question}
    old_animal = parent_node[ans_to_change]

    if ans_for_new_animal == 'yes':
        node['yes'] = new_animal
        node['no'] = old_animal
    else:
        node['no'] = new_animal
        node['yes'] = old_animal

    parent_node[ans_to_change] = node

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

        print('Did I get it right?')
        r=get_yes_no()
        if r == 'no':
            print('dangit!')
            new_animal = input('what animal were you thinking of?')
            new_question = input('Give me a question to separate ' + next_node + ' from ' + new_animal + ':')
            print('And what would be the answer for ',new_animal,'?')
            ans_for_new_animal = get_yes_no()

            add_new_node(current_node, ans, new_animal, new_question, ans_for_new_animal)
        else:
            print('yeah!')

        current_node=root_node

    current_node = current_node[ans]