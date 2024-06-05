"""La librería gtts (Google Text-to-Speech) de Python se utiliza para convertir texto a habla utilizando el servicio de Google Translate. 
Es una herramienta muy útil para aplicaciones que necesitan sintetizar voz a partir de texto, como en asistentes virtuales, 
sistemas de notificación por voz, aplicaciones educativas, entre otros."""

from gtts import gTTS

file = open("F:/Python/Proyectos_python/AudioLibro/libro.txt", "r", encoding="utf-8")
textbook = file.read()
file.close()

audio = gTTS(text=textbook, lang="es")
audio.save("F:/Python/Proyectos_python/AudioLibro/audioBook.mp3")