# Get lowest contiguous subarray with strictly decreasing percentage build

def binary_search(run):
	low, high = 0, len(run) - 1
	idx = -1
	while low <= high:
		mid = (low + high)//2
		if run[mid] == False:
			idx = mid
			high = mid - 1
		else:
			low = mid + 1
	return idx

def get_build_percent(run):
	#find build percent- binary search- first instance of False
	builds = len(run)
	false_index = binary_search(run)
	true_index = false_index - 1
	return (true_index + 1) * 100/(true_index + (builds - false_index + 1))


def get_lowest_decreasing(build_runs):
	# precompute to get percentages
	build_percents = []
	for run in build_runs:
		p = get_build_percent(run)
		build_percents.append(p)
	l = [1] * len(build_percents)
	start_index = [0]*len(build_percents)
	l[0] = 1
	start_index[0] = 0
	
	maximum = 1
	max_at = 0
	for i in range(1, len(build_percents)):
		if build_percents[i] < build_percents[i-1]:
			l[i] = l[i-1] + 1
			start_index[i] = start_index[i-1]
		else:
			l[i] = 1
			start_index[i] = i
		if maximum < l[i]:
			maximum = l[i]
			max_at = i
			
	return maximum, (start_index[max_at], max_at)

		
    



builds = [
[True, True, True, False, False],
[True, True, True, True, False],
[True, True, True, True, True, True, True, True, True, False, False, False],
[True, False, False, False, False, False],
[True, True, True, True, True, True, True, True, True, False],
[True, False]
]
print(get_lowest_decreasing(builds))