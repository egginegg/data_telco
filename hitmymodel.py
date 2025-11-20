#make requiest to this URL:https://eggineggpredicts.azurewebsites.net/api/Predict?code=wn7iS0uBEPlzHkeFq_J-ZfXdUmIMRGg5FnrjLObiDOyfAzFujZ3xMA==

import requests
t = 12
m = 90
ts = 0

response = requests.get(
    f"https://eggineggpredicts.azurewebsites.net/api/Predict?code=wn7iS0uBEPlzHkeFq_J-ZfXdUmIMRGg5FnrjLObiDOyfAzFujZ3xMA==&tenure={t}&monthly={m}&techsupport={ts}"
)
print(response.text)