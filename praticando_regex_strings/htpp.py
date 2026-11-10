url = input('Digite a url: ')
if url.startswith('https://') and url.endswith('.com'):
    print('URL valida!')
else:
    print('URL inválida!')
