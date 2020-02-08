def phone(strng, num):
    import re
    
    if not '+' + num in strng:
        return 'Error => Not found: ' + num
    
    if strng.count('+' + num) > 1:
        return 'Error => Too many people: ' + num
    
    strng = '\n' + strng
    line = re.search(r'\n(.*{0}.*)\n'.format(num), strng)[1]
    
    name = re.search(r'<(.*)>', line)[1]
    
    address = re.sub(r'{0}|{1}|[<>+;/$*!?,:]'.format(num, name), '', line)
    address = re.sub('_', ' ', address)
    address = re.sub('  ', ' ', address)
    address = address.strip()
    
    return 'Phone => {0}, Name => {1}, Address => {2}'.format(num, name, address)
