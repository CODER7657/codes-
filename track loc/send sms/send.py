import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '+91 9428231049',
  'message': 'hii saale muthaal insann ',
  'key': 'textbelt',
})
print(resp.json())