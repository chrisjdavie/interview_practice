from copy import copy

blocks = [
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True
    },
]

reqs = ["gym", "school", "store"]

# left to right
closest_dist = {r: len(blocks) + 1 for r in reqs }
block_closest_dist_lhs = []

for blk in enumerate(blocks):
    for rq in reqs:
        if blk[rq]:
            closest_dist[rq] = 0
        else:
            closest_dist[rq] += 1
        block_closest_dist_lhs.append(
            copy(closest_dist)
        )

closest_dist = {r: len(blocks) + 1 for r in reqs }
block_closest_dist_rhs = []

for blk in enumerate(blocks[::-1]):
    for rq in reqs:
        if blk[rq]:
            closest_dist[rq] = 0
        else:
            closest_dist[rq] += 1
        block_closest_dist_lhs.append(
            copy(closest_dist)
        )

block_closest_dist_rhs.reverse()


shortest_dist = len(blocks) + 1
index_sln = -1

for index_blk, (blk_cls_lhs, blk_cls_rhs) in enumerate(zip(block_closest_dist_lhs, block_closest_dist_rhs)):
    dists = []
    for rq in reqs:
        dists.append(min(blk_cls_lhs[rq], blk_cls_rhs[rq]))
    if min_blk_dis := max(dists) < shortest_dist:
        shortest_dist = min_blk_dis
        index_sln = index_blk

print(index_sln)


# # right to left
# closest_dist = {r: len(blocks) + 1 for r in reqs }

# for index_blk, blk in enumerate(blocks[::-1]):
#     for rq in reqs:
#         if blk[rq]:
#             closest_dist[rq] = 0
#         else:
#             closest_dist[rq] += 1
#         if min_dist := min(closest_dist.values()) < shortest_dist:
#             shortest_dist = min_dist
#             index_sln = len(blocks) - index_blk - 1
