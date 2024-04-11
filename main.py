import time
print("ciao, sono un programma che ti spiega il linguaggio moderno")
time.sleep(1)
while True:
    parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")
    meme_dict = {"CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante","LOL": "Una risposta comune a qualcosa di divertente",'SHEESH':'leggera disapprovazione','CREEPY':'spaventoso, inquietante','PARA':'preoccuparsi per qualcosa, paranoiarsi','PHYTON':'linguaggio di programmazione utilizzato da noi👍'}
    if parola in meme_dict.keys():
    # Cosa fare se la parola è stata trovata?
        print(meme_dict[parola])
    # Cosa fare se la parola non è stata trovata?
    else:
        print("scegli un'altra parola, grazie")
