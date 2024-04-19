import requests
import json

def get_free_games_with_discount(url):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        game_urls = []
        for element in data['data']['Catalog']['searchStore']['elements']:
            discount_price = element['price']['totalPrice']['discountPrice']
            original_price = element['price']['totalPrice']['originalPrice']
            page_slug = element.get('productSlug')
            if not page_slug:
                for mapping in element['catalogNs']['mappings']:
                    if mapping['pageType'] == 'productHome':
                        page_slug = mapping['pageSlug']
                        break
            if discount_price == 0 and original_price != 0:
                game_url = f"https://store.epicgames.com/zh-Hant/p/{page_slug}"
                game_urls.append(game_url)

        return game_urls
    else:
        print("Failed to retrieve data from the URL.")
        return None

if __name__ == "__main__":
    url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"
    free_game_urls = get_free_games_with_discount(url)
    if free_game_urls:
        for game_url in free_game_urls:
            print(game_url)
    else:
        print("無法獲取免費遊戲資訊")
