import httpx
import okx.PublicData as PublicData
import time
import datetime

flag = "0"  # 实盘:0 , 模拟盘：1

if __name__ == "__main__":
    coinType = input("请输入币种信息，大写英文：")
    coinType = coinType.upper()
    while True:
        publicDataAPI = PublicData.PublicAPI(flag=flag,debug=False)
        # 获取交易产品基础信息
        try:
            result = publicDataAPI.get_mark_price(
                instType="SWAP",
                instId=f"{coinType}-USDT-SWAP"
            )
            systime = publicDataAPI.get_system_time() #{'code': '0', 'data': [{'ts': '1704163736765'}], 'msg': ''}
            # print(systime["data"][0]["ts"])
            # datetime_str2 = datetime.datetime.strftime(datetime.datetime.fromtimestamp(int(systime["data"][0]["ts"])), '%Y-%m-%d %H:%M:%S')
            # print(datetime_str2)
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            if result["code"]=="0": #错误判断
                print(time_str + f"  {coinType}:" + result["data"][0]["markPx"])# {'code': '0', 'data': [{'instId': 'ETH-USDT-SWAP', 'instType': 'SWAP', 'markPx': '2381.38', 'ts': '1704162777391'}], 'msg': ''}
            else:
                print("发生错误: "+result["msg"])
            time.sleep(1)
        except httpx.ConnectError:
            print("Http连接错误，准备重新连接")