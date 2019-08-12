"""
This program is for calculating the edit distance of two strings by
the edit distance algorithm by Vladimir Levenshtein

1. Created API endpoint with POST request, where two strings can be passed as a part of JSON text
2. Created recursive function with a terminating condition of one of the length being zero.
3. API sends response in the form of dictionary, which is further converted to JSON format

"""


from flask import Flask, jsonify, request

#Object of Flask class
app = Flask(__name__)

#Create POST method with endpoint
@app.route('/edit_distance', methods = ['POST'])
def result_edit_distance():
	# Fetch data as dictionary from JSON input
	data = request.get_json()
	str1 = data['string1']
	str2 = data['string2']
	#Jeturn the result in form of JSON
	return jsonify({'edit distance of the two strings':edit_distance_calculator(str1, str2, len(str1), len(str2))})

def edit_distance_calculator(str1, str2, len1 , len2):

	# If first string is empty, the only option is to
	# insert all characters of second string into first
	if len1==0:
		return len2

	# If second string is empty, the only option is to
	# remove all characters of first string
	if len2==0:
		return len1

	# If last characters of two strings are same, nothing
	# much to do. Ignore last characters and get count for
	# remaining strings.
	if str1[len1-1]==str2[len2-1]:
		return edit_distance_calculator(str1,str2,len1-1,len2-1)

	# If last characters are not same, consider all three
	# operations on last character of first string, recursively
	# compute minimum cost for all three operations and take
	# minimum of three values.
	return 1 + min(edit_distance_calculator(str1, str2, len1, len2-1), # Insert
				edit_distance_calculator(str1, str2, len1-1, len2), # Remove
				edit_distance_calculator(str1, str2, len1-1, len2-1) # Replace
				)

app.run(port=4657)




