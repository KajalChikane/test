import requests
from urllib.parse import quote

HEADERS = {
    "User-Agent": "AI-Agent-Learning/1.0 (contact: example@email.com)"
}

def search_wikipedia(query: str) -> str:
    try:
        # STEP 1: SEARCH
        search_url = "https://en.wikipedia.org/w/api.php"
        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json"
        }

        search_response = requests.get(
            search_url,
            params=search_params,
            headers=HEADERS,
            timeout=5
        )

        if search_response.status_code != 200:
            return "Search service unavailable."

        search_data = search_response.json()

        results = search_data.get("query", {}).get("search", [])
        if not results:
            return "No results found."

        # STEP 2: FIRST RESULT TITLE
        title = results[0]["title"]

        # STEP 3: FETCH SUMMARY
        safe_title = quote(title)
        summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{safe_title}"

        summary_response = requests.get(
            summary_url,
            headers=HEADERS,
            timeout=5
        )

        if summary_response.status_code != 200:
            return "No summary available."

        summary_data = summary_response.json()
        return summary_data.get("extract", "No summary available.")

    except requests.exceptions.RequestException:
        return "Network error while searching Wikipedia."

    except ValueError:
        return "Received invalid response from Wikipedia."
