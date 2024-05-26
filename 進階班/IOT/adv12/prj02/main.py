import whisper

model = whisper.load_model("base")
result = model.transcribe("adv12/prj02/20240526.m4a")
print(result["text"])
