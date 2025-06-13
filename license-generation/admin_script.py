import base64
import json
from pathlib import Path

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding

key_size = 3072
output_dir = Path(".")
private_key_path = output_dir / "private_key.pem"
public_key_path = output_dir / "public_key.pem"
private_key_password = b"password"


def save_key_files(private_key, public_key):
    with open(private_key_path, "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.BestAvailableEncryption(private_key_password)
            )
        )
    print(f"✅ Saved private key → {private_key_path}")
    with open(public_key_path, "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )
    print(f"✅ Saved public key → {public_key_path}")


def generate_key_pair():
    print("🔐 Generating RSA key pair ...")
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
    )
    public_key = private_key.public_key()
    save_key_files(private_key, public_key)


def sign_data(key, dest_file):
    print("🔐 Loading private key ...")
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=private_key_password,
            backend=default_backend()
        )

    print("✍️ Signing the data ...")
    signature = private_key.sign(key, padding.PKCS1v15(), hashes.SHA512())
    payload = {
        "data": base64.b64encode(key).decode(),
        "signature": base64.b64encode(signature).decode()
    }
    with open(output_dir / dest_file, "w") as f:
        json.dump(payload, f, indent=2)
    print(f"📄 Signed payload written to → {output_dir / dest_file}")
    print("✅ Done.")


if __name__ == "__main__":
    # generate_key_pair()
    key = (b"{"
           b"'company_id': 'ebrahem_factory',"
           b"'host_id': 'CDD9524A-7CAD-4CFE-8259-94B47FFE44E2',"
           b"'expiry': '20-06-2025'"
           b"}")
    sign_data(key, "signed_key.json")
