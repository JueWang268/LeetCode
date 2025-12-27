import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # maintain pq for end time?
        roomuse = [0] * n
        availableRooms = list(range(n)) # another pq
        heapify(availableRooms)
        meetings.sort()
        pq = [] # meetings in progress, (endtime, room)

        for meet in meetings:
            # check if any meetings finished by start time?
            while pq and pq[0][0] <= meet[0]:
                f = heapq.heappop(pq)
                heapq.heappush(availableRooms, f[1])

            if not availableRooms:
                # meeting delayed
                endMeet, room = heapq.heappop(pq)
                # heapq.heappush(availableRooms, endMeet[1])

                # while pq and endMeet[0] == pq[0][0]:
                #     heapq.heappush(availableRooms, heapq.heappop(pq)[1])
                delay = endMeet - meet[0]
                meet[1] += delay
                heapq.heappush(pq, (meet[1], room))
            else:
                room = heapq.heappop(availableRooms)
                heapq.heappush(pq, (meet[1], room))


            # if there's empty room, start meetign in that room
            # lowestAvail = heapq.heappop(availableRooms)
            # print(f"meeting {meet} starts in {lowestAvail}")
            roomuse[room] += 1
        print(roomuse)
        # print(roomuse[72])
        return roomuse.index(max(roomuse))



            
