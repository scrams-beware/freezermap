# === Stage 8: Постраничный вывод ===
# Project: FreezerMap
page = 1
size = 10
items = []
total_pages = 0


def set_page(new_page):
    global page
    page = max(1, min(new_page, total_pages if total_pages else 1))


def set_size(new_size):
    global size
    size = max(1, new_size)


def recalculate(total_count):
    global total_pages
    total_pages = (total_count + size - 1) // size if size else 0
    if page > total_pages:
        page = 1


def get_start():
    return (page - 1) * size


def get_end():
    return get_start() + size


def get_page_items():
    start = get_start()
    end = min(get_end(), len(items))
    return items[start:end]


def get_total_pages():
    return total_pages


def get_page():
    return page


def get_size():
    return size
