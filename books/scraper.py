import requests

from bs4 import BeautifulSoup
from celery import shared_task

from .models import Book


def extract_data(book_data):
    """
    this extraction is separated so that one can unit test the logic
    example input:
    <article class="product_pod">
        <div class="image_container">
                <a href="a-light-in-the-attic_1000/index.html">
                <img src="2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
        </div>
        <p class="star-rating Three">
            <i class="icon-star"></i>
            <i class="icon-star"></i>
            <i class="icon-star"></i>
            <i class="icon-star"></i>
            <i class="icon-star"></i>
        </p>
        <h3><a href="a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
        <div class="product_price">
            <p class="price_color">£51.77</p>
            <p class="instock availability"><i class="icon-ok"></i>In stock</p>
            <form>
                <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">
                Add to basket
                </button>
            </form>
        </div>
    </article>
    """
    title = book_data.find('h3').find('a')["title"]
    price = book_data.find('p', class_="price_color").text.strip()
    return title, price


@shared_task
def scrape_books(base_url="https://books.toscrape.com/"):
    page = requests.get(base_url)
    parsed = BeautifulSoup(page.content, "html.parser")
    all_books = parsed.find_all("article", class_="product_pod")
    for book_data in all_books:
        title, price = extract_data(book_data)
        Book.objects.create(title=title, price=price)

