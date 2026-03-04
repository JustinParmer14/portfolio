import os
import urllib.request
import urllib.parse
from urllib.error import URLError

os.makedirs('assets/images', exist_ok=True)

urls_to_names = {
    "https://teal-right-clownfish-557.mypinata.cloud/ipfs/bafybeigeoweqpqnnhlmgbx6ymj25aapciltg7ps6be2wbchlxenivyui2q": "og_image.jpg",
    "https://assets.codepen.io/16179665/IMG_3091.jpg": "IMG_3091.jpg",
    "https://assets.codepen.io/16179665/Burnin%20Rubber%20Logo.png": "Burnin_Rubber_Logo.png",
    "https://assets.codepen.io/16179665/Cup%20Series%20Playoff%20Grid%20Round%20of%208%20Talladega.png": "Cup_Series_Playoff_Grid_Round_of_8_Talladega.png",
    "https://assets.codepen.io/16179665/Truck%20Series%20Playoff%20Grid%20Round%20of%208%20Talladega.png": "Truck_Series_Playoff_Grid_Round_of_8_Talladega.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Northwestern_University_seal.svg/250px-Northwestern_University_seal.svg.png": "Northwestern_University_seal.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/University_of_Missouri_logo.svg/1920px-University_of_Missouri_logo.svg.png": "University_of_Missouri_logo.png",
    "https://upload.wikimedia.org/wikipedia/en/thumb/3/39/Big_Ten_Network_Logo.svg/1280px-Big_Ten_Network_Logo.svg.png": "Big_Ten_Network_Logo.png",
    "https://assets.codepen.io/16179665/5MlKbySt_400x400.jpg": "5MlKbySt_400x400.jpg",
    "https://assets.codepen.io/16179665/KOMU_2023.svg": "KOMU_2023.svg",
    "https://assets.codepen.io/16179665/1631303859276.jpeg": "1631303859276.jpeg",
    "https://assets.codepen.io/16179665/FSLogo_1040x585_1.jpg": "FSLogo_1040x585_1.jpg",
    "https://upload.wikimedia.org/wikipedia/en/e/e8/Daytona_500_2022_Logo.png": "Daytona_500_2022_Logo.png",
    "https://upload.wikimedia.org/wikipedia/commons/8/80/Kansas_Speedway_Logo.png": "Kansas_Speedway_Logo.png",
    "https://1000logos.net/wp-content/uploads/2021/07/Missouri-Tigers-logo.png": "Missouri-Tigers-logo.png",
    "https://cdn.prod.website-files.com/695d833ae7baf7a3f70dfc64/695d833ae7baf7a3f70e019b_WNIT_TransparentBckgrnd.png": "WNIT_TransparentBckgrnd.png",
    "https://pbs.twimg.com/profile_banners/774776936983764994/1645546383/1500x500": "header_bg.jpg",
    "https://pbs.twimg.com/profile_images/1340363366166626304/K1nxSqZW_400x400.jpg": "podcast_bg.jpg"
}

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'), ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')]
urllib.request.install_opener(opener)

for url, name in urls_to_names.items():
    filepath = os.path.join('assets/images', name)
    try:
        # Check if the URL has spaces and escape them
        # Wait, the dictionary has spaces as %20 already in python
        # But we pass the string directly to urlretrieve
        urllib.request.urlretrieve(url, filepath)
        print(f"Downloaded {name}")
    except URLError as e:
        print(f"Failed to download {name} from {url}: {e.reason}")
    except Exception as e:
        print(f"Failed to download {name} from {url}: {e}")
