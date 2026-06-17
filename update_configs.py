import requests

# လမ်းကြောင်းအမှန်ဖြစ်သော Free V2Ray Source Links များ
SOURCES = [
    "https://githubusercontent.com",
    "https://githubusercontent.com",
    "https://githubusercontent.com"
]

def main():
    unique_configs = set()
    
    for url in SOURCES:
        try:
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                for line in res.text.splitlines():
                    line = line.strip()
                    # vmess, vless, ss, trojan များကို စစ်ထုတ်ယူခြင်း
                    if any(line.startswith(p) for p in ["vmess://", "vless://", "ss://", "trojan://"]):
                        unique_configs.add(line)
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            
    # အများဆုံး Config အခု ၅၀ သာ ကန့်သတ်သိမ်းဆည်းခြင်း
    limited_configs = list(unique_configs)[:50]
    
    # sub.txt ဖိုင်ထဲသို့ ပြန်လည်ရေးသားခြင်း
    with open("sub.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(limited_configs))
    print(f"Successfully updated {len(limited_configs)} configs.")

if __name__ == "__main__":
    main()
