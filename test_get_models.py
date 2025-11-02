import os
import sys
import dotenv 
dotenv.load_dotenv('.env.development')

# Prefer importing via the package (works when installed). If running locally
# from the repo root, add the parent directory to sys.path so the package is
# importable as 'Lukrum_models_client'.
try:
    from Lukrum_models_client.api_client import LukrumModelsAPIClient
    from Lukrum_models_client.config import ModelsAPIConfig
except ImportError:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from Lukrum_models_client.api_client import LukrumModelsAPIClient
    from Lukrum_models_client.config import ModelsAPIConfig


def main() -> int:
    api_key = os.getenv("LUKRUM_MODELS_API_KEY")
    print(api_key)
    base_url = os.getenv("LUKRUM_MODELS_BASE_URL", ModelsAPIConfig().base_url)
    print(base_url)

    if not api_key:
        print("Error: LUKRUM_MODELS_API_KEY environment variable is not set.")
        print("Set it and re-run, e.g.: export LUKRUM_MODELS_API_KEY=\"your-api-key\"")
        return 1

    config = ModelsAPIConfig(base_url=base_url, api_key=api_key)

    # Use context manager to ensure clean session closing
    with LukrumModelsAPIClient(config=config) as client:
        models = client.get_models()
        print(f"Total models: {len(models)}")
        for m in models[:5]:
            name = getattr(m, "name", None)
            uuid = getattr(m, "model_uuid", None)
            print(f"- {name} (uuid={uuid})")

    return 0


if __name__ == "__main__":
    sys.exit(main())


