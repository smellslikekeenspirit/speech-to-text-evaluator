import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud import storage
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    'api-key.json')

storage_client = storage.Client()
# Instantiates a client
client = speech.SpeechClient(credentials=credentials)
bucket = storage_client.get_bucket('ntid_bucket')
print(bucket)
# The name of the audio file to transcribe
gcs_uri = 'gs://' + 'ntid_bucket' + '/' + 'Global_Travel_DIptanu_Rerecord.flac'

client = speech.SpeechClient()
audio = speech.RecognitionAudio(uri=gcs_uri)


config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz=44100,
    language_code="en-US",
)

# Detects speech in the audio file
operation = client.long_running_recognize(config=config, audio=audio)
response = operation.result(timeout=10000)
for result in response.results:
    print(result.alternatives[0].transcript.strip())
