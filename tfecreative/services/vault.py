import functools
import hvac
from tfecreative import settings


class VaultService:
    client = None
    shares = 5
    threshold = 3

    def __init__(self):
        self.client = hvac.Client(url=settings.CRYPT_VAULT_URL)
        self.initialize_client()
        self.authenticate_client()

    def initialize_client(self):
        if self.client.sys.is_initialized:
            return
        result = self.client.sys.initialize(shares, threshold)
        self.client.token = result.get("root_token", "")

        sealed = self.client.sys.is_sealed()
        if not sealed:
            return

        keys = result.get("keys", None)
        if not keys:
            raise ValueError("No keys found")
        client.sys.submit_unseal_key(keys[0])
        client.sys.submit_unseal_key(keys[1])
        client.sys.submit_unseal_key(keys[2])

    def authenticate_client(self):
        if self.client.is_authenticated():
            return
        self.client.token = settings.CRYPT_VAULT_TOKEN

    def get_secret(self, path):
        secret = self.client.secrets.kv.v2.read_secret_version(mount_point='kv', path=path)
        return secret
