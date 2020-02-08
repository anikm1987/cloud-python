import secrets

import uuid

for i in range(5):
  print(secrets.token_hex(2))
  print(uuid.uuid4())