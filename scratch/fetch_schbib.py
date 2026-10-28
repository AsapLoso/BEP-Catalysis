import urllib.request
import re
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
urls = [
    'https://sci-hub.se/10.1021/ie950600k',
    'https://sci-hub.st/10.1021/ie950600k',
    'https://sci-hub.ru/10.1021/ie950600k'
]

os.makedirs('research/literature', exist_ok=True)
dest = 'research/literature/schbib_1996_front_end_kinetics.pdf'

success = False
for u in urls:
    try:
        print(f"Trying {u}...")
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read()
            html = content.decode('utf-8', errors='ignore')
            m = re.search(r'src=["\']([^"\']+\.pdf[^"\']*)["\']', html)
            if not m:
                m = re.search(r'location\.href=["\']([^"\']+\.pdf[^"\']*)["\']', html)
            if m:
                pdf_url = m.group(1)
                if pdf_url.startswith('//'):
                    pdf_url = 'https:' + pdf_url
                elif pdf_url.startswith('/'):
                    pdf_url = 'https://' + urllib.parse.urlparse(u).netloc + pdf_url
                print(f"Found PDF url: {pdf_url}")
                req_pdf = urllib.request.Request(pdf_url, headers=headers)
                with urllib.request.urlopen(req_pdf, timeout=20) as presp:
                    data = presp.read()
                    if len(data) > 10000:
                        with open(dest, 'wb') as f:
                            f.write(data)
                        print(f"Successfully downloaded {len(data)} bytes to {dest}")
                        success = True
                        break
                    else:
                        print(f"Downloaded payload too small: {len(data)} bytes")
            else:
                print("No PDF iframe/embed found in response.")
    except Exception as e:
        print(f"Failed {u}: {e}")

if not success:
    print("Could not download via Sci-Hub.")
