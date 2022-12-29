# https://leetcode.com/problems/single-threaded-cpu/


import heapq

def getOrder(tasks):
        n = len(tasks[0])   # no. of tasks

        next_task = []
        task_processing_order = []

        sorted_tasks = [(enqueueTime, processingTime, idx) for idx, (enqueueTime, processingTime) in enumerate(tasks)]
        sorted_tasks.sort() # sorted tasks as per processingTime

        print(sorted_tasks)

        curr_time = 0
        task_index = 0

        while task_index < n or next_task:
            if not next_task and curr_time < sorted_tasks[task_index][0]:
                curr_time = sorted_tasks[task_index][0]

            while task_index < len(sorted_tasks) and curr_time >= sorted_tasks[task_index][0]:
                enqueueTime, processingTime, index = sorted_tasks[task_index]
                heapq.heappush(next_task, (processingTime, index)) 
                task_index += 1

            processingTime, index = heapq.heappop(next_task)

            curr_time += processingTime

            task_processing_order.append(index)

        return task_processing_order


if __name__ == '__main__':
    tasks = [[1,2],[2,4],[3,2],[4,1]]

    print(getOrder(tasks))
