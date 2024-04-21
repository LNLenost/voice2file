import speech_recognition as sr
import os

def recognize_speech():
    # Inizializza il recognizer
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        # Utilizza Google Speech Recognition per convertire l'audio in testo
        text = r.recognize_google(audio, language='it-IT')
        print(f"You said: {text}")
        return text.lower()  # Converti il testo in minuscolo per facilitare il confronto
    except sr.UnknownValueError:
        print("This is not the chosen word!")
        return ""
    except sr.RequestError as e:
        print(f"oof Google Speech ain't working. Here's the error: {e}")
        return ""

def main():
    # Parola da rilevare per aprire il file
    target_word = "xxx"

    while True:
        # Ascolta il microfono e riconosci il testo
        spoken_text = recognize_speech()

        # Controlla se la parola target è presente nel testo riconosciuto
        if target_word in spoken_text:
            # Apri il file desiderato
            file_path = "xxx"  # Inserisci il percorso del tuo file
            try:
                os.startfile(file_path)  # Apre il file con l'applicazione predefinita
                print(f"File opened: {file_path}")
            except FileNotFoundError:
                print(f"You have to put a file in this directory: {file_path}")

if __name__ == "__main__":
    main()