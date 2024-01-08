import os
from pathlib import Path
import requests

RVC_DOWNLOAD_LINK = "https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/"

BASE_DIR = Path(__file__).resolve().parent.parent


def dl_model(link, model_name, dir_name):
    file_path = os.path.join(dir_name, model_name)
    file_exists = os.path.exists(file_path)
    if file_exists:
        return
    with requests.get(f"{link}{model_name}") as r:
        r.raise_for_status()
        os.makedirs(os.path.dirname(dir_name / model_name), exist_ok=True)
        with open(dir_name / model_name, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


if __name__ == "__main__":
    print("Downloading hubert_base.pt...")
    dl_model(RVC_DOWNLOAD_LINK, "hubert_base.pt", BASE_DIR / "assets/hubert")
    print("Downloading rmvpe.pt...")
    dl_model(RVC_DOWNLOAD_LINK, "rmvpe.pt", BASE_DIR / "assets/rmvpe")
    print("Downloading vocals.onnx...")


    rvc_models_dir = BASE_DIR / "assets/pretrained"

    print("Downloading pretrained models:")

    model_names = [
        "f0D48k.pth",
        "f0G48k.pth",
    ]

    rvc_models_dir = BASE_DIR / "assets/pretrained_v2"

    print("Downloading pretrained models v2:")

    for model in model_names:
        print(f"Downloading {model}...")
        dl_model(RVC_DOWNLOAD_LINK + "pretrained_v2/", model, rvc_models_dir)

    print("Downloading uvr5_weights:")

    rvc_models_dir = BASE_DIR / "assets/uvr5_weights"

    print("All models downloaded!")
import os
from pathlib import Path
import requests

RVC_DOWNLOAD_LINK = "https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/"

BASE_DIR = Path(__file__).resolve().parent.parent


def dl_model(link, model_name, dir_name):
    file_path = os.path.join(dir_name, model_name)
    file_exists = os.path.exists(file_path)
    if file_exists:
        return
    with requests.get(f"{link}{model_name}") as r:
        r.raise_for_status()
        os.makedirs(os.path.dirname(dir_name / model_name), exist_ok=True)
        with open(dir_name / model_name, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


if __name__ == "__main__":
    print("Downloading hubert_base.pt...")
    dl_model(RVC_DOWNLOAD_LINK, "hubert_base.pt", BASE_DIR / "assets/hubert")
    print("Downloading rmvpe.pt...")
    dl_model(RVC_DOWNLOAD_LINK, "rmvpe.pt", BASE_DIR / "assets/rmvpe")
    print("Downloading vocals.onnx...")


    rvc_models_dir = BASE_DIR / "assets/pretrained"

    print("Downloading pretrained models:")

    model_names = [
        "f0D40k.pth",
        "f0G40k.pth",
    ]

    rvc_models_dir = BASE_DIR / "assets/pretrained_v2"

    print("Downloading pretrained models v2:")

    for model in model_names:
        print(f"Downloading {model}...")
        dl_model(RVC_DOWNLOAD_LINK + "pretrained_v2/", model, rvc_models_dir)

    print("Downloading uvr5_weights:")

    rvc_models_dir = BASE_DIR / "assets/uvr5_weights"

    print("All models downloaded!")
