"""
1105. Filling Bookcase Shelves

You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book.
You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth,
then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by
the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf,
the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

Example 1:
Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.
Example 2:

Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
Output: 4
"""
from typing import List

width_idx = 0
height_idx = 1


# Iterative approach
def iterative(books: List[List[int]], shelfWidth: int) -> int:
    minimum_heights = [0 for _ in range(len(books))]
    minimum_heights[0] = books[0][height_idx]

    for current_book_idx in range(1, len(books)):
        known_height = minimum_heights[current_book_idx-1]
        minimum_height = known_height + books[current_book_idx][height_idx]

        width = books[current_book_idx][width_idx]
        for book_idx in range(current_book_idx-1, -1, -1):
            width += books[book_idx][width_idx]
            if width > shelfWidth:
                break
            updated_height = minimum_heights[book_idx-1] + max(height for (_, height) in books[book_idx: current_book_idx+1])
            minimum_height = min(minimum_height, updated_height)
        minimum_heights[current_book_idx] = minimum_height
    return minimum_heights[-1]







# This solution passes all the tests
# It's more cache friendly and that adding cache here is crucial for performance since it is recursive
def another_recursive(books: List[List[int]], shelfWidth: int) -> int:
    cache = {}
    def calculate_minimum_height(current_book: int, remaining_shelf_width: int, max_height: int = 0) -> int:
        cache_key = (current_book, remaining_shelf_width, max_height)
        cache_result = cache.get(cache_key)
        if cache_result is not None:
            return cache_result
        if current_book >= len(books):
            return max_height
        book_width, book_height = books[current_book]
        # Add book to the new shelf
        new_shelf = max_height + calculate_minimum_height(current_book+1, shelfWidth-book_width, book_height)

        # Add book to the current shelf
        add_book = float('inf')
        if remaining_shelf_width >= book_width:
            add_book = calculate_minimum_height(current_book+1, remaining_shelf_width-book_width, max(book_height, max_height))

        result = min(new_shelf, add_book)
        cache[cache_key] = result
        return result

    return calculate_minimum_height(0, shelfWidth, 0)


# recursive approach
# tried to submit it as is but it exeeds time limit
# It takes really long time to pass the last test
def recursive(books: List[List[int]], shelfWidth: int) -> int:
    result = calculate_minimum_height(books, shelfWidth, [])
    return result

def calculate_minimum_height(books: List[List[int]], shelfWidth: int, shelf: List[List[int]], current_height: int = 0) -> int:
    if len(books) == 0:
        return current_height + max(height for (_, height) in shelf)

    book_thickness, book_height = books[0]
    add_new_book = float('inf')
    if shelfWidth - sum(thickness for (thickness, _) in shelf) >= book_thickness:
        add_new_book = calculate_minimum_height(books[1:], shelfWidth, shelf + [books[0]], current_height)

    shelf_height = max(height for (_, height) in shelf) if shelf else 0
    add_new_shelf = calculate_minimum_height(books[1:], shelfWidth, [books[0]], shelf_height + current_height)

    return min(add_new_book, add_new_shelf)


if __name__ == "__main__":
    # books: List[List[int]], shelfWidth: int, expected_result: int
    test_cases = [
        ([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4, 6),
        ([[1,3],[2,4],[3,2]], 6, 4),
        ([[11,83],[170,4],[93,80],[155,163],[134,118],[75,14],[122,192],[123,154],[187,29],[160,64],[170,152],[113,179],[60,102],[28,187],[59,95],[187,97],[49,193],[67,126],[75,45],[130,160],[4,102],[116,171],[43,170],[96,188],[54,15],[167,183],[58,158],[59,55],[148,183],[89,95],[90,113],[51,49],[91,28],[172,103],[173,3],[131,78],[11,199],[77,200],[58,65],[77,30],[157,58],[18,194],[101,148],[22,197],[76,181],[21,176],[50,45],[80,174],[116,198],[138,9],[58,125],[163,102],[133,175],[21,39],[141,156],[34,185],[14,113],[11,34],[35,184],[16,132],[78,147],[85,170],[32,149],[46,94],[196,3],[155,90],[9,114],[117,119],[17,157],[94,178],[53,55],[103,142],[70,121],[9,141],[16,170],[92,137],[157,30],[94,82],[144,149],[128,160],[8,147],[153,198],[12,22],[140,68],[64,172],[86,63],[66,158],[23,15],[120,99],[27,165],[79,174],[46,19],[60,98],[160,172],[128,184],[63,172],[135,54],[40,4],[102,171],[29,125],[81,9],[111,197],[16,90],[22,150],[168,126],[187,61],[47,190],[54,110],[106,102],[55,47],[117,134],[33,107],[2,10],[18,62],[109,188],[113,37],[59,159],[120,175],[17,147],[112,195],[177,53],[148,173],[29,105],[196,32],[123,51],[29,19],[161,178],[148,2],[70,124],[126,9],[105,87],[41,121],[147,10],[78,167],[91,197],[22,98],[73,33],[148,194],[166,64],[33,138],[139,158],[160,19],[140,27],[103,109],[88,16],[99,181],[2,140],[50,188],[200,77],[73,84],[159,130],[115,199],[152,79],[1,172],[124,136],[117,138],[158,86],[193,150],[56,57],[150,133],[52,186],[21,145],[127,97],[108,110],[174,44],[199,169],[139,200],[66,48],[52,190],[27,86],[142,191],[191,79],[126,114],[125,100],[176,95],[104,79],[146,189],[144,78],[52,106],[74,74],[163,128],[34,181],[20,178],[15,107],[105,8],[66,142],[39,126],[95,59],[164,69],[138,18],[110,145],[128,200],[149,150],[149,93],[145,140],[90,170],[81,127],[57,151],[167,127],[95,89]], 200, 15672)
    ]

    for test_case_num, (books, shelfWidth, expected_result) in enumerate(test_cases):
        result = iterative(books, shelfWidth)
        assert expected_result == result, f"(recursive) Test case {test_case_num} failed: {expected_result=} {result=}"
    print("All tests passed!")
