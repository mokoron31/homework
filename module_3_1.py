calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    return {len(string), string.upper(), string.lower()}

def is_contains(string,list):
    count_calls()
    if string in list:
        return True
    return False
print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(calls)
