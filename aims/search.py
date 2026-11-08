def search_by_category(items, category):
    """Tìm kiếm đĩa DVD theo thể loại (không phân biệt hoa thường)."""
    if not category:
        return []
    return [dvd for dvd in items if dvd.category and category.lower() in dvd.category.lower()]

def search_by_title(items, keyword):
    if not keyword:
        return []
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]