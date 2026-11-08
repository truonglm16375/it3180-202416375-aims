def search_by_title(items, keyword):
    if not keyword:
        return []
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]