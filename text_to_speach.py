import requests
import json
import time

from typing import List, Dict


class EdenAI:
    providers: List[str] = [
        "openai", "deepgram", "google", "elevenlabs",
        "ibm", "lovoai", "microsoft", "amazon",
    ]
    languages: Dict[str, str] = {
        "russian": "ru-RU", "english": "en-US", "spanish": "es-ES",
        "french": "fr-FR", "german": "de-DE", "italian": "it-IT",
        "chinese": "zh-CN", "japanese": "ja-JP", "korean": "ko-KR",
        "portuguese": "pt-BR", "turkish": "tr-TR", "thai": "th-TH",
        "vietnamese": "vi-VN", "arabic": "ar-SA", "hebrew": "he-IL",
        "indonesian": "id-ID", "malay": "ms-MY", "dutch": "nl-NL",
        "finnish": "fi-FI", "swedish": "sv-SE", "norwegian": "no-NO",
    }
    genders: List[str] = ["MALE", "FEMALE"]

    def __init__(self, API_KEY: str, language: str = "ru-RU", providers: str = "lovoai", gender: str = "MALE") -> None:
        self.API_KEY = API_KEY
        self.language = self.__correct_language__(language)
        self.providers = self.__correct_providers__(providers)
        self.gender = self.__correct_gender__(gender)

    def __correct_language__(self, language: str) -> str:
        if language in self.languages:
            return self.languages[language]
        elif language in self.languages.values():
            return language
        raise ValueError("Language not found")

    def __correct_providers__(self, providers: str) -> str:
        if providers in self.providers:
            return providers
        raise ValueError("Providers not found")

    def __correct_gender__(self, gender: str) -> str:
        if gender.upper() in self.genders:
            return gender.upper()
        raise ValueError("Gender not found")

    def text_to_speach(self, text: str, file_name: str) -> None:
        headers = {"Authorization": "Bearer {key}".format(key=self.API_KEY)}
        url = "https://api.edenai.run/v2/audio/text_to_speech"

        payload = {
            "providers": f"{self.providers}/ru-RU_Pyotr Semenov",
            "language": self.language,
            "option": self.gender,
            "text": text
        }
        response = requests.post(url, json=payload, headers=headers)
        result = json.loads(response.text)

        try:
            audio_url = result[self.providers]["audio_resource_url"]
            r = requests.get(audio_url)

            file_name = file_name or str(int(time.time()))
            with open(f"{file_name}.mp3", "wb") as f:
                f.write(r.content)
        except KeyError:
            print("Error: {err}".format(err=result.get('No more credits')))
        except AttributeError:
            if result.get("detail") == "Invalid Api Key":
                print("Invalid Api Key")
            else:
                raise

    def get_supported_models_by_language(self, language: str = 'en') -> Dict[str, str | List[str]]:
        with open("models.json", "r", encoding="utf-8") as f:
            data_models = json.load(f)

        result = {}

        for model, data in data_models.items():
            result[model] = [mod for mod in data if mod.startswith(language)]

        return result
