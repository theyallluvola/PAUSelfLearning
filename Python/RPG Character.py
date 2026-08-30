full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return  'The character name should be a string'
    elif name == '':
        return 'The character should have a name'
    elif len(name) > 10:
        return 'The character name is too long'
    elif " " in name:
        return 'The character name should not contain spaces'
    elif not isinstance(strength, int):
        return 'All stats should be integers'
    elif not isinstance(intelligence, int):
        return 'All stats should be integers'
    elif not isinstance(charisma, int):
        return 'All stats should be integers'
    elif strength < 1:
        return 'All stats should be no less than 1'
    elif intelligence < 1:
        return 'All stats should be no less than 1'
    elif charisma < 1:
        return 'All stats should be no less than 1'
    elif strength > 4:
        return 'All stats should be no more than 4'
    elif intelligence > 4:
        return 'All stats should be no more than 4'
    elif charisma > 4:
        return 'All stats should be no more than 4'
    elif strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    else:
        strength_gui = (full_dot * strength) + (empty_dot * (10-strength))
        intelligence_gui = (full_dot * intelligence) + (empty_dot * (10-intelligence))
        charisma_gui = (full_dot * charisma) + (empty_dot * (10-charisma))
        return name + '\nSTR ' + strength_gui + '\nINT ' + intelligence_gui + '\nCHA ' + charisma_gui

create_character('ren', 4, 2, 1)