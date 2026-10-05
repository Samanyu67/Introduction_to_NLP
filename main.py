import requests
from config import HF_API_KEY 

MODEL_ID = "facebook/bart-large-mnli"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}
TOPICS = {"Sports", "Technology", "Buisness", "Politics", "Health"}

def ask_hf(headline: str):
    payload = {"input": headline, "parameters": {"candidate_labels": TOPICS}}
    r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
    if not r.ok:
        raise RuntimeError(f"HF error {r.status_code} {r.text}")
    return r.json()

def best_topic(preds):
    best = max(preds, key=lambda x: x["score"])
    return best["label"], best["score"]

def bar(score):
    pct = score * 100
    blocks = int(pct // 10)
    return "█" * blocks + "░" * (10 - blocks)

def show(headline: str, preds: list):
    top_label, top_score = best_topic(preds)
    print("\n" + "=" * 60)
    print("News Topic Classifier")
    print("=" * 60)
    print(f"headline, {headline}")
    print(f"best_topic, {top_label}")
    print(f"Confidence: {round(top_score * 100,1)}%, [{bar(top_score)}]")
    print("\n top 3 scoren :")
    top3 = sorted(preds, key=lambda x: x["score"], reverse=True)[:3]
    for i, p in enumerate(top3, start=1):
        print(f"{i}. {p['label']:<11} {round(p['score']*100,1)}% [{bar(p['score'])}]")
    print("="*60)

def main():
    print("Type a news headline & I'll guess the topic")
    print("Topics", ",".join(TOPICS))
    print("type exit to stop\n")

    while True:
        headline = input("Headline").strip()
        if headline.lower() == 'exit':
            print("Thank you for playing")
            break
        if not headline:
            print("Type in a new headline")
            continue
        try:
            preds = ask_hf(headline)
            if isinstance(preds, list) and preds and "label" in preds[0]:
                show(headline, preds)
            else:
                print("Oops! Unexpected Reply", preds)
        except Exception as e:
            print("An error has occured", e)

if __name__ == "__main__":
    main()
