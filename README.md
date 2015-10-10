PyGcs
=====

## Example
	from PyGcs import PyGcs
	gcs = PyGcs()
	gcs.set_api_key(YOUR_API_KEY)
	gcs.set_cx_id(YOUR_CX_ID)
	gcs.set_query(YOUR_QUERY)
	result = gcs.search()

	for r in result:
		print r.get_link()

## Contributing
Since I am still new to Python, I would love some constructive feedback.
Please help this code become better, as well as helping me to become better.

## Todo
1.	Add option to search for more than one page(10 sites)
