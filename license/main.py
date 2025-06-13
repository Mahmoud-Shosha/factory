from verification_utils import load_public_key, load_signed_key, verify_signature

LOG_TAG = ">> EXPERTS-VISION LICENSE >>"

if __name__ == "__main__":
    print(f"{LOG_TAG} 🕵️‍♂️ Starting license verification ...")
    public_key = load_public_key()
    signed_key = load_signed_key()
    verify_signature(public_key, signed_key["data"], signed_key["signature"])
