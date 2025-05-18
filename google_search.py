from googlesearch import search



def googlesearch_function(query):
    results = search(f"{query}", advanced=True, num_results=30, start_num=10)
    results_list = []
    for result in results:
        # If result is a custom object, convert to dict
        if hasattr(result, '__dict__'):
            results_list.append(result.__dict__)
        else:
            results_list.append(result)
    return results_list

# googlesearch_function("python developer jobs in Pune 8LPA")