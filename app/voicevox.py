import logging
import httpx as requests
from asyncio import run, gather

# ロガー設定
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Voicevox:
    """
    VoiceVox API client for text-to-speech synthesis.
    """

    def __init__(self, host: str = "http://localhost:50021", speaker_id: int = 1):
        self.host = host
        self.speaker_id = speaker_id

    # audio_query
    async def audio_query(self, text: str) -> dict:
        try:
            async with requests.AsyncClient() as client:
                # curl -v -s -X POST "http://localhost:50021/audio_query?speaker=1" --get --data-urlencode text@example/text.txt > example/query.json

                payload = {'text': text, 'speaker': self.speaker_id}
                response = await client.post(
                    f"{self.host}/audio_query",
                    params=payload
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            logger.error(f"Error occurred while querying audio: {e}")
            return {}

    # synthesize
    async def synthesize(self, query: dict, speaker_id: int = 1) -> bytes:
        try:
            async with requests.AsyncClient() as client:
                response = await client.post(
                    f"{self.host}/synthesis?speaker={self.speaker_id}",
                    json=query
                )
                response.raise_for_status()
                return response.content
        except Exception as e:
            logger.error(f"Error occurred while synthesizing speech: {e}")
            return b""
