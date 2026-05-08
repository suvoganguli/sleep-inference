from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PATHS = {
    "raw_data": BASE_DIR / "data" / "raw",
    "processed_data": BASE_DIR / "data" / "processed",
    "figures": BASE_DIR / "outputs" / "figures",
    "models": BASE_DIR / "outputs" / "models",
}

def savefig(fig, name):
    fig.savefig(PATHS["figures"] / f"{name}.png", dpi=300, bbox_inches="tight")

def varsave(obj, name):
    import pickle
    with open(PATHS["processed_data"] / f"{name}.pkl", "wb") as f:
        pickle.dump(obj, f)
