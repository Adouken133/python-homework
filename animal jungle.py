def jungle_animal(animal, my_speed):
    if animal == 'zebra':
        return 'Try to ride a zebra!'
    if animal == 'cheetah':
        if my_speed > 115:
            return 'Run!'
        else:
            return 'stay calm and wait!'
    else:
        return 'Introduce yourself!'


print jungle_animal('cheetah',114)
