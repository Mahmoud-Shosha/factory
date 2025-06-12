import base64
import json
from pathlib import Path
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

from stopping_utils import shutdown

script_dir = Path(__file__).resolve().parent
signed_key_path = script_dir / "signed_key.json"
public_key_path = script_dir / "public_key.pem"
LOG_TAG = ">> EXPERTS-VISION LICENSE >>"


def load_public_key():
    print(f"{LOG_TAG} Loading public key from {public_key_path} ...")
    try:
        with open(public_key_path, "rb") as f:
            return serialization.load_pem_public_key(f.read())
    except Exception as e:
        print(f"{LOG_TAG} Failed to load public key: {e}")
        shutdown()


def load_signed_key():
    print(f"{LOG_TAG} Loading signed key from {signed_key_path} ...")
    try:
        with open(signed_key_path, "r") as f:
            payload = json.load(f)
        data = base64.b64decode(payload["data"])
        signature = base64.b64decode(payload["signature"])
        return {"data": data, "signature": signature}
    except Exception as e:
        print(f"{LOG_TAG} Failed to load or decode signed key: {e}")
        shutdown()


def verify_signature(public_key, data, signature):
    print(f"{LOG_TAG} Verifying signature ...")
    try:
        public_key.verify(signature, data, padding.PKCS1v15(), hashes.SHA512())
        # Ensure expiry date, hardware id
        print(f"{LOG_TAG} ✅ License is valid")
    except InvalidSignature:
        print(f"{LOG_TAG} ❌ License is invalid")
        shutdown()
