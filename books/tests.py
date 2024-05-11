from django.test import TestCase

from bs4 import BeautifulSoup

from .scraper import extract_data


class BookScraperTestCase(TestCase):

    def test_extract_data(self):
        """
        test that data extraction works as expected from the HTML block
        """
        sample_data = """
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
        parsed = BeautifulSoup(sample_data, "html.parser")
        title, price = extract_data(parsed)
        self.assertEqual(title, "A Light in the Attic")
        self.assertEqual(price, "£51.77")
