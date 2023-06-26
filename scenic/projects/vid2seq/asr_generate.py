from google.cloud import speech
from google.oauth2 import service_account

import io

client = speech.SpeechClient()
credentials = service_account.Credentials.from_service_account_file("test_user.json")
# scoped_credentials = credentials.with_scopes(["https://speech.googleapis.com"])

path = 'video/1min_3rd_sample.flac'
with io.open(path, "rb") as audio_file:
    content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        #encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=32000,
        language_code="en-US",
        # Enable automatic punctuation
        enable_automatic_punctuation=True,
        )

    response = client.recognize(config=config, audio=audio)
    print(response)
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print("First alternative of result {}".format(i))
        print("Transcript: {}".format(alternative.transcript))
