from pprint import pprint

import requests
import bs4
import xlsxwriter
from django.shortcuts import redirect

from book.models import Book


def get_data_emag(request):

    url = "https://www.emag.ro/search/carti?ref=effective_search"
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    cases = soup.find_all('div', class_='card-v2')
    all_books = {'data': []}

    for case in cases:
        data = {}
        name_of_book = case.find('a', class_='card-v2-title semibold mrg-btm-xxs js-product-url')
        book_price = case.find('p', class_='product-new-price')
        if name_of_book is None:
            data['book_name'] = 'No data available'
        else:
            data['book_name'] = name_of_book.text
        if book_price is None:
            data['price'] = 'No data available'
        else:
            data['price'] = book_price.text
        all_books['data'].append(data)
    for book in all_books['data']:
        Book.objects.create(book_name=book.get('book_name'),
                            author_last_name='meh',
                            author_first_name='meeh',
                            book_type='d',
                            book_year='122',
                            book_rating=4.2,
                            book_quantity='12',
                            book_description='dddd')
    # workbook = xlsxwriter.Workbook('Books.xlsx') ## to save in Excel file
    # worksheet = workbook.add_worksheet('list of books')
    #
    # row = 0
    # col = 0
    # for book in all_books['data']:
    #     worksheet.write(row, col, book['book_name'])
    #     worksheet.write(row, col + 1, book['price'])
    #     row +=1
    # workbook.close()
    return redirect('home')
