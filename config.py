SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:new_password@localhost:5432/castingagency'
SQLALCHEMY_UNIT_TEST_URI = 'postgresql://postgres:new_password@localhost:5432/castingagencytest'
LISTINGS_PER_PAGE = 8

# paginate results
def paginate_results(request, selections):
  page = request.args.get('page', 1, type=int)
  start = (page - 1) * LISTINGS_PER_PAGE
  end = start + LISTINGS_PER_PAGE
  listings = [listing.format() for listing in selections]
  current_listings = listings[start:end]

  return current_listings