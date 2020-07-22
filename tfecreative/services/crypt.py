import logging
from uuid import uuid4
from decouple import config

from .vault import VaultService
from tfecreative import settings


logger = logging.getLogger(__name__)


class Crypt:
    uuid = uuid4()
    vault_service = None

    def __init__(self):
        self.vault_service = VaultService()

    def get_env_secrets(self):
        try:
            response = self.vault_service.get_secret(settings.CRYPT_VAULT_ENV_PATH)
            data = response['data']
            return data.get('data')
        except Exception:
            logger.error('Failed to retreive vault env secrets')
            return {}

if __name__ == "__main__":
    crypt = Crypt()
