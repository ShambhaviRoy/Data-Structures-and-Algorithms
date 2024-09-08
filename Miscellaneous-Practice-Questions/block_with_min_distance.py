# Find the block that would minimize the furthest distance from all building in reqs

import sys

def find_block(blocks, reqs):
    n = len(blocks)
    m = len(reqs)
    grid = [[sys.maxsize] * (m+1)] * n
    reqs_map = {}
    idx_map = {}
    for i, req in enumerate(reqs):
        reqs_map[req] = i
        idx_map[i] = req
    
    for r in reqs:
        if blocks[0][r]:
            grid[0][reqs_map[r]] = 0

    for i in range(n):
        for j in range(m):
            grid[i][m] = max(grid[i][m], grid[i][j])  
            result = grid[i][m]      
    
    for i in range(n):
        grid[i][m] = 0
        for j in range(m):
            r = idx_map[j]
            if blocks[i][r]:
                grid[i][j] = 0
            else:
                if grid[i-1][j] != sys.maxsize:
                    grid[i][j] = min(grid[i][j], grid[i-1][j] + 1)
            grid[i][m] = max(grid[i][m], grid[i][j])

            print(grid)

    # for i in reversed(range(n-2)):
    #     for j in range(m):
    #         r = idx_map[j]
    #         if blocks[i][r]:
    #             grid[i][j] = 0
    #         else:
    #             if grid[i+1][j] != sys.maxsize:
    #                 grid[i][j] = min(grid[i][j], grid[i+1][j] + 1)
    #         grid[i][m] = max(grid[i][m], grid[i][j])
    #         result = min(result, grid[i][m])




# def find_block(blocks, reqs):
# 	grid = [[-1] * (len(reqs))] * len(blocks)
# 	reqs_map = {}
# 	for i, req in enumerate(reqs):
# 		# map req to index in reqs array
# 		reqs_map[req] = i
# 	print(reqs_map)
# 	for r in reqs:
# 		if blocks[0][r]:
# 			grid[0][reqs_map[r]] = 0
			
#     print(grid)
		
#     # for r in reqs:
	
		
	
		
	# fill grid, if req is True, dist is 0
# 	for i in range(len(blocks)):
# 		for req in reqs:
# 			j = reqs_map[req]
# 			if blocks[i][req]:
# 				grid[i][j] = 0
# 	print(grid)

# 	# update grid with distances
# 	for i in range(len(reqs)):
# 		for j in range(len(blocks)):
# 			find_nearest_block(grid, j, i)
# 	# print(grid)


# 	block_index = -1
# 	furthest_dist = sys.maxsize
# 	for i in range(len(grid)):
# 		block = grid[i]
# 		if furthest_dist < min(block):
# 			furthest_dist = min(block)
# 			block_index = i
# 	return block_index


# # def find_nearest_block(grid, block_index, req_index):
# # 	# find nearest block
# # 	offset = 1
# # 	blocks = len(grid)
# # 	while offset < block_index or block_index + offset < blocks:
# # 		if grid[block_index + offset][req_index] != -1 or grid[block_index - offset][req_index] != -1:
# # 			grid[block_index + offset][req_index] = offset
# # 			return
# # 		offset += 1
	
    
    
    
#     # dist = 1
# 	# # go ahead (right)
	# while block_index + dist < len(grid):
	# 	if grid[block_index + dist][req_index] != -1:
	# 		grid[block_index + dist][req_index] = dist
	# 		return
	# 	dist += 1
	# dist = 1
	# # go left
	# while dist < block_index:
	# 	if grid[block_index - dist][req_index] != -1:
	# 		grid[block_index - dist][req_index] = dist
	# 		return
	# 	dist -= 1
		
        
		

blocks = [{
'gym' : False,
'school' : True,
'store' : False
},
{
'gym' : True,
'school' : False,
'store' :False
},
{
'gym' : True,
'school' : True,
'store' :False
},
{
'gym' : False,
'school': True,
'store':False
},
{
'gym': False,
'school': True,
'store' :True
}]
reqs = ['gym', 'school', 'store']

find_block(blocks, reqs)
	
