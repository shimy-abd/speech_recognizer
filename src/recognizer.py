import speech_recognition


class Recognizer:

    def main(self):
        recognizer = speech_recognition.Recognizer()
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    recognizer.adjust_for_ambient_noise(mic, 0.5)
                    print("Ok, I'm listening...")
                    audio = recognizer.listen(mic)
                    text_list = recognizer.recognize_google(audio)
                    print(f"Right, you said: {text_list}")
            except speech_recognition.UnknownValueError:
                print("Sorry I didn't get that :(")
            except Exception as e:
                print(f"exception: {e}")
            exit(1)


Recognizer().main()
