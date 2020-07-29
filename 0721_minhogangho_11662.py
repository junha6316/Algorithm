
x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4 = list(map(int, input().split()))


def length(g_loc,m_loc):
    l = (g_loc[0]-m_loc[0])*(g_loc[0]-m_loc[0]) + (g_loc[1]-m_loc[1])*(g_loc[1]-m_loc[1])
    return l**0.5

m_start = [x_1, y_1]
m_end = [x_2, y_2]
m_dir = (y_2-y_1)/(x_2-x_1)


g_start = [x_3, y_3]
g_end = [x_4, y_4]
g_dir = (y_4-y_3)/(x_4-x_3)

l_st = length(g_start, m_start)
l_end = length(g_end, m_end)


if m_dir == g_dir or l_st == l_end:
    print(length(g_start, m_start))
else:
    if g_dir * (x_2 - x_3) + y_3 <= y_2:
        print(0.000000)

    elif l_st >= l_end:

    elif l_st < l_end:




#
#

# print(l_st, l_end)
# '''
# 0 0 1 1 2 2 3 3 동일 라
# 0 0 1 1 1 0 0 1 만난다.
# 인 좁혀짐
# 5 5 10 10 7 2 20 30짐 벌어
# '''
#
# # if l_st > l_end: ans =l_st #점차 길이 줄어들
# # else: ans = l_end #점차 길이가 늘어날
# ans = l_end
#
# while (True):
#     m_mid = [(m_start[0]+m_end[0])/2 , (m_start[1]+m_end[1])/2]
#     g_mid = [(g_start[0]+g_end[0])/2 , (g_start[1]+g_end[1])/2]
#     l = length(g_mid, m_mid)
#     if ans > l:
#         m_end = [m_mid[0]-0.0000001, m_mid[1]-0.0000001]
#         g_end = [g_mid[0]-0.0000001, g_mid[1]-0.0000001]
#         if abs(ans - l) <= 0.0000000001:
#             break
#         else:
#             print(ans, l)
#             ans = l
#
#     elif ans < l:
#         print(ans)
#         m_start = [m_mid[0]+0.0000001,m_mid[1]+0.0000001]
#         g_start = [g_mid[0]+0.0000001,g_mid[1]+0.0000001]
#
#
#
#
#
#
#
#
#
#
# print(ans)

