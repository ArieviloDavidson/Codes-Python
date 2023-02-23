import speech_recognition as sr

# Inicialize o reconhecedor de voz
r = sr.Recognizer()

# Captura o áudio do microfone
with sr.Microphone() as source:
    print("Diga algo:")
    audio = r.listen(source)

# Reconhece a fala
try:
    print("Você disse: " + r.recognize_google(audio, language='pt-BR'))
except sr.UnknownValueError:
    print("Não foi possível entender o que você disse")
except sr.RequestError as e:
    print("Erro ao chamar o serviço de reconhecimento de voz: {0}".format(e))
