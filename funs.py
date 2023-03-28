import datetime

import pandas
import random
import pandas as pd

from docxtpl import DocxTemplate, R


def get_random_list(value, num):
    """获取动态值列表"""
    random_list = [value]
    if value == 'N/A':
        random_list = random_list * num
    else:
        low = int(value - value * 0.005)
        high = int(value + value * 0.005)
        for i in range(num - 1):
            random_list.append(random.randint(low, high))
    return random_list


def del_datatime(time, mark):
    if isinstance(time, str):
        new_time = time
    else:
        if mark == 1:
            new_time = time.strftime("%Y-%m-%d")
        else:
            new_time = time.strftime("%Y.%m")

    return new_time


def read_xls(xls_file, sm_n):
    """读取excel数据，构造车辆信息列表"""
    sheet1 = pandas.read_excel(xls_file, index_col=0, sheet_name=0)
    sheet2 = pandas.read_excel(xls_file, index_col=0, sheet_name=1)
    row1, col1 = sheet1.shape
    sheet2 = sheet2.fillna('N/A')
    # 获取动态参数项
    length_list = get_random_list(sheet2.iloc[0, 1], sm_n)
    width_list = get_random_list(sheet2.iloc[1, 1], sm_n)
    height_list = get_random_list(sheet2.iloc[2, 1], sm_n)
    up_edge_h_list = get_random_list(sheet2.iloc[3, 1], sm_n)
    down_edge_h_list = get_random_list(sheet2.iloc[4, 1], sm_n)

    # 近光灯
    headlamp_d_list = get_random_list(sheet2.iloc[7, 1], sm_n)
    headlamp_e_list = get_random_list(sheet2.iloc[7, 2], sm_n)
    headlamp_h1_list = get_random_list(sheet2.iloc[7, 3], sm_n)
    headlamp_h2_list = get_random_list(sheet2.iloc[7, 4], sm_n)
    # 前位灯
    fp_lamp_d_list = get_random_list(sheet2.iloc[9, 1], sm_n)
    fp_lamp_e_list = get_random_list(sheet2.iloc[9, 2], sm_n)
    fp_lamp_h1_list = get_random_list(sheet2.iloc[9, 3], sm_n)
    fp_lamp_h2_list = get_random_list(sheet2.iloc[9, 4], sm_n)
    # 后位灯
    rp_lamp_d_list = get_random_list(sheet2.iloc[23, 1], sm_n)
    rp_lamp_e_list = get_random_list(sheet2.iloc[23, 2], sm_n)
    rp_lamp_h1_list = get_random_list(sheet2.iloc[23, 3], sm_n)
    rp_lamp_h2_list = get_random_list(sheet2.iloc[23, 4], sm_n)
    # 前雾灯
    ffog_lamp_e_list = get_random_list(sheet2.iloc[11, 2], sm_n)
    ffog_lamp_h1_list = get_random_list(sheet2.iloc[11, 3], sm_n)
    ffog_lamp_h2_list = get_random_list(sheet2.iloc[11, 4], sm_n)
    # 前转向
    if sheet2.iloc[13, 1] == sheet2.iloc[9, 1]:
        fd_lamp_d_list = fp_lamp_d_list
    else:
        fd_lamp_d_list = get_random_list(sheet2.iloc[13, 1], sm_n)
    if sheet2.iloc[13, 2] == sheet2.iloc[9, 2]:
        fd_lamp_e_list = fp_lamp_e_list
    else:
        fd_lamp_e_list = get_random_list(sheet2.iloc[13, 2], sm_n)
    if sheet2.iloc[13, 3] == sheet2.iloc[9, 3]:
        fd_lamp_h1_list = fp_lamp_h1_list
    else:
        fd_lamp_h1_list = get_random_list(sheet2.iloc[13, 3], sm_n)
    if sheet2.iloc[13, 4] == sheet2.iloc[9, 4]:
        fd_lamp_h2_list = fp_lamp_h2_list
    else:
        fd_lamp_h2_list = get_random_list(sheet2.iloc[13, 4], sm_n)
    # 后转向
    if sheet2.iloc[15, 1] == sheet2.iloc[23, 1]:
        rd_lamp_d_list = rp_lamp_d_list
    else:
        rd_lamp_d_list = get_random_list(sheet2.iloc[15, 1], sm_n)
    if sheet2.iloc[15, 2] == sheet2.iloc[23, 2]:
        rd_lamp_e_list = rp_lamp_e_list
    else:
        rd_lamp_e_list = get_random_list(sheet2.iloc[15, 2], sm_n)
    if sheet2.iloc[15, 3] == sheet2.iloc[23, 3]:
        rd_lamp_h1_list = rp_lamp_h1_list
    else:
        rd_lamp_h1_list = get_random_list(sheet2.iloc[15, 3], sm_n)
    if sheet2.iloc[15, 4] == sheet2.iloc[23, 4]:
        rd_lamp_h2_list = rp_lamp_h2_list
    else:
        rd_lamp_h2_list = get_random_list(sheet2.iloc[15, 4], sm_n)
    # 侧转向
    sd_lamp_k_list = get_random_list(sheet2.iloc[17, 1], sm_n)
    sd_lamp_h1_list = get_random_list(sheet2.iloc[17, 3], sm_n)
    sd_lamp_h2_list = get_random_list(sheet2.iloc[17, 4], sm_n)
    # 昼间行驶灯
    if sheet2.iloc[31, 1] == sheet2.iloc[9, 1]:
        daytime_lamp_d_list = fp_lamp_d_list
    else:
        daytime_lamp_d_list = get_random_list(sheet2.iloc[31, 1], sm_n)
    # if sheet2.iloc[31, 2] == sheet2.iloc[9, 2]:
    #     daytime_lamp_e_list = fp_lamp_e_list
    # else:
    #     daytime_lamp_e_list = get_random_list(sheet2.iloc[31, 2], sm_n)
    if sheet2.iloc[31, 3] == sheet2.iloc[9, 3]:
        daytime_lamp_h1_list = fp_lamp_h1_list
    else:
        daytime_lamp_h1_list = get_random_list(sheet2.iloc[31, 3], sm_n)
    if sheet2.iloc[31, 4] == sheet2.iloc[9, 4]:
        daytime_lamp_h2_list = fp_lamp_h2_list
    else:
        daytime_lamp_h2_list = get_random_list(sheet2.iloc[31, 4], sm_n)
    # 制动灯
    if sheet2.iloc[19, 1] == sheet2.iloc[23, 1]:
        stop_lamp_d_list = rp_lamp_d_list
    else:
        stop_lamp_d_list = get_random_list(sheet2.iloc[19, 1], sm_n)
    if sheet2.iloc[19, 2] == sheet2.iloc[23, 2]:
        stop_lamp_e_list = rp_lamp_e_list
    else:
        stop_lamp_e_list = get_random_list(sheet2.iloc[19, 2], sm_n)
    if sheet2.iloc[19, 3] == sheet2.iloc[23, 3]:
        stop_lamp_h1_list = rp_lamp_h1_list
    else:
        stop_lamp_h1_list = get_random_list(sheet2.iloc[19, 3], sm_n)
    if sheet2.iloc[19, 4] == sheet2.iloc[23, 4]:
        stop_lamp_h2_list = rp_lamp_h2_list
    else:
        stop_lamp_h2_list = get_random_list(sheet2.iloc[19, 4], sm_n)
    # 高位制动
    h_stop_lamp_h2_list = get_random_list(sheet2.iloc[21, 4], sm_n)
    # 倒车灯
    reversing_lamp_h1_list = get_random_list(sheet2.iloc[25, 3], sm_n)
    reversing_lamp_h2_list = get_random_list(sheet2.iloc[25, 4], sm_n)
    # 后雾灯
    # rfog_stop_distance_list = get_random_list(sheet2.iloc[27, 1], sm_n)
    if sheet2.iloc[27, 3] == sheet2.iloc[25, 3]:
        rfog_lamp_h1_list = reversing_lamp_h1_list
    else:
        rfog_lamp_h1_list = get_random_list(sheet2.iloc[27, 3], sm_n)
    if sheet2.iloc[27, 4] == sheet2.iloc[25, 4]:
        rfog_lamp_h2_list = reversing_lamp_h2_list
    else:
        rfog_lamp_h2_list = get_random_list(sheet2.iloc[27, 4], sm_n)
    # 示廓灯
    # om_lamp_fe_list = get_random_list(sheet2.iloc[29, 1], sm_n)
    om_lamp_e_list = get_random_list(sheet2.iloc[29, 2], sm_n)
    om_lamp_h1_list = get_random_list(sheet2.iloc[29, 3], sm_n)
    om_lamp_h2_list = get_random_list(sheet2.iloc[29, 4], sm_n)
    # 非三角回复反射器
    reflector_d_list = get_random_list(sheet2.iloc[33, 1], sm_n)
    reflector_e_list = get_random_list(sheet2.iloc[33, 2], sm_n)
    reflector_h1_list = get_random_list(sheet2.iloc[33, 3], sm_n)
    reflector_h2_list = get_random_list(sheet2.iloc[33, 4], sm_n)
    # 前侧标志灯
    fsm_lamp_k_list = get_random_list(sheet2.iloc[35, 1], sm_n)
    fsm_lamp_h1_list = get_random_list(sheet2.iloc[35, 3], sm_n)
    fsm_lamp_h2_list = get_random_list(sheet2.iloc[35, 4], sm_n)
    # 前侧回复
    fs_reflector_k_list = get_random_list(sheet2.iloc[37, 1], sm_n)
    fs_reflector_h1_list = get_random_list(sheet2.iloc[37, 3], sm_n)
    fs_reflector_h2_list = get_random_list(sheet2.iloc[37, 4], sm_n)
    # 后侧标志灯
    rsm_lamp_d_list = get_random_list(sheet2.iloc[39, 1], sm_n)
    rsm_lamp_k_list = get_random_list(sheet2.iloc[39, 2], sm_n)
    rsm_lamp_h1_list = get_random_list(sheet2.iloc[39, 3], sm_n)
    rsm_lamp_h2_list = get_random_list(sheet2.iloc[39, 4], sm_n)
    # 后侧回复
    rs_reflector_d_list = get_random_list(sheet2.iloc[41, 1], sm_n)
    rs_reflector_k_list = get_random_list(sheet2.iloc[41, 2], sm_n)
    rs_reflector_h1_list = get_random_list(sheet2.iloc[41, 3], sm_n)
    rs_reflector_h2_list = get_random_list(sheet2.iloc[41, 4], sm_n)
    # 前驻车灯
    if sheet2.iloc[43, 2] == sheet2.iloc[9, 2]:
        fpark_lamp_e_list = fp_lamp_e_list
    else:
        fpark_lamp_e_list = get_random_list(sheet2.iloc[43, 2], sm_n)
    if sheet2.iloc[43, 3] == sheet2.iloc[9, 3]:
        fpark_lamp_h1_list = fp_lamp_h1_list
    else:
        fpark_lamp_h1_list = get_random_list(sheet2.iloc[43, 3], sm_n)
    if sheet2.iloc[43, 4] == sheet2.iloc[9, 4]:
        fpark_lamp_h2_list = fp_lamp_h2_list
    else:
        fpark_lamp_h2_list = get_random_list(sheet2.iloc[43, 4], sm_n)
    # 后驻车灯
    if sheet2.iloc[45, 2] == sheet2.iloc[23, 2]:
        rpark_lamp_e_list = rp_lamp_e_list
    else:
        rpark_lamp_e_list = get_random_list(sheet2.iloc[45, 2], sm_n)
    if sheet2.iloc[45, 3] == sheet2.iloc[23, 3]:
        rpark_lamp_h1_list = rp_lamp_h1_list
    else:
        rpark_lamp_h1_list = get_random_list(sheet2.iloc[45, 3], sm_n)
    if sheet2.iloc[45, 4] == sheet2.iloc[23, 4]:
        rpark_lamp_h2_list = rp_lamp_h2_list
    else:
        rpark_lamp_h2_list = get_random_list(sheet2.iloc[45, 4], sm_n)

    # 灯光强度
    left_light_list = get_random_list(sheet2.iloc[49, 2], sm_n)
    right_light_list = get_random_list(sheet2.iloc[49, 3], sm_n)

    # 序号
    n_list = [i for i in range(1, row1 + 1)]

    vehicle_list = []
    tol_list = []

    for n in range(0, row1):
        t_sam_num = sheet1.iloc[n, 0]
        t_vin = sheet1.iloc[n, 1]
        t_pd = sheet1.iloc[n, 4]
        t_sd = sheet1.iloc[n, 5]
        t_cd = sheet1.iloc[n, 7]

        t = {"t_sm_num": t_sam_num, "t_vin": t_vin, "t_PD": t_pd, "t_SD": t_sd, "t_CD": t_cd}
        t.update({"t_n": n_list[n]})

        tol_list.append(t)

    for r in range(0, sm_n):
        sample_num = sheet1.iloc[r, 0]  # 样车数量
        vin = sheet1.iloc[r, 1]  # vin
        engine_num = sheet1.iloc[r, 3]  # 发动机号
        pd_ = del_datatime(sheet1.iloc[r, 4], 0)   # 生产日期
        # pd_ = sheet1.iloc[r, 4]   # 生产日期

        sd = del_datatime(sheet1.iloc[r, 5], 1)  # 送样日期
        # sd = sheet1.iloc[r, 5]  # 送样日期

        pg_n = sheet1.iloc[r, 6]  # 乘员数
        cd = del_datatime(sheet1.iloc[r, 7], 1)  # 检测日期
        # cd = sheet1.iloc[r, 7]  # 检测日期

        if sheet2.iloc[47, 2] == 'N/A' and sheet2.iloc[47, 3] == 'N/A':
            trunk = 'N/A'
        else:
            if pg_n <= 5:
                trunk_length = sheet2.iloc[47, 2]
            else:
                trunk_length = sheet2.iloc[47, 3]
            trunk = "行李区的纵向长度为{0}mm，为车长的{1}%".format(trunk_length, round(trunk_length / length_list[r] * 100, 1))
        # print(trunk)

        # 灯光强度计算
        left_light = int(left_light_list[r]/100)*100
        right_light = int(right_light_list[r]/100)*100

        d = {"sm_num": sample_num, "vin": vin, "PD": pd_, "SD": sd, "CD": cd, "eng_num": engine_num, "pg_n": pg_n}
        d.update({"n": n_list[r], "length": length_list[r], "width": width_list[r], "height": height_list[r],
                  "trunk": trunk,
                  "up_edge_h": up_edge_h_list[r], "down_edge_h": down_edge_h_list[r],
                  "headlamp_d": headlamp_d_list[r], "headlamp_e": headlamp_e_list[r],
                  "headlamp_h1": headlamp_h1_list[r], "headlamp_h2": headlamp_h2_list[r],
                  "fp_lamp_d": fp_lamp_d_list[r], "fp_lamp_e": fp_lamp_e_list[r], "fp_lamp_h1": fp_lamp_h1_list[r],
                  "fp_lamp_h2": fp_lamp_h2_list[r], "ffog_lamp_e": ffog_lamp_e_list[r],
                  "ffog_lamp_h1": ffog_lamp_h1_list[r], "ffog_lamp_h2": ffog_lamp_h2_list[r],
                  "fd_lamp_d": fd_lamp_d_list[r], "fd_lamp_e": fd_lamp_e_list[r], "fd_lamp_h1": fd_lamp_h1_list[r],
                  "fd_lamp_h2": fd_lamp_h2_list[r], "rd_lamp_d": rd_lamp_d_list[r], "rd_lamp_e": rd_lamp_e_list[r],
                  "rd_lamp_h1": rd_lamp_h1_list[r], "rd_lamp_h2": rd_lamp_h2_list[r],
                  "daytime_lamp_d": daytime_lamp_d_list[r], "daytime_lamp_h1": daytime_lamp_h1_list[r],
                  "daytime_lamp_h2": daytime_lamp_h2_list[r], "sd_lamp_k": sd_lamp_k_list[r],
                  "sd_lamp_h1": sd_lamp_h1_list[r], "sd_lamp_h2": sd_lamp_h2_list[r],
                  "rp_lamp_d": rp_lamp_d_list[r], "rp_lamp_e": rp_lamp_e_list[r], "rp_lamp_h1": rp_lamp_h1_list[r],
                  "rp_lamp_h2": rp_lamp_h2_list[r], "stop_lamp_d": stop_lamp_d_list[r],
                  "stop_lamp_e": stop_lamp_e_list[r], "stop_lamp_h1": stop_lamp_h1_list[r],
                  "stop_lamp_h2": stop_lamp_h2_list[r], "h_stop_lamp_h2": h_stop_lamp_h2_list[r],
                  "reversing_lamp_h1": reversing_lamp_h1_list[r], "reversing_lamp_h2": reversing_lamp_h2_list[r],
                  "rfog_lamp_h1": rfog_lamp_h1_list[r], "rfog_lamp_h2": rfog_lamp_h2_list[r],
                  "om_lamp_e": om_lamp_e_list[r], "om_lamp_h1": om_lamp_h1_list[r],
                  "om_lamp_h2": om_lamp_h2_list[r], "reflector_d": reflector_d_list[r],
                  "reflector_e": reflector_e_list[r], "reflector_h1": reflector_h1_list[r],
                  "reflector_h2": reflector_h2_list[r], "fsm_lamp_k": fsm_lamp_k_list[r],
                  "fsm_lamp_h1": fsm_lamp_h1_list[r], "fsm_lamp_h2": fsm_lamp_h2_list[r],
                  "fs_reflector_k": fs_reflector_k_list[r], "fs_reflector_h1": fs_reflector_h1_list[r],
                  "fs_reflector_h2": fs_reflector_h2_list[r], "rsm_lamp_d": rsm_lamp_d_list[r],
                  "rsm_lamp_k": rsm_lamp_k_list[r], "rsm_lamp_h1": rsm_lamp_h1_list[r],
                  "rsm_lamp_h2": rsm_lamp_h2_list[r], "rs_reflector_d": rs_reflector_d_list[r],
                  "rs_reflector_k": rs_reflector_k_list[r], "rs_reflector_h1": rs_reflector_h1_list[r],
                  "rs_reflector_h2": rs_reflector_h2_list[r], "fpark_lamp_e": fpark_lamp_e_list[r],
                  "fpark_lamp_h1": fpark_lamp_h1_list[r], "fpark_lamp_h2": fpark_lamp_h2_list[r],
                  "rpark_lamp_e": rpark_lamp_e_list[r], "rpark_lamp_h1": rpark_lamp_h1_list[r],
                  "rpark_lamp_h2": rpark_lamp_h2_list[r], "left_light": left_light, "right_light": right_light,
                  "tol_light": left_light+right_light
                  })

        vehicle_list.append(d)

    return vehicle_list, tol_list


def make_context(vehicle_list, tol_list):
    """构造文本"""
    context = {
        "page_break": R('\f'),
        "blank": "——",
        "vehicle_list": vehicle_list,
        "tol_list": tol_list
    }

    return context


def merge(tem_file, context, dst_path):
    """渲染模板"""
    doc = DocxTemplate(tem_file)
    doc.render(context)
    doc.save(dst_path)
