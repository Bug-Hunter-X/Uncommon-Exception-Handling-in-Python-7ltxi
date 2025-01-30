def function_with_improved_error_handling(data):
    processed_data = []
    for item in data:
        try:
            processed_data.append(item['value'])
        except KeyError:
            print(f"Key 'value' not found in item: {item}")
        except TypeError as e:
            print(f"Type error encountered: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {type(e).__name__} - {e}")
    return processed_data

data = [{'value': 1}, {'key': 'value'}, {'value': 3}, 123] #Added a non-dictionary item
result = function_with_improved_error_handling(data)
print(result) # Output: [1, 3]

#Demonstrates handling of non-dictionary items
data2 = [{'value': 1}, {'key': 'value'}, {'value': 3}, 123, {'value':4, 'extra':'data'}]
result2 = function_with_improved_error_handling(data2)
print(result2) # Output: [1, 3, 4]