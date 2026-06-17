import requests

# ပိုမိုမြန်ဆန်ပြီး ပိတ်မထားသော Free V2Ray Subscription Links အသစ်များ
SOURCES = [
    "https://githubusercontent.com",
    "https://githubusercontent.com",
    "https://githubusercontent.com"
]

def main():
    unique_configs = set()
    
    for url in SOURCES:
        try:
            # timeout ကို ၁၅ စက္ကန့်အထိ တိုးမြှင့်ထားပါတယ်
            res = requests.get(url, timeout=15)
            if res.status_code == 200:
                for line in res.text.splitlines():
                    line = line.strip()
                    # vmess, vless, ss, trojan, tuic, hy2 များကို စစ်ထုတ်ယူခြင်း
                    if any(line.startswith(p) for p in ["vmess://", "vless://", "ss://", "trojan://", "tuic://", "hysteria2://"]):
                        unique_configs.add(line)
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            
    # အများဆုံး Config အခု ၁၀၀ အထိ သိမ်းဆည်းခိုင်းပါမယ်
    limited_configs = list(unique_configs)[:100]
    
    with open("sub.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(limited_configs))
    print(f"Successfully updated {len(limited_configs)} configs.")

if __name__ == "__main__":
    main()
