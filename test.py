import pandas

# xls = r"C:\Users\kindr\Desktop\test\样车车辆信息.xlsx"
#
# df_recoder = pandas.read_excel(xls, index_col=0, sheet_name=1)
# row1, col1 = df_recoder.shape
#
# df_recoder = df_recoder.fillna("N/A")
# print(row1, col1)
# 基本参数
# engine_num = df_recoder.iloc[0, 1]
# length = df_recoder.iloc[0, 1]
# width = df_recoder.iloc[1, 1]
# height = df_recoder.iloc[2, 1]
# up_edge_h = df_recoder.iloc[3, 1]
# down_edge_h = df_recoder.iloc[4, 1]
# 近光灯
# headlamp_d = df_recoder.iloc[7, 1]
# headlamp_e = df_recoder.iloc[7, 2]
# headlamp_H1 = df_recoder.iloc[7, 3]
# headlamp_H2 = df_recoder.iloc[7, 4]
# 前位灯
# fp_lamp_D = df_recoder.iloc[9, 1]
# fp_lamp_E = df_recoder.iloc[9, 2]
# fp_lamp_H1 = df_recoder.iloc[9, 3]
# fp_lamp_H2 = df_recoder.iloc[9, 4]
# 前雾灯
# ffog_lamp_D = df_recoder.iloc[11, 1]
# ffog_lamp_E = df_recoder.iloc[11, 2]
# ffog_lamp_H1 = df_recoder.iloc[11, 3]
# ffog_lamp_H2 = df_recoder.iloc[11, 4]
# 前转向
# fd_lamp_D = df_recoder.iloc[13, 1]
# fd_lamp_E = df_recoder.iloc[13, 2]
# fd_lamp_H1 = df_recoder.iloc[13, 3]
# fd_lamp_H2 = df_recoder.iloc[13, 4]
# 后转向
# rd_lamp_D = df_recoder.iloc[15, 1]
# rd_lamp_E = df_recoder.iloc[15, 2]
# rd_lamp_H1 = df_recoder.iloc[15, 3]
# rd_lamp_H2 = df_recoder.iloc[15, 4]
# 侧转向
# sd_lamp_K = df_recoder.iloc[17, 1]
# sd_lamp_H1 = df_recoder.iloc[17, 3]
# sd_lamp_H2 = df_recoder.iloc[17, 4]
# 制动灯
# stop_lamp_D = df_recoder.iloc[19, 1]
# stop_lamp_E = df_recoder.iloc[19, 2]
# stop_lamp_H1 = df_recoder.iloc[19, 3]
# stop_lamp_H2 = df_recoder.iloc[19, 4]
# 高位制动
# h_stop_lamp_H2 = df_recoder.iloc[21, 4]
# 后位灯
# rp_lamp_D = df_recoder.iloc[23, 1]
# rp_lamp_E = df_recoder.iloc[23, 2]
# rp_lamp_H1 = df_recoder.iloc[23, 3]
# rp_lamp_H2 = df_recoder.iloc[23, 4]
# 倒车灯
# reversing_lamp_H1 = df_recoder.iloc[25, 3]
# reversing_lamp_H2 = df_recoder.iloc[25, 4]
# 后雾灯
# rfog_stop_distance = df_recoder.iloc[27, 1]
# rfog_lamp_H1 = df_recoder.iloc[27, 3]
# rfog_lamp_H2 = df_recoder.iloc[27, 4]
# 示廓灯
# om_lamp_FE = df_recoder.iloc[29, 1]
# om_lamp_RE = df_recoder.iloc[29, 2]
# om_lamp_H1 = df_recoder.iloc[29, 3]
# om_lamp_H2 = df_recoder.iloc[29, 4]
# 昼间行驶灯
# daytime_lamp_D = df_recoder.iloc[31, 1]
# daytime_lamp_E = df_recoder.iloc[31, 2]
# daytime_lamp_H1 = df_recoder.iloc[31, 3]
# daytime_lamp_H2 = df_recoder.iloc[31, 4]
# 非三角回复反射器
# reflector_D = df_recoder.iloc[33, 1]
# reflector_E = df_recoder.iloc[33, 2]
# reflector_H1 = df_recoder.iloc[33, 3]
# reflector_H2 = df_recoder.iloc[33, 4]
# 前侧标志灯
# fsm_lamp_K = df_recoder.iloc[35, 1]
# fsm_lamp_H1 = df_recoder.iloc[35, 3]
# fsm_lamp_H2 = df_recoder.iloc[35, 4]
# 前侧回复
# fs_reflector_K = df_recoder.iloc[37, 1]
# fs_reflector_H1 = df_recoder.iloc[37, 3]
# fs_reflector_H2 = df_recoder.iloc[37, 4]
# 后侧标志灯
# rsm_lamp_D = df_recoder.iloc[39, 1]
# rsm_lamp_K = df_recoder.iloc[39, 2]
# rsm_lamp_H1 = df_recoder.iloc[39, 3]
# rsm_lamp_H2 = df_recoder.iloc[39, 4]
# 后侧回复
# rs_reflector_D = df_recoder.iloc[41, 1]
# rs_reflector_K = df_recoder.iloc[41, 2]
# rs_reflector_H1 = df_recoder.iloc[41, 3]
# rs_reflector_H2 = df_recoder.iloc[41, 4]
# 前驻车灯
# fpark_lamp_e = df_recoder.iloc[43, 1]
# fpark_lamp_h1 = df_recoder.iloc[43, 3]
# fpark_lamp_h2 = df_recoder.iloc[43, 4]
# 后驻车灯
# rpark_lamp_e = df_recoder.iloc[45, 1]
# rpark_lamp_h1 = df_recoder.iloc[45, 3]
# rpark_lamp_h2 = df_recoder.iloc[45, 4]
# 轮重
# FL_weight = df_recoder.iloc[47, 1]
# RL_weight = df_recoder.iloc[47, 2]
# FR_weight = df_recoder.iloc[47, 3]
# RR_weight = df_recoder.iloc[47, 4]
# 远光光强
# left_cd = df_recoder.iloc[49, 1]
# right_cd = df_recoder.iloc[49, 2]

# import random
#
# num = 65800
# low = int(num - num * 0.005)
# high = int(num + num * 0.005)
# print(low)
# print(high)
#
# rand_num = random.randint(low, high)
# print(rand_num)
# a = int(rand_num/100)*100
# print(a)
import datetime


 a =
