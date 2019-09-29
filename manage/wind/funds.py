from manage.wind import w


SECTOR_IDS = ['1000031768000000', '1000031769000000', '1000031770000000', '1000031771000000', '1000031772000000', '1000031774000000']


def sector_funds(sectorid, date):
    data = w.wset("sectorconstituent", f"date={date};sectorid={sectorid};field=date,wind_code")
    codes = data.Data[1]
    return codes


def csi_open_funds(date):
    """根据日期获取证监会分类下全部开放式基金"""
    funds = []
    for sectorid in SECTOR_IDS:
        data = sector_funds(sectorid, date)
        funds.extend(data)
    return funds
