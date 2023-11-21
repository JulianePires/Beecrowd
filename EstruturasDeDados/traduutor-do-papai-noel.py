def treatByCountry(country):
  greetings = {
      "brasil": "Feliz Natal!",
      "espanha": "Feliz Navidad!",
      "alemanha": "Frohliche Weihnachten!",
      "austria": "Frohe Weihnacht!",
      "coreia": "Chuk Sung Tan!",
      "egito": "Mutlu Noeller",
      "grecia": "Kala Christougena!",
      "estados-unidos": "Merry Christmas!",
      "inglaterra": "Merry Christmas!",
      "australia": "Merry Christmas!",
      "portugal": "Feliz Natal!",
      "suecia": "God Jul!",
      "turquia": "Mutlu Noeller",
      "argentina": "Feliz Navidad!",
      "chile": "Feliz Navidad!",
      "mexico": "Feliz Navidad!",
      "antardida": "Merry Christmas!",
      "canada": "Merry Christmas!",
      "irlanda": "Nollaig Shona Dhuit!",
      "belgica": "Zalig Kerstfeest!",
      "italia": "Buon Natale!",
      "libia": "Buon Natale!",
      "siria": "Milad Mubarak!",
      "marrocos": "Milad Mubarak!",
      "japao": "Merii Kurisumasu!"
  }

  return greetings.get(country, "--- NOT FOUND ---")


while True:
  try:
    inputCountry = input()
    print(treatByCountry(inputCountry))
  except EOFError:
    break
